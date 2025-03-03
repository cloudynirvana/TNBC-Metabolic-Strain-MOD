# # TNBC Metabolic Strain Model
An open-source computational model of metabolic strain in triple-negative breast cancer (TNBC).

## Overview
This project uses ODEs to simulate ATP and ROS dynamics in TNBC, testing a phytochemical-enhanced nanobiocomposite. Built in Google Colab, it shifts Gₜᵢₚ from 0.238 to 0.245.

## Model
- dA/dt = k_glyc * G_lc - s * R_os * A + r * (Nano_DOX + Nano_ROS) * A  
  (ATP dynamics)
- dR_os/dt = g * k_glyc * G_lc + h * R_os^2 - d * Nano_ROS * R_os  
  (ROS modulation)
- dG_lc/dt = u - k_glyc * G_lc - i_glyc * Nano_DOX  
  (Glucose consumption)
Key parameters: k_glyc = 0.6 mM/min, r = 0.14 (treated).

## Key Finding: Gₜᵢₚ Shift
Gₜᵢₚ (glucose at ATP < 2.0 mM) shifts from 0.238 (control) to 0.245 (treated), delaying collapse.

## Phytochemical Dynamics
The nanobiocomposite (Nano_DOX = 1, Nano_ROS = 2) reduces ROS by ~30%, enhancing therapeutic potential.

## Requirements
- Google Colab (or Python 3.x with NumPy, SciPy, Matplotlib)

## Files
- `tnbc_model.ipynb`: Colab notebook with simulation and plots.
- `figure1.png`: ATP/ROS trajectories.

## Usage
1. Open `tnbc_model.ipynb` in Google Colab.
2. Run all cells to generate results and `figure1.png`.

## License
MIT License—free to use, modify, and share.
