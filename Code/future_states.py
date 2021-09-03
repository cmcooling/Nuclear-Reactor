from scipy.integrate import odeint
from state import State
from derivative import derivative
import numpy as np

def calculate_future_states(start_state, problem_specification):
    '''Calculates the state at a series of times from the state at the initial time by using the equations of the system
    start_state -- The state at the start of the period being simulated (State)
    end_time -- The time at the end of the simulated period (s)(float)
    [return] -- The states at the specified times (np.array[State])'''

    start_array = start_state.as_array

    calculated_arrays = odeint(derivative, start_array, problem_specification.output_times, args=(problem_specification,))

    calculated_states = np.array([State(problem_specification, time, array) for array, time in zip(calculated_arrays, problem_specification.output_times)])

    return calculated_states

    