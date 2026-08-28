"""Core TNBC metabolic ODE model.

Research code only: this model is a computational hypothesis-testing framework,
not a validated therapeutic model.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp

DEFAULT_CONTROL = {
    "k_glyc": 0.6,
    "u": 0.5,
    "s": 0.15,
    "g": 0.2,
    "h": 0.01,
    "r": 0.1,
    "i_glyc": 0.3,
    "d": 0.15,
    "Nano_DOX": 0.0,
    "Nano_ROS": 0.0,
}


def rhs(t: float, y: np.ndarray, p: dict[str, float]) -> np.ndarray:
    A, R_os, G_lc = y
    dA = p["k_glyc"] * G_lc - p["s"] * R_os * A + p["r"] * (p["Nano_DOX"] + p["Nano_ROS"]) * A
    dR = p["g"] * p["k_glyc"] * G_lc + p["h"] * R_os**2 - p["d"] * p["Nano_ROS"] * R_os
    dG = p["u"] - p["k_glyc"] * G_lc - p["i_glyc"] * p["Nano_DOX"]
    return np.asarray([dA, dR, dG], dtype=float)


def simulate(params: dict[str, float] | None = None, y0=(10.0, 1.0, 5.0), t_end=30.0, n_points=300):
    p = DEFAULT_CONTROL.copy()
    if params:
        p.update(params)
    t_eval = np.linspace(0.0, t_end, n_points)
    sol = solve_ivp(lambda t, y: rhs(t, y, p), (0.0, t_end), np.asarray(y0, dtype=float), t_eval=t_eval, method="LSODA")
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.t, sol.y.T


def summary(t: np.ndarray, y: np.ndarray, atp_threshold=2.0) -> dict[str, float]:
    A, R_os, G_lc = y.T
    below = np.flatnonzero(A < atp_threshold)
    return {
        "final_ATP": float(A[-1]),
        "final_ROS": float(R_os[-1]),
        "final_glucose": float(G_lc[-1]),
        "min_ATP": float(A.min()),
        "max_ROS": float(R_os.max()),
        "ATP_below_threshold": bool(below.size),
        "first_ATP_threshold_time": float(t[below[0]]) if below.size else float("nan"),
    }
