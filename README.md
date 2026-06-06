# TNBC Metabolic Strain Model

An open-source computational model of metabolic strain in triple-negative breast cancer (TNBC).

## Overview

This project uses ODEs to simulate ATP and ROS dynamics in TNBC, testing a nanobiocomposite intervention in Google Colab. The current notebook-oriented result reports a `G_mix` shift from `0.238` to `0.245`.

## Files

- `tnbc_model.ipynb`: Annotated Colab notebook with simulation and plots.
- `tnbc_ode_bifurcation.ipynb`: Bifurcation analysis notebook.
- `stability_analysis.ipynb`: Stability analysis notebook.
- `growth_plot.png`: Tumor growth dynamics.
- `monte_carlo.png`: Monte Carlo output figure.
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
