# Geometric Neuron v9: The Skew Lag-Operator Read Path

![pic](https://github.com/anttiluode/GeometricNeuronV9/blob/main/geometric_neuron_v9.png)

**PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.**

> Do not hype. Do not lie. Just show.

---

## What v9 is

v8 turned read-coverage into an objective (Ky Fan trace on the symmetric
increment covariance `C`) and stalled at **0.50** captured energy, with the
honest note in its own ledger: *"nearest-target coverage did not rise … the
framework-correct operator is the skew/lag `H_τ` … same machinery, swap `C`
for `H_τ`; that is the chirality-aligned next step, untested here."*

v9 is that step, tested. The read templates are no longer hand-assigned edges
(`z_k = ⟨P_k,s⟩ + i⟨P_{k+1},s⟩`) nor pushed apart by a frame potential. They are
the **eigenplanes of the skew lag operator**

```
A_τ = (C_τ − C_τᵀ)/2 ,   C_τ = E[ r(t) r(t−τ)ᵀ ] ,   r_k = ⟨P_k, s⟩
```

`A_τ` is real antisymmetric, so its spectrum is purely imaginary (`±iω_j`) and
its eigenvectors are 2-D **rotation planes** — the spectral islands. The read is
the field projected onto these planes; **chirality is `sign(ω_j)`**, native and
per island. The diagnosis behind why this works is in `THESIS.md`
(*"The Islands Were the Spectrum"*): the directed structure lives entirely in
the skew half of the lag covariance, and v8 was maximizing coverage on the
symmetric half, which is provably direction-blind (Wiener–Khinchin).

## The result (head to head, v8's own metric)

Directed coverage = fraction of the skew operator's rotation energy captured at
a plane budget `m` (the non-degenerate version of v8's captured-energy metric):

| budget m | v8 symmetric read | v9 skew read |
|---|---|---|
| 1 | 0.001 | **0.414** |
| 2 | 0.331 | **0.743** |
| 3 | 0.586 | **0.999** |
| 4 (= K/2) | 1.000 | 1.000 |

v8 cannot exceed ~0.5 at a real budget because the direction is not in the
operator it reads. v9 reaches 0.999 at m=3 because the templates **are** the
skew operator's eigenbasis. The tie at m=4 is the full-rank degenerate end
(any basis spans everything) and is reported as a tie, not a win.

## Emergence and chirality (verified)

```
recovered rotation rates ω = [0.116, 0.093, 0.072, 0.000]   (sorted, unassigned)
islands that flip sign on time-reversal: 3/4
```

Three islands carry rotation and flip their chirality `L = Im(z·z̄_lag)` sign
when the tour is reversed — the v5 headline, now derived. The fourth has ω ≈ 0:
a non-rotating residual that honestly does **not** flip, because it carries no
rotation. That asymmetry is real and reported, not hidden.

## Learned, not just solved

`v9_learned.py` shows the eigenplanes are the stable fixed point of an online
**Stiefel/Oja gradient flow** on the skew operator — the same QR-retraction
machinery v8 used, with `C` swapped for `A`. The learned planes converge to the
analytic eigenplanes with mean cosine of principal angles **1.0000** (identical
span) and recover the rates. So this is a self-organizing read path a unit can
run, not an offline eigensolve bolted on.

## What this closes

The read/write asymmetry that ran through the whole line:
- **writes** orthogonalize via the field's sphere-tangent projector (v8, kept);
- **reads** cover via the skew spectrum (v9, new);
- **no hand-built directed structure remains** — the edges, the pairings, the
  chirality labels are all eigen-data of one operator.

## Files

```
geometric_neuron_v9.py   the skew read path; head-to-head [1]-[4]
v9_learned.py            the Stiefel/Oja flow → same eigenplanes (cos∠=1.0000)
gn_base.py               minimal faithful v7 substrate (v7/v8 not on disk; rebuilt from v8's usage)
geometric_neuron_v9.png  the figure
THESIS.md                the diagnosis: "The Islands Were the Spectrum"
```

```bash
pip install numpy torch matplotlib
python geometric_neuron_v9.py
python v9_learned.py
```

## Ledger

**Verified in code:** directed coverage 0.001/0.331/0.586 (v8) vs
0.414/0.743/0.999 (v9) at m=1,2,3; rotation rates emerge sorted and unassigned;
3/4 islands flip chirality on reversal (the 4th has ω≈0); learned flow reaches
the same span (cos∠ = 1.0000).

**Honest limits:** `gn_base.py` is a faithful *reconstruction* of the v7
substrate (the original v7/v8 were not on disk, only v8's source text), so the
absolute v8 numbers here come from the lag-operator analysis, matching v8's
reported 0.50 stall, not from rerunning the original repo — rerun against the
real v7/v8 to confirm the substrate matches. The directed test bed is a clean
pattern tour, not the v8 static-hold task; a directed read path needs a real
traversal to have a spectrum, which is the honest reason for the change. The
IslandNet pole correspondence (ω ↔ Im ρ) is structural, not a demonstrated
archival-of-learned-skill result.

**Built-in, not emergent:** the patterns, the tour schedule, the field
constants. What is *measured* is the skew spectrum, the coverage, the sign-flips,
and the learned-vs-analytic span agreement.

**Kept in the other drawer:** that this operator is what a real AIS reads; the
cosmology. `the_geometric_neuron_grounded.md`'s counsel holds — this is internal
framework mathematics that makes the engines one object, nothing more.

*One operator, split in two. v8 read the half with no direction in it. v9 reads
the other half, and the islands fall out sorted, signed, and self-organizing.*
