# Statistical Analysis of Residential Energy Consumption

## Overview
This project presents a statistical and physics-based model of residential electrical energy consumption.  
The goal is to analyze daily and long-term load behavior, peak power demand, and the probability of network overloads.

The project is designed as a pre-university Electrical Engineering study, focusing on energy systems analysis rather than software development.

## Motivation
Electrical power systems must be designed not only for average consumption, but also for peak loads and variability in user behavior.  
This project investigates how stochastic variations in daily usage affect:
- total energy consumption
- peak power demand
- reliability of household electrical infrastructure

Such analysis is essential for power system planning, circuit protection selection, and energy efficiency optimization.

## Model Description
The model simulates a typical residential household with the following electrical appliances:

| Appliance            | Power (W) | Usage Schedule                          |
|----------------------|-----------|-----------------------------------------|
| Lighting             | 10 (day)<br>50 (evening) | 50 W from 18:00 to 23:00<br>10 W otherwise |
| Refrigerator         | 150       | Constant operation (24/7)                |
| Washing Machine      | 2000      | Operates only at 19:00 (1 hour)          |
| Personal Computer    | 300       | Operates from 16:00 to 22:00             |

A base hourly load profile (24 values in Watts) is created using realistic power ratings and usage schedules.  
Daily variability is modeled via Monte Carlo simulation with multiplicative random variation ~ N(1.0, σ=0.15), representing ±15% fluctuations in overall consumption.

Key electrical relations used:  
- Power: P = U × I (voltage assumed constant at 230 V)  
- Energy: E = ∑(P × Δt) where Δt = 1 hour (energy in kWh = sum(P)/1000)

Maximum allowed power is set to **3500 W** (typical rating for a household circuit breaker in many apartments).

## Simulation Approach
- Time resolution: 1 hour  
- Simulation duration: 60 days  
- Random variation: normal distribution with mean 1.0 and standard deviation 0.15  
- Overload event: peak power in a day > 3500 W  

The simulation calculates:  
- Daily energy consumption (kWh)  
- Daily peak power (W)  
- Number of overload days

## Key Results
Base (deterministic) profile:  
- Daily energy consumption: **8.18 kWh**  
- Peak power: **2500 W** (at 19:00 due to simultaneous operation of washing machine, computer, lighting, and refrigerator)

With stochastic variation (example run with 60 days, reproducible seed):  
- Mean daily energy: **7.99 kWh**  
- Minimum daily energy: **5.78 kWh**  
- Maximum daily energy: **10.45 kWh**  
- Mean peak power: **2442 W**  
- Maximum observed peak power: **3194.6 W**  
- Probability of overload (>3500 W): **0.0%** (0 overload days)

**Note**: Results may vary slightly between runs due to randomness, but overload probability typically remains very low (<5%) because the base peak (2500 W) is well below the 3500 W limit, and even with +30% variation (rare) it stays under the threshold.

## Analysis and Conclusions
- The household has comfortable margin below the 3500 W limit under modeled conditions.  
- Peak demand occurs in the evening (19:00) due to coincidence of high-power appliances.  
- Stochastic variation significantly affects total energy consumption (range ~5.8–10.5 kWh) but has limited impact on overload risk in this scenario.  
- Recommendations:  
  - Shift washing machine to off-peak hours (e.g., nighttime) to further reduce peak.  
  - Replace lighting with LED (lower evening power) for energy savings.  
  - Add more variable loads (e.g., electric kettle, microwave) for more realistic overload risk assessment.

## Limitations
- Hourly resolution (real consumption has minute-level spikes).  
- Limited set of appliances (no seasonal loads like air conditioning or heating).  
- Variation applied uniformly to all loads (in reality, appliances vary independently).  
- No modeling of reactive power or power factor.

## Project Structure
- `config.py` - Physical parameters and system assumptions  
- `load_model.py` - Household load modeling  
- `simulation.py` - Monte Carlo simulation  
- `analysis.py` - Statistical analysis  
- `visualization.py` - Result visualization (histogram of daily energy + peak power over time)  
- `main.py` - Entry point

## How to Run
1. Install required libraries:
```bash
pip install numpy matplotlib
python main.py
```

The program will print statistical results to console and display two plots:

Histogram of daily energy consumption distribution
Daily peak power over the simulation period (with 3500 W limit line)

Feel free to modify parameters in config.py to explore different scenarios!
