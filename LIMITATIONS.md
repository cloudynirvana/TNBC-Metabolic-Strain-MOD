# Limitations

- Simulated scenarios, not real patients or cells (unless a section says otherwise).
- Parameters marked "assumed" have not been fitted to data.
- Model timescale in the core notebook is 0 to 30 minutes; do not extrapolate to tumours or clinical stages.
- Resistance mechanisms may be missing.
- The `G_mix` 0.238 to 0.245 shift is a notebook model output. Control vs treated DOX and NanoROS arms were not re-extracted in this hygiene pass.
- What would falsify this: if the notebook, with the same equations and parameters, does not reproduce the reported `G_mix` shift.
- Validation path: model -> public-data plausibility -> wet-lab -> animals -> trials.
