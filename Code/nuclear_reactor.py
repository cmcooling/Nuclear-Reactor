from input_reader import read_input
from state import State
import numpy as np

# Read the input file to form a problem specification
problem_specification = read_input("Inputs/sample_input1.txt")

# Create the output states of the system. Initially, this is an empty array
output_states = np.empty(len(problem_specification.output_times), dtype=object)

# Set up the initial state
output_states[0] = State(problem_specification, 0)
output_states[0].t_fuel = np.full(problem_specification.n_z, problem_specification.temperature_zero)
output_states[0].t_cool = np.full(problem_specification.n_z, problem_specification.temperature_zero)

