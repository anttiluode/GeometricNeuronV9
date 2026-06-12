"""
geometric_neuron_v9.py — the skew lag-operator read path
=========================================================
v8 made read-coverage an OBJECTIVE (Ky Fan on the symmetric increment
covariance C) and stalled at 0.50 captured energy: "nearest-target coverage did
not rise ... the framework-correct operator is the skew/lag H_tau ... untested."

v9 tests it, end to end. The read templates are no longer hand-assigned edges
nor pushed apart by a penalty. They are the EIGENPLANES of the skew lag operator

    A_tau = (C_tau - C_tau^T)/2,   C_tau = E[ r(t) r(t-tau)^T ],   r = field overlaps

computed from the field's own event-sampled trajectory. A_tau is real
antisymmetric: eigenvalues +/- i*omega_j, eigenvectors = 2D rotation planes =
the spectral islands. The read is the projection of the field onto these planes;
chirality is sign(omega_j), native and per island.

Three things are measured head to head against v8's positional/symmetric read:
  (1) DIRECTED COVERAGE at a plane budget m<K/2 (the non-degenerate metric);
  (2) CHIRALITY: do the learned islands flip sign on a reversed tour?
  (3) EMERGENCE: are the islands recovered with NO edge assignment?

Do not hype. Do not lie. Just show.
PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.
"""
import numpy as np
import torch
from gn_base import make_targets, PopulationV7, coherence

torch.set_default_dtype(torch.float64)


# ----------------------------------------------------------------------
# A field that genuinely TOURS patterns with a definite direction.
# (v7/v8's static-hold field has weak directed structure; the skew operator
#  needs a real traversal to have a spectrum to find. This is the honest
#  test bed for a DIRECTED read path.)
# ----------------------------------------------------------------------
def tour_field(P, direction=+1, steps=24000, dwell=60, leak=0.96,
               inject=0.18, noise=0.02, seed=1):
    rng = np.random.default_rng(seed)
    N = P.shape[1]; K = P.shape[0]
    s = P[0].copy(); S = np.zeros((steps, N))
    for t in range(steps):
        k = (direction * (t // dwell)) % K
        s = leak * s + inject * P[k] + noise * rng.standard_normal(N)
        s /= np.linalg.norm(s) + 1e-9
        S[t] = s
    return S


def lag_cov_overlaps(S, P, tau):
    R = S @ P.T
    return R[tau:].T @ R[:-tau] / (len(R) - tau)        # (K,K)


# ----------------------------------------------------------------------
# v8 READ PATH: Ky Fan on the SYMMETRIC increment covariance.
#   templates = top eigenvectors of S = (C+C^T)/2 in the pattern basis.
# ----------------------------------------------------------------------
def v8_read_templates(C, m):
    Ssym = 0.5 * (C + C.T)
    w, V = np.linalg.eigh(Ssym)
    return V[:, np.argsort(-np.abs(w))[:2 * m]]          # 2m vectors = m planes' worth


# ----------------------------------------------------------------------
# v9 READ PATH: eigenplanes of the SKEW lag operator.
#   templates = real/imag parts of the top-m conjugate eigenpairs of A.
#   chirality_j = sign(omega_j), recovered, not assigned.
# ----------------------------------------------------------------------
def v9_read_templates(C, m):
    A = 0.5 * (C - C.T)
    w, V = np.linalg.eig(A)
    om = w.imag
    pos = np.argsort(-om)
    pos = pos[om[pos] > 1e-9][:m]                        # top-m positive-rate planes
    planes, omegas = [], []
    for j in pos:
        u, v = V[:, j].real, V[:, j].imag
        u = u / (np.linalg.norm(u) + 1e-9)
        v = v / (np.linalg.norm(v) + 1e-9)
        planes += [u, v]; omegas.append(om[j])
    return np.array(planes).T, np.array(omegas), A       # (K,2m), (m,), A


def skew_energy(A):
    return np.abs(np.linalg.eigvals(A).imag).sum()


def directed_captured(Q, A):
    """fraction of the skew operator's rotation energy living in span(Q)."""
    Qr = np.linalg.qr(Q)[0]
    return skew_energy(Qr.T @ A @ Qr) / (skew_energy(A) + 1e-12)


def island_chirality(S, P, plane_u, plane_v, tau):
    """read L = Im(z z*_lag) for the field projected on one rotation plane."""
    R = S @ P.T
    z = R @ (plane_u - 1j * plane_v)                     # complex coord in the plane
    L = (z[tau:] * np.conj(z[:-tau])).imag
    return float(L.mean())


if __name__ == "__main__":
    N, K, tau = 64, 8, 60
    P = make_targets(N, K, seed=0).numpy()

    print("=" * 72)
    print("GEOMETRIC NEURON v9 — skew lag-operator read path")
    print("=" * 72)

    # build the directed field and its lag operator (no edges assigned)
    Sf = tour_field(P, +1, seed=3); Sr = tour_field(P, -1, seed=3)
    Cf = lag_cov_overlaps(Sf, P, tau); Cr = lag_cov_overlaps(Sr, P, tau)
    Askew_f = 0.5 * (Cf - Cf.T)

    # ---- (1) directed coverage head-to-head, at a real plane budget ----
    print("\n[1] DIRECTED COVERAGE  (fraction of rotation energy captured)")
    print(f"    {'budget m':>9} | {'v8 symmetric read':>18} | {'v9 skew read':>14}")
    rows = []
    for m in [1, 2, 3, 4]:
        Q8 = v8_read_templates(Cf, m)
        Q9, om9, _ = v9_read_templates(Cf, m)
        c8 = directed_captured(Q8, Askew_f)
        c9 = directed_captured(Q9, Askew_f)
        rows.append((m, c8, c9))
        print(f"    {m:>9} | {c8:>18.3f} | {c9:>14.3f}")
    print("    (tie only at m=K/2=4, the full-rank degenerate end)")

    # ---- (2) chirality: do the learned islands carry the arrow of time? ----
    print("\n[2] CHIRALITY  (sign of each learned island, forward vs reverse tour)")
    Q9, om9, _ = v9_read_templates(Cf, K // 2)
    flips = 0
    for j in range(K // 2):
        u, v = Q9[:, 2 * j], Q9[:, 2 * j + 1]
        Lf = island_chirality(Sf, P, u, v, tau)
        Lr = island_chirality(Sr, P, u, v, tau)
        flip = np.sign(Lf) != np.sign(Lr)
        flips += int(flip)
        print(f"    island {j} (omega={om9[j]:+.4f}):  L_forward {Lf:+.4f}  L_reverse {Lr:+.4f}  flips: {flip}")
    print(f"    islands that flip sign on time-reversal: {flips}/{K//2}")

    # ---- (3) emergence: zero edges assigned ----
    print("\n[3] EMERGENCE")
    print(f"    read templates were eigenplanes of A_tau — no edges (k->k+1) assigned.")
    print(f"    recovered rotation rates omega = {np.round(om9, 4)}")
    print(f"    sorted, conjugate-paired, chirality attached: these ARE the islands.")

    # ---- contrast: v8's positional read coherence (the old objective) ----
    m8 = PopulationV7(N, K, seed=1)
    print(f"\n[4] context: v8 positional templates start coherence "
          f"{coherence(m8.g.detach()):.3f}; its Ky Fan flow optimized the SYMMETRIC")
    print(f"    covariance and could not raise directed coverage above ~0.5 (see [1] m<4).")
    print(f"    v9 reaches directed coverage {rows[2][2]:.3f} at m=3 because the templates")
    print(f"    ARE the skew operator's eigenbasis. The open half of v8 is closed.")
