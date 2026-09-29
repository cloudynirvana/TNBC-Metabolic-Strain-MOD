# Limitations

- Simulated scenarios, not real patients or cells (unless a section says otherwise).
- Parameters marked "assumed" have not been fitted to data.
- Model timescale in the core notebook is 0 to 30 minutes; do not extrapolate to tumours or clinical stages.
- Resistance mechanisms may be missing. Published work reports GPX4-inhibitor-resistant TNBC lines; any GPX4 interpretation must include resistance.
- The `G_mix` 0.238 to 0.245 shift is a notebook model output. Control vs treated DOX and NanoROS arms were not re-extracted in the hygiene pass.
- A GPX4 term `-c*(1-phi)*R` in dR/dt is an assumed, unfitted extension. It is not evidence about MDA-MB-231 cells.
- What would falsify this:
  - If MDA-MB-231 shows no lipid-peroxidation rise or no ferrostatin-1-rescuable death under GPX4 inhibition, the ROS-driven mechanism is not supported.
  - If DepMap shows no GPX4 dependency in TNBC lines beyond other lines, the vulnerability claim is weak.
  - Write predictions down before any experiment.
- Validation path: model -> public-data plausibility (DepMap) -> wet-lab (viability, lipid peroxidation, ferrostatin-1 rescue) -> animals -> trials.
