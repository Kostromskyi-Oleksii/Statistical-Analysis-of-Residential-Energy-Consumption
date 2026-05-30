# Statistical Analysis of Residential Energy Consumption

## Overview
This project presents a statistical and physics-based model of residential electrical energy consumption in a typical apartment.  
The main purpose is to evaluate daily and long-term load behavior, peak power demand, and the probability of exceeding the circuit breaker rating.

The project is designed as a pre-university level Electrical Engineering study, focusing on energy systems analysis rather than software development.

## Goal and Objectives

**Goal**:  
Model household electricity consumption with realistic daily variability and assess the risk of tripping the main 3500 W circuit breaker.

**Objectives**:
- Build a base hourly load profile from typical household appliances
- Simulate daily consumption variations using Monte Carlo method
- Calculate key metrics: daily energy, peak power, overload probability
- Visualize results and provide practical recommendations for peak reduction

## Key Formulas

- Hourly power at hour h:  
  Pₕ = P_lighting(h) + P_fridge + P_washing(h) + P_computer(h)

- Daily variation:  
  Pₕ,day = Pₕ × v,    where v ∼ 𝒩(1.0, 0.15)

- Daily energy consumption:  
  E_day = (∑₂₄ Pₕ,day) / 1000     [kWh]

- Daily peak power:  
  P_peak = max(Pₕ,day)

- Overload condition: P_peak > 3500 W

- Overload probability = (number of overload days / 60) × 100%

## Appliances Model

| Appliance            | Power (W)       | Schedule                                  |
|----------------------|-----------------|-------------------------------------------|
| Lighting             | 10 / 50         | 50 W from 18:00 to 23:00, otherwise 10 W  |
| Refrigerator         | 150             | 24/7                                      |
| Washing machine      | 2000            | only at 19:00 (1 hour)                    |
| Personal computer    | 300             | 16:00 - 22:00                             |

Network voltage — 230 V  
Main breaker rating — 3500 W

## Project Structure

- `config.py`          — constants and system parameters  
- `load_model.py`      — base load profile generation  
- `simulation.py`      — Monte Carlo simulation (60 days)  
- `analysis.py`        — statistical calculations  
- `visualization.py`   — plotting routines  
- `main.py`            — main entry point

## How to Run

```bash
pip install numpy matplotlib
python main.py
```
The program displays:

Base daily load profile (hourly)
Histogram of daily energy consumption
Daily peak power time series (with 3500 W limit line)

Example Results (seed=42)
Deterministic base profile

Daily energy: 8.18 kWh
Peak power: 2500 W (at 19:00)

After 60 days with ±15% variation

Mean daily energy:      7.99 kWh
Min / Max energy:       5.78 - 10.45 kWh
Mean daily peak:        2442 W
Maximum observed peak:  3194.6 W
Overload days (>3500 W): 0
Overload probability:   0.0 %

## Conclusions

Under current assumptions the household has a significant safety margin — overload probability is practically zero.
The main evening peak (19:00) is caused by simultaneous operation of washing machine, computer, evening lighting and fridge.
±15% daily variation strongly affects total energy use, but barely influences overload risk due to low base peak (2500 W).
To make overloads more probable in the model one could: increase variation (σ=0.25-0.35), add high-power short-duration loads (kettle, oven, hairdryer), or reduce breaker limit to 3000-3200 W.

## Practical recommendations:

Move washing machine cycle to night hours (02:00-05:00)
Replace incandescent/halogen bulbs with LED lighting
Use smart plugs / timers to shift high-power loads away from evening peak
Consider demand-side management when adding new high-power appliances (EV charger, heat pump, etc.)

## Limitations

Hourly resolution (real spikes are much shorter)
Uniform variation coefficient applied to all loads
No seasonal / weather-dependent loads (air conditioning, electric heating)
No reactive power or power factor considered

## References

- Swan LG, Ugursal VI. Modeling of end-use energy consumption in the residential sector: A review of modeling techniques. Renewable and Sustainable Energy Reviews, 2009.
- Grandjean A, et al. A review of domestic hot water consumption and its modeling. Energy and Buildings, 2016.
- Gouveia JP, et al. Daily electricity consumption profiles for Portuguese households. Energy and Buildings, 2017.
- Yohanis YG. Domestic seasonal variations of electricity consumption. Energy and Buildings, 2010.
- Filippín C, et al. Household electricity consumption in Argentina. Energy for Sustainable Development, 2012.