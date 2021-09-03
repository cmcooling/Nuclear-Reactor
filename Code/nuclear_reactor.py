from input_reader import read_input
from state import State
import numpy as np
from future_states import calculate_future_states
import matplotlib.pyplot as plt
import os

# Read the input file to form a problem specification
problem_specification = read_input("inputs/sample_input1.txt")

# Set up the initial state
initial_state = State(problem_specification, 0)
initial_state.t_fuel = np.full(problem_specification.n_z, problem_specification.temperature_zero)
initial_state.t_coolant = np.full(problem_specification.n_z, problem_specification.temperature_zero)

# Find the other states of the system
output_states = calculate_future_states(initial_state, problem_specification)



# Make the output directory if it doesn't exist
output_directory = os.path.join("outputs", problem_specification.simulation_name)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Plot some outputs
power= np.array([state.power for state in output_states])
fig_power, ax_power = plt.subplots()
ax_power.plot(problem_specification.output_times, power)
ax_power.set_xlabel("Time(s)")
ax_power.set_ylabel("Power(W)")
fig_power.savefig(os.path.join(output_directory, "power.png"))

temperature_fuel = np.array([state.t_fuel_mean for state in output_states])
fig_temperature_fuel, ax_temperature_fuel = plt.subplots()
ax_temperature_fuel.plot(problem_specification.output_times, temperature_fuel)
ax_temperature_fuel.set_xlabel("Time(s)")
ax_temperature_fuel.set_ylabel("Mean Fuel Temperature (K)")
fig_temperature_fuel.savefig(os.path.join(output_directory, "temperature_fuel.png"))

temperature_coolant = np.array([state.t_coolant_mean for state in output_states])
fig_temperature_coolant, ax_temperature_coolant = plt.subplots()
ax_temperature_coolant.plot(problem_specification.output_times, temperature_coolant)
ax_temperature_coolant.set_xlabel("Time(s)")
ax_temperature_coolant.set_ylabel("Mean Coolant Temperature (K)")
fig_temperature_coolant.savefig(os.path.join(output_directory, "temperature_coolant.png"))
