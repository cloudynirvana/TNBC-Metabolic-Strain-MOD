# TNBC Metabolic Strain Model

> **Research only — not a medical device, not a treatment product, not a clinically validated biomarker.**
>
> This repository is an **in-silico / computational** dynamical-systems study of metabolic strain in triple-negative breast cancer (TNBC). Notebooks integrate ordinary differential equations (ODEs) for ATP, ROS, and glucose and explore bifurcation and stability. They do **not** diagnose, prognose, or treat patients, and they do **not** constitute FDA-cleared or otherwise validated clinical evidence. Expert review (cancer biology, TNBC metabolism, dynamical systems) is invited before any translational interpretation. See [`DISCLAIMER.md`](DISCLAIMER.md).

An open-source computational model of metabolic strain in TNBC.

## Overview

This project uses ODEs to simulate ATP and ROS dynamics in a stylized TNBC metabolic regime and to compare a **simulated** nanobiocomposite parameter set against an untreated control in Google Colab. Those “treated” vs “control” arms are **model inputs**, not patient cohorts.

The current notebook-oriented **in-silico** result reports a `G_tip` (also previously written `G_mix` in this README) shift from `0.238` to `0.245` under the default parameter pair. That number is a computational output of the ODE system, not a clinical endpoint.

## In-silico results (computational, not clinical)

No notebook in this repository loads patient records, trial outcomes, or a fitted clinical biomarker panel. Parameter values are illustrative / literature-inspired placeholders (including an MDA-MB-231-like metabolic regime), not a validated calibration to a clinical dataset.

| What you may see | How to read it |
| --- | --- |
| Control vs treated / nanobiocomposite | Two simulated parameter vectors, not a clinical trial arm |
| `G_tip` / ATP collapse threshold | A model-defined tipping point in the ODE state, not a diagnostic cutoff |
| Monte Carlo “validation” cells | Parameter-noise robustness of the **simulation**, not biomarker validation |
| Growth-rate plots | A derived proxy from modeled ATP, not measured tumor volume |

## Files

- `tnbc_model.ipynb`: Annotated Colab notebook with the core ATP/ROS simulation and plots.
- `tnbc_ode_bifurcation.ipynb`: Bifurcation and related in-silico sweeps.
- `stability_analysis.ipynb`: Local stability / Jacobian analysis of the ODE system.
- `growth_plot.png`: In-silico growth-rate proxy figure.
- `monte_carlo.png`: In-silico Monte Carlo robustness figure.
- `multi_birfucation.tnbc-ode.png`: Bifurcation diagram.
- `stability_analysis.png`: Stability output figure.

## Usage

1. Open `tnbc_model.ipynb` in Google Colab.
2. Run all cells to replicate the core ATP/ROS simulation.
3. Run the bifurcation and stability notebooks for dynamical-systems analysis.

## Citation and Attribution

This repository is MIT-licensed for open review and collaboration. If you use the code, notebooks, figures, or documentation, please cite the repository and credit Kelechi Ogbonna / cloudynirvana.

Expert review invited: cancer biology, TNBC metabolism, dynamical systems, bifurcation analysis, and research-software reviewers are encouraged to inspect the notebooks and challenge assumptions before any translational claims are made.

## License

MIT License. See `LICENSE`.
