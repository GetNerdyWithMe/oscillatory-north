# Oscillatory North

Different systems keep doing the same thing.

Trees under wind loading, a person on a swing, and simple neural oscillator models all tend to settle into a small set of stable motions, even when many are possible. The details differ, but the structure repeats.

This repository is where that pattern was worked through using simple dynamical models.

---

## Repository Structure

- `src/` – shared computational core
- `math/` – governing equations and dimensional analysis
- `mechanics/` – swing dynamics and mode selection
- `ecology/` – tree sway models
- `neuroscience/` – coupled oscillator behavior
- `results/` – qualitative stability comparisons
- `framework/` – cross-domain synthesis
- `docs/` – project notes

**Entry point:** `math/canonical_oscillator.py`

---

## Notes

The models are simple by design.

They exist to make repeated structure visible, not to reproduce any
single system faithfully.

How the behavior is interpreted depends on the domain.

---

This repository stops where the structure becomes clear.
