"""
gn_base.py — minimal faithful reconstruction of the v7 population substrate.
Reconstructed from the v8 source's usage (PopulationV7, make_targets, make_drive,
coherence, coverage, frame_potential, increment_cov, ortho_rows, kyfan_trace).
This is the shared field engine the whole Geometric-Neuron line uses:
  units write patterns P_k into a norm-stabilized field s; they read it with
  templates g_k. v7/v8 read POSITIONALLY (drive_k = <g_k, s>). v9 will swap the
  read for the skew lag-operator eigenplanes.
"""
import numpy as np
import torch

torch.set_default_dtype(torch.float64)


def make_targets(N, K, seed=0):
    """K orthonormal patterns in R^N (rows)."""
    g = torch.tensor(np.linalg.qr(np.random.default_rng(seed).standard_normal((N, K)))[0])
    return g[:, :K].transpose(0, 1).contiguous()        # (K,N)


def make_drive(T, K, targets, dwell, iota, noise, rng):
    """A drive that tours the K patterns in order, dwell steps each.
    Returns (drive (T,N), tgt (T,N), active (T,) int)."""
    N = targets.shape[1]
    active = np.zeros(T, dtype=int)
    for t in range(T):
        active[t] = (t // dwell) % K
    tgt = targets[active]                                # (T,N)
    d = iota * tgt + noise * torch.tensor(rng.standard_normal((T, N)))
    return d, tgt, torch.tensor(active)


class PopulationV7(torch.nn.Module):
    """Shared norm-stabilized field with write patterns P and read templates g."""
    def __init__(self, N, K, seed=1, read="positional", frame=0.0):
        super().__init__()
        self.N, self.K, self.read = N, K, read
        rng = np.random.default_rng(seed)
        P0 = np.linalg.qr(rng.standard_normal((N, K)))[0][:, :K].T
        g0 = P0 + 0.1 * rng.standard_normal((K, N))
        self.P = torch.nn.Parameter(torch.tensor(P0))
        self.g = torch.nn.Parameter(torch.tensor(g0))
        self.leak = 0.90
        self.inject = 0.18

    def run(self, drive, eps=0.1):
        """Integrate the shared field; return the trajectory S (T,N)."""
        T = drive.shape[0]
        s = torch.zeros(self.N)
        S = []
        Pn = self.P / (self.P.norm(dim=1, keepdim=True) + 1e-9)
        for t in range(T):
            rd = self.g @ s                              # read overlaps (positional)
            act = torch.relu(rd)
            inj = act @ Pn                               # write back
            s = self.leak * s + self.inject * inj + eps * drive[t]
            s = s / (s.norm() + 1e-9)
            S.append(s)
        return torch.stack(S)                            # (T,N)


def coherence(g):
    gn = g / (g.norm(dim=1, keepdim=True) + 1e-9)
    G = gn @ gn.transpose(0, 1)
    K = g.shape[0]
    off = G - torch.eye(K)
    return float(off.abs().max())


def coverage(g, targets, thr=0.5):
    gn = g / (g.norm(dim=1, keepdim=True) + 1e-9)
    tn = targets / (targets.norm(dim=1, keepdim=True) + 1e-9)
    M = (gn @ tn.transpose(0, 1)).abs()
    return float((M.max(dim=1).values > thr).sum())


def frame_potential(g, K):
    gn = g / (g.norm(dim=1, keepdim=True) + 1e-9)
    G = gn @ gn.transpose(0, 1)
    return (G**2).sum() - torch.diagonal(G**2).sum()


def increment_cov(S, weight=True):
    ds = S[1:] - S[:-1]
    sp = S[:-1]
    proj = ds - (sp * ds).sum(1, keepdim=True) * sp
    w = proj.norm(dim=1, keepdim=True) if weight else torch.ones(proj.shape[0], 1)
    C = (proj * w).transpose(0, 1) @ proj / (w.sum() + 1e-9)
    return 0.5 * (C + C.transpose(0, 1))


if __name__ == "__main__":
    N, K = 24, 8
    tg = make_targets(N, K)
    m = PopulationV7(N, K, seed=1)
    rng = np.random.default_rng(2)
    d, tgt, act = make_drive(200, K, tg, 25, 0.2, 0.13, rng)
    S = m.run(d, eps=0.12)
    print("substrate OK — field run shape", tuple(S.shape),
          "| coverage", coverage(m.g.detach(), tg), "/", K,
          "| coherence", round(coherence(m.g.detach()), 3))
