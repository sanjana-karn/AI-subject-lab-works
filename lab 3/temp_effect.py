import math
import random
import matplotlib.pyplot as plt

def probability_of_acceptance(delta_e, temperature):
    """
    Calculate the probability of accepting an inferior solution.
    :param delta_e: Difference in cost (positive for an inferior solution).
    :param temperature: Current temperature.
    :return: Probability of acceptance.
    """
    if delta_e < 0:
        return 1.0  # Always accept if the solution is better
    return math.exp(-delta_e / temperature)

def simulate_temperature_effect(delta_e, initial_temperature, cooling_rate, steps):
    """
    Simulate the effect of temperature on the acceptance probability.
    :param delta_e: Fixed difference in cost.
    :param initial_temperature: Starting temperature.
    :param cooling_rate: Rate at which the temperature decreases.
    :param steps: Number of steps for the simulation.
    :return: List of temperatures and corresponding probabilities.
    """
    temperature = initial_temperature
    probabilities = []
    temperatures = []

    for _ in range(steps):
        prob = probability_of_acceptance(delta_e, temperature)
        probabilities.append(prob)
        temperatures.append(temperature)
        temperature *= cooling_rate  # Decrease temperature

    return temperatures, probabilities

# Parameters for the simulation
delta_e = 5  # Fixed difference in cost
initial_temperature = 100
cooling_rate = 0.95
steps = 50

# Simulate the temperature effect
temperatures, probabilities = simulate_temperature_effect(delta_e, initial_temperature, cooling_rate, steps)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(temperatures, probabilities, marker='o', color='b')
plt.title("Effect of Temperature on Acceptance Probability")
plt.xlabel("Temperature")
plt.ylabel("Acceptance Probability")
plt.grid()
plt.show()
