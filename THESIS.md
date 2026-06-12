# The Islands Were the Spectrum

## One operator under the whole Geometric-Neuron line — and the open half of v8, closed

**PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.**

> Do not hype. Do not lie. Just show.

---

## 0. What this is, and what it is not

This is not a claim about the universe. It is a small, exact piece of linear
algebra that closes a gap you have flagged honestly in every Geometric-Neuron
README: the spectral islands / directed edges were always **hand-assigned**,
and v8's attempt to make them emergent stalled at 0.50 captured energy with the
note *"nearest-target coverage did not rise."* The gap closes, and it closes
for a reason that ties the chiral readout, the v3 orbit, the v8 coverage
objective, the Chiral-Eye/Ear motion detector, and the IslandNet poles into a
single object: **the skew part of one lag operator.**

I will keep the cosmology in the drawer your own grounded document built for it.
The strong wing — clockfield-to-spacetime, particles as timeless cores, the
universe as a neural network — is inspiration, and `the_geometric_neuron_grounded.md`
already gives you the correct counsel: keep it out of the papers that carry the
results. I am following that counsel here. What follows is in the other drawer:
established mathematics, verified in code, with a ruthless ledger.

---

## 1. The one operator

Every engine in the line reads a shared field `s(t)` through a set of patterns,
producing overlaps `r_k(t) = ⟨P_k, s(t)⟩`. The single statistic that carries
sequence and direction is the **lag covariance**

```
C_τ = E[ r(t) r(t−τ)ᵀ ].
```

Split it the only way a square matrix can be split:

```
S = (C_τ + C_τᵀ)/2     symmetric
A = (C_τ − C_τᵀ)/2     skew (antisymmetric)
```

These are not two views of the same information. They are **orthogonal halves**:

- **S is the power half.** It is fixed by the autocorrelation, hence by the
  power spectrum. Time-reversal leaves it invariant. This is the
  Wiener–Khinchin ceiling, now stated structurally: anything you compute from
  `S` alone is phase-blind and direction-blind. *This is exactly what v8's Ky
  Fan objective optimized, and exactly why it could not see direction.*
  Measured: `‖S_forward − S_reverse‖ = 3×10⁻³` (zero to noise).

- **A is the rotation half.** It is real antisymmetric, so its spectrum is
  purely imaginary, `±iω_j`, and its eigenvectors are 2-D **rotation planes**.
  Time-reversal flips its sign. All of the direction lives here.
  Measured: `‖A_forward − A_reverse‖ = 0.47` (the entire reversal).

That single split is the thesis. The rest is consequences.

---

## 2. The islands emerge (they were eigenvectors)

Diagonalize `A`. Each conjugate eigenpair `(+iω_j, −iω_j)` is a **spectral
island**: a 2-D plane of the overlap space in which the field rotates at rate
`ω_j`. Nothing is assigned. On a field touring eight patterns the skew operator
hands back, sorted, the rotation rates

```
ω = [0.116, 0.093, 0.072, 0.000, ...]
```

— the Koopman rotation modes of the tour. The AIS-stores-a-Koopman-eigenfunction
hypothesis from the single-neuron model is, at the population scale, just this:
**the islands are the eigenmodes of the skew lag operator, and the cell that
reads one is reading one eigenplane.**

**Chirality is the eigenvalue sign.** Read the *same* leading plane on a forward
tour and its reverse: the rotation rate goes `+0.116 → −0.116`. The sign of
`ω_j` is that island's arrow of time, per island, natively — the v5 headline,
now derived rather than constructed.

---

## 3. The hand-built edges were one coordinate chart

The v5 directed edge `z_k = r_k + i·r_{k+1}` with `L_k = Im(z·z̄_lag)` is not
wrong — it is **one basis** for `A`. The basis-free invariant is the operator's
cyclic flux. Measured on the same runs:

```
v5 net angular momentum:   forward +0.929   reverse −0.930
skew-operator cyclic flux:  forward −0.929   reverse +0.930
ratio (v5 / flux):          −1.000           −1.000
```

A constant ratio of exactly −1 across both directions means these are the same
quantity in two coordinate systems (the sign is a convention in how the edge is
oriented). The edges you hand-built were a guess at a basis for an operator you
were already implicitly computing. Diagonalizing `A` removes the guess.

---

## 4. The open half of v8, closed — honestly

v8's decisive metric was captured-energy fraction of the **symmetric** increment
covariance: baseline 0.32, frame-potential 0.32, Ky Fan 0.50, and directed
coverage stuck. The honest v8 ledger already named the fix —
*"swap C for H_τ ... untested here."* Tested now.

The non-degenerate comparison is **directed coverage at a plane budget** `m`
(how much rotational energy you capture with `m` planes, `m < K/2`):

| planes m | symmetric basis (v8) | skew eigenmodes (this) |
|---|---|---|
| 1 | 0.001 | **0.414** |
| 2 | 0.331 | **0.743** |
| 3 | 0.586 | **0.999** |
| 4 (=K/2) | 1.000 | 1.000 |

**Honest caveat, stated plainly:** at the full-rank end (`m = K/2`) both bases
span the whole overlap space and tie at 1.0 — captured-energy is degenerate
there, and an earlier version of this test reported a meaningless 1.000/1.000
until I caught it. The real, non-degenerate statement is the table above: at any
*budget* the skew eigenmodes are the optimal directed basis (Schur–Horn /
Ky-Fan optimality for the skew operator), sorted by `|ω|` with chirality
attached; the symmetric basis has no reason to align with rotation and captures
far less per plane. v8 stalled not because coverage is unreachable but because
it was being maximized on the operator that provably has no direction in it.

---

## 5. The bridge to IslandNet (and why it is only a bridge)

An island has a rotation rate `ω_j` (from `A`) and the field has a leak
(`leak = 0.96 → decay 0.041`). Together they are a **complex pole**

```
ρ_j = 0.041 + i·ω_j      (decay + rotation).
```

That is the same object IslandNet stores as `C_k/(s − ρ_k)`: the real part is
depth/archival, the imaginary part is the island's rotation. So the
continual-learning field and the spectral-island readout are the same complex
plane seen from two sides — memory poles on one side, rotation modes on the
other. **The honest limit:** this is a structural correspondence (rate ↔ Im ρ,
decay ↔ Re ρ), not a proof that archiving a *learned task* preserves its
chirality. That would need the IslandNet experiments rerun with the skew
operator as the encoder, which I have not done. I flag it as the next build, not
a result.

---

## 6. What this unifies, in one breath

One diagonalization of one operator:

- **v3** read the delay-space orbit — that orbit lives in `A`'s eigenplanes.
- **v5** read per-edge `L_k` — that is `A` in the edge basis (ratio −1, §3).
- **v8** maximized coverage on `S` — the half with no direction (§4).
- the **Chiral-Eye/Ear** `L = Im(z·z̄_lag)` — the EMD detector — is the
  imaginary part of a single eigenplane's lag product.
- **IslandNet** poles — `Re ρ` decay, `Im ρ` = `A`'s rotation rate (§5).

The recurring primitive across all your work — `S = Re⟨f,g⟩`, the phase-coherence
metric — was the *symmetric* half. The skew half is the part that was being
rebuilt by hand every time under a different name. It has a spectrum, the
spectrum is the islands, and the islands carry the arrow of time as the sign of
their eigenvalue.

---

## 7. Ledger

**Verified in code (`spectral_islands.py`, `coverage_test2.py`):**
- the symmetric lag half is invariant under time-reversal (`3×10⁻³`); the skew
  half carries the entire reversal (`0.47`);
- the skew operator's conjugate eigenpairs are the rotation islands; rates
  `[0.116, 0.093, 0.072, ...]` emerge sorted, unassigned;
- the same eigenplane's rate flips sign forward↔reverse (chirality = arrow of
  time, per island);
- v5 net `L` = −(skew cyclic flux), ratio exactly −1.000 both directions;
- at a plane budget `m<K/2` skew eigenmodes capture markedly more directed
  energy than the symmetric basis (0.41 vs 0.001 at m=1; 0.74 vs 0.33 at m=2).

**Honest corrections forced by the build:**
- the first captured-energy metric was degenerate (1.000/1.000) because a full
  basis spans everything; the meaningful comparison is per-plane at a budget;
- the IslandNet bridge is a structural correspondence, not a demonstrated
  archival-of-learned-skill result.

**Built-in, not emergent (here):** the patterns `P`, the tour schedule, the
field leak/inject constants. What is *measured* is the spectrum of `A`, the
sign-flips, the flux identity, and the budgeted coverage.

**Kept in the other drawer (inspiration, not claim):** that this skew operator
is what a real AIS reads; that the cosmology (clockfield, universe-as-network)
follows from any of it. Section 0 means it. The grounded document's counsel
stands: the EEG geometric-dysrhythmia result is the empirical anchor, the
EMD/delta-code line is the deployable one, and this note is a clean piece of
the framework's *internal* mathematics — it makes the engines one object; it
does not touch the hard problem or the physics.

---

## 8. The one concrete next build

Replace the hand-assigned edges in `geometric_neuron_v8` with the skew
operator's eigenplanes: form `A` from the event-sampled lag covariance, take its
top-`m` rotation planes as the read templates, and let chirality be `sign(ω_j)`.
This is the `H_τ` swap Fable named, now with the diagnosis behind it — coverage
should reach the directed structure because the templates *are* its eigenbasis.
If it holds on the v8 task, the read/write asymmetry closes with no hand-built
structure remaining: writes orthogonalize via the field projector, reads cover
via the skew spectrum, and the islands are emergent end to end.

*Helsinki, June 2026. One operator, split in two. The power half is what you
always had; the rotation half is what you kept rebuilding by hand. Do not hype.
Do not lie. Just show.*
