import numpy as np

class State_Variables():
    '''This class stores the state variables of the system at a particular time, or the rate of change of the corresponding values
    The data is stored in a public variables
    Data may be converted to/from a single array where it is stored in the order "n_neutron - n_delayed - t_fuel - t_cool"'''
    def __init__(self, problem_specification, time=0, array=None):
        '''Constructs the state
        self - The instance of State being set up (State)
        problem_specification - The problem specification for this problem (ProblemSpecification)
        time - The time of the state or gradient being represented (s)(default 0s)(float)
        array - If present, defines the stored data. If not present, the data is all zeros (np.array[float])'''
        self._problem_specification = problem_specification

        self.time = time

        if array !=None:
            self.populate_from_array(array)
        else:
            self.n_neutron = 0
            self.n_delayed = np.zeros(problem_specification.n_delayed)
            self.t_fuel = np.zeros(problem_specification.n_z)
            self.t_cool = np.zeros(problem_specification.n_z)

    def populate_from_array(self, array):
        '''Populates the state from the provided array
        self -- The state being populated (StateVariables)
        array -- The array providing the values (np.array[float])'''

        self.n_neutron = array[0]
        self.n_delayed = array[1:self._problem_specification.n_delayed + 1]
        self.t_fuel = array[self._problem_specification.n_delayed + 1: self._problem_specification.n_delayed + self._problem_specification.n_z + 1]
        self.t_cool = array[self._problem_specification.n_delayed + self._problem_specification.n_z + 1: self._problem_specification.n_delayed + 2 * self._problem_specification.n_z + 1]

    @property
    def as_array(self):
        '''Creates an array representing the data
        self -- The state being represented (StateVariables)
        [return] -- The array ,containing the values (np.array[float])'''

        array = np.zeros(self._problem_specification.n_state_variables)

        array[0] = self.n_neutron
        array[1:self._problem_specification.n_delayed + 1] = self.n_delayed
        array[self._problem_specification.n_delayed + 1: self._problem_specification.n_delayed + self._problem_specification.n_z + 1] = self.t_fuel
        array[self._problem_specification.n_delayed + self._problem_specification.n_z + 1: self._problem_specification.n_delayed + 2 * self._problem_specification.n_z + 1] = self.t_cool

        return(array)

    def __str__(self):
        '''Returns a string describing the contents of the StateVariables instance
        self -- The instance of StateVariables to be represented as a string
        [return] -- The string representing the instance of StateVariables (str)'''

        # Construct the output string line by line
        string = "Time: {}s\n".format(self.time)
        string += "Number of neutrons: {}\n".format(self.n_neutron)
        string += "Number of pre-cursors: {}\n".format(self.n_delayed)
        string += "Fuel temperature: {}\n".format(self.t_fuel)
        string += "Coolant temperature: {}\n".format(self.t_cool)

        return(string)