import matplotlib.pyplot as plt
from config import MAX_ALLOWED_POWER
from load_model import generate_base_load

def plot_base_load():
    base_profile = generate_base_load()
    plt.figure(figsize=(10, 5))
    plt.plot(base_profile)
    plt.title("Baseline daily load profile")
    plt.xlabel("Hour of the day")
    plt.ylabel("Power, W")
    plt.grid(True)
    plt.show()

def plot_results(daily_energy, peak_power):
    plt.figure(figsize=(10, 5))
    plt.hist(daily_energy, bins=15, edgecolor='black')
    plt.title("Distribution of daily energy consumption")
    plt.xlabel("kWh")
    plt.ylabel("Number of days")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.plot(peak_power, marker='.', linestyle='-')
    plt.axhline(MAX_ALLOWED_POWER, color='red', linestyle="--", label="Limit: 3500 W")
    plt.title("Daily peak power")
    plt.xlabel("Day number")
    plt.ylabel("Power, W")
    plt.legend()
    plt.grid(True)
    plt.show()