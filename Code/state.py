from state_variables import State_Variables
import numpy as np

class State(State_Variables):
    ''''Represents a state of the system at a given time
    The main state variables are handled in the StatVariables class definition
    Other useful values are accessible through properties'''
    
    @property
    def t_fuel_mean(self):
        '''Calculates the  mean temperature of the coolant
        self -- The instance of State the value is being calculated (State)
        [return] -- The mean fuel temperature (K)(float)'''
        return np.mean(self.t_fuel)

    @property
    def t_coolant_mean(self):
        '''Calculates the  mean temperature of the fuel
        self -- The instance of State the value is being calculated (State)
        [return] -- The mean coolant temperature (K)(float)'''

        return np.mean(self.t_coolant)

    @property
    def driving_reactivity(self):
        '''Calculates the current driving reactivity
        self -- The instance of State the value is being calculated (State)
        [return] -- The reactivity contribution from the driving reactivity ($)(float)'''

        return self._problem_specification.reactivity_driving(self.time)

    @property
    def fuel_reactivity(self):
        '''Calculates the current reactivity due to the temperature of the fuel
        self -- The instance of State the value is being calculated (State)
        [return] -- The reactivity contribution from the fuel temperature ($)(float)'''

        return self._problem_specification.feedback_fuel * (self.t_fuel_mean - self._problem_specification.temperature_zero)

    @property
    def coolant_reactivity(self):
        '''Calculates the current reactivity due to the temperature of the coolant
        self -- The instance of State the value is being calculated (State)
        [return] -- The reactivity contribution from the coolant temperature ($)(float)'''

        return self._problem_specification.feedback_coolant * (self.t_coolant_mean - self._problem_specification.temperature_zero)

    @property
    def power(self):
        '''Calculates the current power
        self -- The instance of State the value is being calculated (State)
        [return] -- The power of the state (W)(float)'''

        return self.n_neutron * self._problem_specification.energy_fission / self._problem_specification.generation_time