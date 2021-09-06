from state_variables import StateVariables
from state import State
import numpy as np

def derivative(state_array, time, problem_specification):
    '''This function takes the current state of the system and the current time of the system and calculates the current rate of change of the state variables of the system
    It takes the array providing the state variables and uses this to construct an instance of State to make it easier to interrogate the current state
    The rate of change is created in an instance of StateVariables from which an array containing the rates of change is extracted and returned
    state_array -- The current state of the system contained in a single array (np.array[float])
    time -- The current time of the state (s)(float)
    problem_specification -- The specification of the current physical system (ProblemSpecifcation)
    [return] -- The current rate of change of the different variables describing the state of the system (np.array[float])'''

    # Create the instance of State to hold the current state of the system
    state = State(problem_specification, time, state_array)

    # Create the instance of StateVariable to hold the current rate of change of the variables
    gradient = StateVariables(problem_specification, time)

    # Populate gradient using the equations which define how the system changes with time
    reactivity = state.driving_reactivity + state.fuel_reactivity + state.coolant_reactivity
    power = state.power

    # The rate of change of the number of neutrons
    gradient.n_neutron = problem_specification.beta * (reactivity- 1) * state.n_neutron / problem_specification.generation_time
    gradient.n_neutron += np.dot(problem_specification.lambdas, state.n_delayed)
    gradient.n_neutron += problem_specification.source

    # The rate of change of the number of delayed neutron precursors
    gradient.n_delayed = problem_specification.betas * reactivity * state.n_neutron / problem_specification.generation_time
    gradient.n_delayed -= problem_specification.lambdas * state.n_delayed

    # The rate of change of the fuel temperature
    gradient.t_fuel = state.power * problem_specification.power_profile / problem_specification.heat_capacity_per_discretisation_fuel
    gradient.t_fuel -= (state.t_fuel - state.t_coolant) * problem_specification.heat_transfer_coefficient / problem_specification.heat_capacity_per_discretisation_fuel
    try:
        # The thermal diffusion term may raise an error if there are 2 or fewer discretisations, so put it in a try block
        gradient.t_fuel[0] -= problem_specification.thermal_conductivity_fuel * (state.t_fuel[1] - state.t_fuel[0]) / (problem_specification.heat_capacity_per_discretisation_fuel * problem_specification.d_z ** 2)
        gradient.t_fuel[-1] -= problem_specification.thermal_conductivity_fuel * (state.t_fuel[-2] - state.t_fuel[-1]) / (problem_specification.heat_capacity_per_discretisation_fuel * problem_specification.d_z ** 2)
        gradient.t_fuel[1:-1] -= problem_specification.thermal_conductivity_fuel * (state.t_fuel[:-2] + state.t_fuel[2:] - 2 * state.t_fuel[1:-1]) / (problem_specification.heat_capacity_per_discretisation_fuel * problem_specification.d_z ** 2)
    except IndexError:
        pass

    # The rate of change of the coolant temperature
    gradient.t_coolant = (state.t_fuel - state.t_coolant) * problem_specification.heat_transfer_coefficient / problem_specification.heat_capacity_per_discretisation_coolant
    try:
        # The advection term may fail if there is 1 discretisation, so put it in a try block
        gradient.t_coolant[1:] -= problem_specification.speed_coolant * (state.t_coolant[1:] - state.t_coolant[:-1]) / problem_specification.d_z
    except IndexError:
        pass
    gradient.t_coolant[0] -= problem_specification.speed_coolant * (state.t_coolant[0] - problem_specification.temperature_zero) / problem_specification.d_z

    # Extract an array containing the gradient and return it
    return gradient.as_array