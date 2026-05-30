import numpy as np
from config import SIMULATION_DAYS

def analyze(daily_energy, peak_power, overloads):
    return {
        "mean_energy": round(daily_energy.mean(), 2),
        "min_energy": round(daily_energy.min(), 2),
        "max_energy": round(daily_energy.max(), 2),
        "mean_peak": round(peak_power.mean()),
        "max_peak": round(peak_power.max(), 1),
        "overload_days": overloads,
        "overload_probability": round(overloads / SIMULATION_DAYS * 100, 1)
    }