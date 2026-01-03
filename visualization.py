import matplotlib.pyplot as plt
from config import MAX_ALLOWED_POWER

def plot_results(daily_energy, peak_power):
    plt.figure()
    plt.hist(daily_energy, bins=15)
    plt.title("Daily Energy Consumption Distribution")
    plt.xlabel("kWh")
    plt.grid()
    plt.show()

    plt.figure()
    plt.plot(peak_power)
    plt.axhline(MAX_ALLOWED_POWER, linestyle="--")
    plt.title("Peak Power per Day")
    plt.ylabel("W")
    plt.grid()
    plt.show()
