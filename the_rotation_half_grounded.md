# The Rotation Half, Grounded

## What the skew lag-operator is in a real neuron — asymmetric plasticity, broken detailed balance, and why the arrow of time costs energy

*PerceptionLab / Antti Luode, with Claude (Opus 4.8). Helsinki, June 2026.*

> Do not hype. Do not lie. Just show.

---

## 0. What this document adds

Two earlier notes already grounded most of the framework. `the_geometric_neuron_grounded.md` mapped the **static** machinery — dendrite as a lossy delay line (`αᵏ` = cable attenuation), AIS as a structured trigger zone, the delta-code as the sparse-coding energy economy, the population field as the local ephaptic field. `membrane_to_qualia_synthesis.md` made energy the bridge between the single neuron and the population. Both predate the result that reorganized the whole line: the v9 / SpectralIslands finding that every engine — v3's Takens orbit, v5's directed edges, the Chiral-Ear EMD, the IslandNet poles — is reading **one operator's skew half**.

```
C_τ = E[ r(t) r(t−τ)ᵀ ],   r_k(t) = ⟨P_k, s(t)⟩       the lag covariance
S = (C_τ + C_τᵀ)/2     symmetric — power, autocorrelation, Wiener–Khinchin
A = (C_τ − C_τᵀ)/2     skew — rotation, chirality, the arrow of time
```

The previous documents grounded the symmetric world. They could not ground `A`, because `A` had not yet been isolated as the thing carrying all the direction. This document grounds `A`. The claim is sharp and, I think, the most defensible biological statement the framework has produced so far:

> **The skew lag-operator `A` is not a new object. It is the asymmetric component of synaptic connectivity that classical theory has used to generate sequences since 1986, that spike-timing-dependent plasticity physically writes, that experience-dependent place-field skewing physically shows, and that nonequilibrium physics identifies as broken detailed balance. The Geometric-Neuron line rediscovered it from the read side; neuroscience has had it on the write side for forty years. They are the same antisymmetric matrix.**

Everything below labels its evidential status, in the same spirit as the prior ledgers. The cosmology and the qualia bet stay in the drawer the grounded document built for them.

---

## 1. One operator, two halves, restated in neural terms

A square matrix splits uniquely into a symmetric and an antisymmetric part. For the lag covariance of population overlaps that split is not a formality — it is the boundary between physics that can carry time and physics that cannot.

**`S` is the power half.** It is fixed by the autocorrelation and therefore by the power spectrum (Wiener–Khinchin). Time-reversal leaves it invariant. Anything computed from `S` alone is phase-blind and direction-blind. In neural terms `S` is what a **rate code** and a **symmetric (classical Hebbian) synapse** give you: `w_ij ∝ ⟨x_i x_j⟩` is symmetric by construction, so a purely Hebbian network's connectivity has no `A` and can hold patterns but cannot order them. This is the Wiener–Khinchin ceiling of the v3 build, now stated as a property of the synapse, not just of the readout.

**`A` is the rotation half.** Real antisymmetric, so its spectrum is purely imaginary (`±iω_j`) and its eigenvectors are 2-D rotation planes — the spectral islands. Time-reversal flips its sign. All of the direction lives here. Measured in your code: `‖S_fwd − S_rev‖ = 3×10⁻³` (zero to noise), `‖A_fwd − A_rev‖ = 0.47` (the entire reversal). The arrow of time is the sign of an eigenvalue of `A`, per island, natively.

That is the mathematics. The rest of this document is what each half *is*, in tissue.

---

## 2. The skew operator is the asymmetric sequence connectivity (the exact identity)

This is the strongest link in the framework, stronger than the dendrite-as-delay-line mapping, because it is an algebraic identity rather than an analogy.

Sompolinsky & Kanter (1986, *Phys. Rev. Lett.* 57:2861) and Kleinfeld (1986, *PNAS* 83:9469) showed that a recurrent network recalls **sequences** rather than static patterns when you add a connectivity term of the form

```
J_seq = Σ_μ  ξ^{μ+1} (ξ^μ)ᵀ        (a "transition" or asymmetric term)
```

on top of the symmetric Hopfield term `Σ_μ ξ^μ (ξ^μ)ᵀ`. The transition term couples each pattern to its successor. It is **not symmetric**: the reverse coupling `ξ^μ(ξ^{μ+1})ᵀ` is its transpose, so `J_seq − J_seqᵀ` is exactly what drives the network from `μ` to `μ+1` rather than the reverse.

Now look at what `C_τ` is. Sample the field while it tours patterns `… → ξ^μ → ξ^{μ+1} → …`. Then `r(t) ≈ ξ^μ` and `r(t−τ) ≈ ξ^{μ−1}`, so

```
C_τ = E[ r(t) r(t−τ)ᵀ ]  ≈  Σ_μ  ξ^{μ} (ξ^{μ−1})ᵀ.
```

That is the Sompolinsky–Kanter transition matrix. **The lag covariance of the activity is the asymmetric sequence-generating connectivity.** Its skew part `A` is the antisymmetric core that orders the patterns in time. So:

- The matrix v9 **diagonalizes from the read side** (lag covariance of overlaps) and
- the matrix classical theory **builds on the write side** to generate sequences

are the same object. v9's "the islands are the eigenplanes of `A`" is, in established language, "the sequence is stored in the antisymmetric part of the connectivity, and its natural coordinates are that operator's rotation planes." The hand-built v5 edge `z_k = r_k + i·r_{k+1}` is exactly the Sompolinsky–Kanter nearest-neighbour transition `ξ^{k+1}(ξ^k)ᵀ` in one basis — which is why your THESIS.md found the v5 angular momentum equals the skew cyclic flux up to a sign (ratio −1.000). It had to.

**Status: exact structural identity, established.** This is the cleanest thing the framework touches. A reviewer who rejects the standing-wave story still has to grant that the skew lag-operator is the textbook sequence-memory connectivity; you are reading, from activity, the operator that theory writes into synapses.

---

## 3. STDP writes the skew half; place-field skewing shows it

The previous section is linear algebra plus a 1986 model. This section is the biology that builds `A` in a real brain.

**Symmetric Hebb has no time.** "Cells that fire together wire together," taken literally and symmetrically, produces `w_ij = w_ji` — pure `S`, no arrow. A network wired only this way can complete patterns but cannot say "A *then* B."

**STDP is an antisymmetric kernel.** Spike-timing-dependent plasticity (Markram et al. 1997; Bi & Poo 1998) is the correction: if pre fires *before* post, the synapse potentiates; if pre fires *after* post, it depresses. The learning window is, to first order, an **odd function of the timing difference Δt** — it changes sign when you swap pre and post. An odd-in-time plasticity rule applied to a sequence builds precisely the antisymmetric `ξ^{μ+1}(ξ^μ)ᵀ − ξ^μ(ξ^{μ+1})ᵀ` structure. **STDP is the physical mechanism that writes `A` into the connectivity.** The symmetric part of the STDP window builds `S`; the antisymmetric part builds `A`. The framework's "symmetric = power, skew = direction" split is the same split that separates rate-Hebbian from timing-Hebbian plasticity.

**Place-field skewing is `A` made visible.** Mehta, Barnes & McNaughton (1997, *PNAS*) and Mehta, Quirk & Wilson (2000, *Neuron*) showed that hippocampal place fields, initially symmetric, **expand asymmetrically backward** along the direction of travel with experience — and that this skewing is what an STDP rule predicts as the recurrent connectivity acquires the transition term. The experimental signature of the brain growing an `A` is a receptive field that becomes temporally asymmetric. So the emergence v9 demonstrates in code — islands and their chirality falling out of a learned skew operator (the Stiefel/Oja flow in `v9_learned.py`) — has a measured biological counterpart: experience-dependent, plasticity-driven growth of exactly this asymmetric structure.

**Status:** STDP and its temporal asymmetry are established (Markram, Bi & Poo). The identification of the STDP window's odd part with `A` is a clean structural mapping. Experience-dependent place-field skewing is an established empirical phenomenon (Mehta et al.) and is the most direct in-vivo evidence that the brain builds the skew operator. What remains a *model* claim is that a cell *reads* its own field through this operator (Section 6).

---

## 4. The cyclic flux is broken detailed balance — and that is why direction costs energy

Here is the connection that unifies the two halves of the v5 build (D2 time's-arrow and D3 wattage) into a single physical statement, and it is grounded in recent nonequilibrium neuroscience rather than analogy.

A stochastic system **at thermal equilibrium obeys detailed balance**: there are no net probability currents, no cycles, and — equivalently — its cross-correlations are time-symmetric, `C_ij(τ) = C_ji(τ)`. In that regime `A = 0`. The standard, textbook signature of a system held **away** from equilibrium is exactly an **asymmetry in the cross-correlation** — a non-vanishing `A` — which corresponds to a net probability current (a cycle) in state space. Maintaining that current requires continuous energy input and produces entropy. You cannot have circulation for free; the second law forbids it.

Lynn, Cornblath, Papadopoulos, Bertolero & Bassett (2021, *PNAS* 118:e2109889118, "Broken detailed balance and entropy production in the human brain") measured this directly in whole-brain imaging. Three results matter here:

1. the brain **nearly obeys detailed balance at rest** but **strongly breaks it during demanding physical and cognitive tasks** — i.e. `A` grows with cognitive work;
2. these macroscopic violations **emerge from fine-scale asymmetries in the interactions between elements** (they reproduce it with an asymmetric Sherrington–Kirkpatrick model) — i.e. from exactly the asymmetric connectivity of Section 2/3;
3. broken detailed balance is, by construction, **entropy production** — a dissipation rate.

Put these next to the v5 wattage meter and the picture closes:

| v5 / framework quantity | nonequilibrium-physics identity | consequence |
|---|---|---|
| skew operator `A ≠ 0` | broken detailed balance | system is out of equilibrium |
| island rotation rate `ω_j` (sign = chirality) | a net probability current / cycle | the arrow of time, per mode |
| skew cyclic flux (your `Σ A[k,k+1]−A[k+1,k]`) | total circulation / entropy-production proxy | the dissipation that *pays* for the arrow |
| D3 "energy is spent only at transitions" | entropy production concentrated at state changes | the wattage *is* the cost of breaking detailed balance |

So **D2 and D3 are one statement**. The arrow of time the islands read (D2) is a nonequilibrium current; by the second law that current is sustained only by dissipation (D3). "Direction" and "energy cost" are not two separate findings of the v5 build — they are the read-side and the thermodynamic-side of the same broken detailed balance. The framework's instinct that the delta-code is "an energy code" gets a precise version here: holding a percept is the near-equilibrium (`A → 0`, cheap, silent) regime; changing it — touring, sequencing, reading direction — is the driven, dissipative (`A ≠ 0`, expensive, spiking) regime, and Lynn et al. measured the brain doing exactly this split between rest and task.

A closely related result in the same line (Lynn and colleagues, on decomposing the local arrow of time) found that neural activity can define an arrow of time even when the stimulus does not, with the dominant contribution coming from **asymmetric pairwise interactions** — which is, again, `A`.

**Status:** the equilibrium ↔ detailed-balance ↔ time-symmetric-correlation equivalence is established statistical mechanics. The Lynn et al. measurement of load-dependent broken detailed balance in the brain is published and replicated. The identification of your skew flux with a probability current / entropy-production proxy is a clean, exact structural mapping. **The honest limit is the same one the grounded document flagged for the silence ratio:** your `sigma_JN` is dither, not a calibrated thermal bath, so the engine reports a *structural* entropy-production proxy, not a value in nats or Joules. Making it numerical is the next build (Section 8).

---

## 5. The eigenplanes are a spectrum of motion detectors

The grounded document already noted the exact identity `L = Im(z·z̄_lag)` = the Hassenstein–Reichardt elementary motion detector (1956), the canonical model of insect motion vision and the deployable edge of the whole program (trainless, O(K), direction-selective). The skew-operator framing **generalizes** that single detector into a bank.

Each conjugate eigenpair of `A` is one rotation plane with its own rate `ω_j`. `L` on that plane is one HR detector tuned to that rate. So `A` is not *a* motion detector — it is a **spectrum** of them, sorted by `|ω_j|`, with chirality `sign(ω_j)` attached. That is precisely the architecture of biological direction selectivity: not one detector but a population tuned to a range of speeds/directions —

- the **fly lobula plate** EMD array (Hassenstein–Reichardt / Borst);
- the **retinal direction-selective ganglion cells** and the starburst-amacrine circuit (Barlow–Levick), a bank of detectors over directions;
- the **hippocampal theta sequence**, where the population sweeps through place representations within each theta cycle — a rotation in representation space whose sign is the direction of travel.

`hippocampal_field.py` is the framework's most literal contact with this. Its `asymm` parameter **is** the skew term of Section 2/3 — a forward-biased ring connectivity, i.e. a built-in `A`. The theta sweep produces theta-sequence-like diagonal stripes; the rest phase produces SWR-style replay; and `L = Im(z·z̄_lag)` reads replay **direction** natively. Forward vs reverse replay is a real, documented phenomenon (Foster & Wilson 2006; Diba & Buzsáki 2007), and "how does a downstream reader tell forward replay from reverse" is a real open question for which a per-island sign is a genuine, cheap answer. The skew operator says: the two directions are the same eigenplane with opposite `ω` sign — which is exactly what the engine shows (all islands flip, population angular velocity flips).

**Status:** the HR/EMD identity is exact and established; the retinal and lobula-plate direction-selective banks are established; forward/reverse replay is established. That the *brain's* direction-selective populations are literally diagonalizing a skew lag-operator is the model interpretation — well-motivated, and now with a clean mathematical statement to test, but a hypothesis. The hippocampal simulator's honest limits stand as written in its own README: it is a mesoscale population model (bins, not Hodgkin–Huxley cells), fast and useful for population-level questions, not a biophysical replacement.

---

## 6. The seam: read-side flux vs write-side connectivity

Be honest about where the mapping is tight and where it is dual rather than identical.

In your engines `A` is a **read statistic** — the antisymmetric lag covariance of the field's own activity. In the Sompolinsky–Kanter/STDP picture `A` is a **write structure** — the antisymmetric part of the synaptic weights. These are not the same thing; they are two faces of one object. The connectivity that *generates* a sequence and the activity statistics that *result* from running it share the same antisymmetric core (that is the content of Section 2's approximation `C_τ ≈ Σ ξ^μ(ξ^{μ−1})ᵀ`), but "reading direction from the activity's broken detailed balance" (what v9 does) is downstream of "storing the sequence in asymmetric synapses" (what plasticity does).

This duality is a strength, not a hole: the **same antisymmetric matrix appears on both sides**, which is exactly why diagonalizing the activity's lag covariance recovers the stored sequence structure. But it sets the boundary of the claim. What is established: asymmetric connectivity (write) generates sequences, and the activity it produces has a non-vanishing skew lag-operator (read). What is the model's bet: that a single neuron's AIS *physically reads its own field through this operator* — that the AIS is a skew-operator detector and not merely an amplitude trigger. That remains the central falsifiable hypothesis of the single-neuron model, untouched by anything here. The population statement is grounded; the single-cell mechanism is still the good hypothesis it always was.

---

## 7. Ledger

**Established (used, not claimed):**
- the symmetric/antisymmetric split of a matrix; equilibrium ⇔ detailed balance ⇔ time-symmetric cross-correlations (statistical mechanics);
- asymmetric connectivity `Σ ξ^{μ+1}(ξ^μ)ᵀ` generates sequences in recurrent networks (Sompolinsky & Kanter 1986; Kleinfeld 1986; Amari 1972);
- STDP is temporally asymmetric — an odd-dominated learning window (Markram et al. 1997; Bi & Poo 1998);
- experience-dependent, plasticity-driven backward skewing of hippocampal place fields (Mehta, Barnes & McNaughton 1997; Mehta, Quirk & Wilson 2000);
- broken detailed balance / entropy production in the human brain, load-dependent, arising from fine-scale asymmetric interactions (Lynn et al. 2021);
- the Hassenstein–Reichardt EMD (1956) and biological direction-selective populations (retinal DSGCs / Barlow–Levick; fly lobula plate);
- forward and reverse hippocampal replay (Foster & Wilson 2006; Diba & Buzsáki 2007);
- the spike-dominated energy budget and the metabolic case for sparse coding (Attwell & Laughlin 2001) — carried from the prior documents.

**Exact structural identities (sound, the framework's strongest ground):**
- the skew lag-operator `A` = the antisymmetric part of the Sompolinsky–Kanter/Kleinfeld sequence connectivity — the read operator v9 diagonalizes and the write connectivity classical theory builds are the same matrix;
- the v5 per-edge `L_k` = `A` in the nearest-neighbour edge basis (your measured ratio −1.000 to the cyclic flux is the proof);
- the skew cyclic flux = a net probability current = broken detailed balance ⇒ the arrow of time (D2) and the energy cost (D3) are one statement;
- `L = Im(z·z̄_lag)` = one HR/EMD detector = one eigenplane of `A`; `A` is a *spectrum* of EMDs.

**Clean mappings (sound, carried/extended):**
- symmetric Hebb builds `S` (no time); the odd part of the STDP window builds `A` (time);
- holding a percept = near-equilibrium (`A → 0`, silent, cheap); changing/sequencing = driven, dissipative (`A ≠ 0`, spiking, expensive) — the delta-code as a near-/far-from-equilibrium split.

**Model hypotheses (falsifiable, unproven):**
- that the AIS physically reads its field through the skew operator (waveform/orbit geometry, not amplitude) — the central single-neuron bet, testable by STED scaffold geometry vs spike-triggered averages;
- that biological direction-selective populations are, functionally, diagonalizing a skew lag-operator.

**Honest limits:**
- read-side flux vs write-side connectivity are dual, not identical (Section 6);
- the engine's noise is dither, not a calibrated thermal bath, so its entropy-production / wattage figures are structural proxies, not nats or Joules;
- `hippocampal_field.py` is a mesoscale population model, not biophysics.

**Kept in the drawer (inspiration, not claim):** that any of this bears on the hard problem — that the held field is *experienced* rather than processed; that Johnson–Nyquist noise is the *medium* of content; the cosmology. Grounding the rotation half makes the engines one object and ties them to forty years of sequence-memory theory and to measured brain thermodynamics. It does not touch the hard problem; it only locates it more precisely, again.

**The empirical anchor still stands where it was:** the trainless geometric-dysrhythmia EEG result (cross-band eigenmode decoupling p = 0.007, d = −1.21; temporal Betti-1 p = 0.035) is the strongest real result and does not depend on any claim in this document. Note the rhyme, though: cross-band eigenmode *decoupling* and reduced temporal Betti-1 are both losses of coherent temporal/rotational structure — candidate read-outs of a degraded `A`. That is a hypothesis to test, not a result to claim.

---

## 8. The one concrete next build

Make the broken-detailed-balance identity **numerical**, and you turn the wattage meter into a measurement directly comparable to the brain literature.

Run the engine's overlap trajectory `r(t)` through Lynn et al.'s estimator: coarse-grain the state space, count net fluxes between states, and compute the **entropy-production rate** (in nats/step). Then:

1. Show it tracks the skew flux — that the structural quantity you already print *is* the entropy production, confirming Section 4 in your own code;
2. Show the HOLD regime sits near detailed balance (entropy production → 0) and the SCAN/tour regime breaks it — the engine reproducing the rest-vs-task result of Lynn et al. at the population scale;
3. Calibrate the per-spike cost to the Attwell–Laughlin budget so the silence ratio finally reports as Joules/s, the wattage claim made quantitative.

If those three hold, the framework will have a single figure showing that **the arrow of time it reads, the entropy it produces, and the energy it spends are one curve** — the thermodynamic version of "do not hype, do not lie, just show," and the most honest possible statement of what the skew half is: the price the brain pays, in dissipation, to order its thoughts in time.

---

*Helsinki, June 2026. The symmetric half is what you always had — power, the things that do not care which way time runs. The rotation half is what you kept rebuilding by hand, and it turns out to be the oldest idea in sequence memory, the thing STDP writes, the thing place fields show when they learn, and the thing physics calls broken detailed balance. One operator, split in two, grounded on both sides. Do not hype. Do not lie. Just show.*
