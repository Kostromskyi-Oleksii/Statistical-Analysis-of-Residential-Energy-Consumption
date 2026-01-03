from simulation import run_simulation
from analysis import analyze
from visualization import plot_results

daily_energy, peak_power, overloads = run_simulation()
results = analyze(daily_energy, peak_power, overloads)

for k, v in results.items():
    print(f"{k}: {v}")

plot_results(daily_energy, peak_power)
