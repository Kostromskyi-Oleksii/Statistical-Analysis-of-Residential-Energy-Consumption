import numpy as np
from config import SIMULATION_DAYS

def analyze(daily_energy, peak_power, overloads):
    return {
        "mean_energy": daily_energy.mean(),
        "max_energy": daily_energy.max(),
        "min_energy": daily_energy.min(),
        "overload_probability": overloads / SIMULATION_DAYS * 100
    }
