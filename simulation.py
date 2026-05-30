import numpy as np
from config import *
from load_model import generate_base_load

def run_simulation():
    np.random.seed(42)
    base_profile = generate_base_load()

    daily_energy = []
    peak_power = []
    overloads = 0

    for _ in range(SIMULATION_DAYS):
        variation = np.random.normal(1.0, 0.15)
        day_profile = base_profile * variation

        daily_energy.append(day_profile.sum() / 1000)
        peak_power.append(day_profile.max())

        if day_profile.max() > MAX_ALLOWED_POWER:
            overloads += 1

    return np.array(daily_energy), np.array(peak_power), overloads