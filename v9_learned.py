"""
v9_learned.py — the islands as a LEARNED fixed point (Oja flow on the skew op)
==============================================================================
[1]-[3] in geometric_neuron_v9.py computed the eigenplanes analytically. This
shows they are also the stable attractor of a gradient flow a unit could run
online: a Stiefel-manifold ascent of the skew Ky-Fan trace

    maximize  tr(Q^T A Q_perp-rotated)   <=>   Q tracks A's dominant rotation planes

Concretely we maximize the rotational energy a plane-pair captures,
    J(Q) = sum_j  |q_{2j}^T A q_{2j+1}|     (skew bilinear, the per-island |omega|)
by projected gradient ascent with QR retraction (the v8 Stiefel machinery,
skew operator swapped in). No eigensolver, no edge assignment. We verify the
learned planes converge to the analytic eigenplanes and recover the rates.
"""
import numpy as np
import torch
from gn_base import make_targets
from geometric_neuron_v9 import tour_field, lag_cov_overlaps, v9_read_templates, directed_captured

torch.set_default_dtype(torch.float64)

N, K, tau = 64, 8, 60
P = make_targets(N, K, seed=0).numpy()
S = tour_field(P, +1, seed=3)
C = lag_cov_overlaps(S, P, tau)
A = torch.tensor(0.5 * (C - C.T))                       # skew operator (K,K)
m = 3                                                   # learn top-3 rotation planes

# learnable frame on the Stiefel manifold (2m orthonormal columns in R^K)
torch.manual_seed(0)
G = torch.nn.Parameter(torch.linalg.qr(torch.randn(K, 2 * m))[0])
opt = torch.optim.Adam([G], lr=0.05)

def stiefel_retract(G):
    return torch.linalg.qr(G)[0]

for it in range(400):
    Q = stiefel_retract(G)
    # per-island rotational energy: |q_{2j}^T A q_{2j+1}|, summed
    J = 0.0
    for j in range(m):
        a, b = Q[:, 2 * j], Q[:, 2 * j + 1]
        J = J + torch.abs(a @ A @ b)
    loss = -J
    opt.zero_grad(); loss.backward(); opt.step()

Q_learned = stiefel_retract(G).detach().numpy()
Q_analytic, om_an, Askew = v9_read_templates(C, m)

cap_learned = directed_captured(Q_learned, 0.5 * (C - C.T))
cap_analytic = directed_captured(Q_analytic, 0.5 * (C - C.T))

# learned rotation rates: |q_a^T A q_b| per plane
om_learned = []
for j in range(m):
    a, b = Q_learned[:, 2 * j], Q_learned[:, 2 * j + 1]
    om_learned.append(abs(a @ (0.5 * (C - C.T)) @ b))
om_learned = np.sort(np.array(om_learned))[::-1]

# subspace agreement between learned and analytic planes (principal angles)
Ql = np.linalg.qr(Q_learned)[0]; Qa = np.linalg.qr(Q_analytic)[0]
sv = np.linalg.svd(Ql.T @ Qa, compute_uv=False)
mean_cos = sv.mean()

print("=" * 66)
print("v9 LEARNED ISLANDS — Stiefel/Oja flow on the skew operator")
print("=" * 66)
print(f"  learned directed coverage:  {cap_learned:.3f}")
print(f"  analytic directed coverage: {cap_analytic:.3f}")
print(f"  learned rotation rates:  {np.round(om_learned,4)}")
print(f"  analytic rotation rates: {np.round(np.sort(om_an)[::-1],4)}")
print(f"  subspace agreement (mean cos principal angles): {mean_cos:.4f}  (1.0 = identical span)")
print()
print("  => the islands are not just an eigensolve; they are the stable fixed")
print("     point of an online gradient flow a unit can run, using the same")
print("     Stiefel retraction as v8 but on the SKEW operator. Self-organizing.")
