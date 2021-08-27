class ProblemSpecification:
    '''A description of the parameters of the problem to be solved'''
    # By setting a all variables in the constructor with the _ prefix to the variable names, it is indicated that these variables shouldn't be accessed from outside this file. They are accessed through the properties instead. This effectively makes instances of this class immutable as the internal variables should not be changed but may be retrieved.
    def __init__(self, betas, reactivity_driving, generation_time, lambdas, source, feedback_fuel, reference_temperature_fuel, feedback_coolant, reference_temperature_coolant, energy_fission, heat_capacity_fuel, total_height, heat_transfer_coefficient, thermal_conductivity_fuel, heat_capacity_coolant, speed_coolant, inlet_temperature_coolant):
        '''Constructs the data for the problem specification
        self -- The instance of ProblemSpecification being constructed (ProblemSpecification)
        betas -- The delayed neutron fractions of the delayed neutron precursor groups (np.array[float])
        reactivity_driving -- The driving reactivity ($ as a function of time in s)(ReactivityFunction)
        generation_time -- The generation time (s) (float)
        lambdas -- The decay rates of the delayed neutron precursor groups (1/s)(np.array[float])
        source -- The strength of the neutron source (1/s) (float)
        feedback_fuel -- The reactivity feedback coefficient for the fuel ($/K)(float)
        reference_temperature_fuel -- The reference temperature for the fuel (K)(float)
        feedback_coolant -- The feedback coefficient for the coolant temperature ($/K)(float)
        reference_temperature_coolant -- The reference temperature for the coolant (K)(float)
        energy_fission -- The energy released by a fission (J)
        heat_capacity_fuel -- The absolute heat capacity of the fuel (J/K)(float)
        total_height -- The total height of the simulated domain (m)(float)
        heat_transfer_coefficient -- The linear heat transfer coefficient between the fuel and the coolant (W/K/m)(float)
        thermal_conductivity_fuel -- A constant related to the thermal conductivity of the fuel (m^2/s)(float)
        heat_capacity_coolant -- The absolute heat capacity of the coolant (W/K)(float)
        speed_coolant -- The speed of the coolant (m/s)(float)
        inlet_temperature_coolant -- The temperature of the coolant at the inlet
        '''

        # Set various values in the problem specification and calculate other values that are based on them
        self._betas = betas
        self._beta = sum(betas)
        self._reactivity_driving = reactivity_driving
        self._generation_time = generation_time
        self._lambdas = lambdas
        self._source = source
        self._feedback_fuel = feedback_fuel
        self._reference_temperature_fuel = reference_temperature_fuel
        self._feedback_coolant = feedback_coolant
        self._reference_temperature_coolant = reference_temperature_coolant
        self._energy_fission = energy_fission
        self._heat_capacity_fuel = heat_capacity_fuel
        self._total_height = total_height
        self._heat_transfer_coefficient = heat_transfer_coefficient
        self._thermal_conductivity_fuel = thermal_conductivity_fuel
        self._heat_capacity_coolant = heat_capacity_coolant
        self._speed_coolant = speed_coolant
        self._inlet_temperature_coolant = inlet_temperature_coolant

    @property
    def betas(self):
        ''' Returns the delayed neutron precursor fractions for each delayed neutron precursor group
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The delayed neutron precursor fractions for each delayed neutron precursor group (np.array[float])'''
        return(self._betas)

    @property
    def beta(self):
        ''' Returns the total delayed neutron precursor fraction
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The total delayed neutron precursor fraction (float)'''
        return(self._betas)

    def reactivity_driving(self, time):
        ''' Evaluates the driving reactivity at the specified time
        self -- The problem specification the value is being returned from (ProblemSpecification)
        time -- The time the driving reactivity is to be returned at (s)(float)
        [return] -- The driving reactivity at the specified time ($)(float)'''
        return(self._reactivity_driving(time))

    @property
    def generation_time(self):
        ''' Returns the generation time
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The generation time (s)(float)'''
        return(self._generation_time)

    @property
    def lambdas(self):
        ''' Returns the decay rates for each delayed neutron precursor group
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The decay rates for each delayed neutron precursor group (np.array[float])'''
        return(self._lambdas)

    @property
    def source(self):
        ''' Returns the rate at which neutrons are added from the source
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The source strength (1/s)(float)'''
        return(self._betas)

    @property
    def feedback_fuel(self):
        ''' Returns the temperature feedback coefficient for the fuel temperature feedback
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The temperature feedback for the fuel ($/K)(float)'''
        return(self._feedback_fuel)

    @property
    def reference_temperature_fuel(self):
        ''' Returns the reference temperature for the fuel temperature feedback
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The reference temperature for the fuel temperature feedback ($/K)(float)'''
        return(self._reference_temperature_fuel)

    @property
    def feedback_coolant(self):
        ''' Returns the temperature feedback coefficient for the coolant temperature feedback
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The temperature feedback for the coolant ($/K)(float)'''
        return(self._feedback_coolant)

    @property
    def reference_temperature_coolant(self):
        ''' Returns the reference temperature for the coolant temperature feedback
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The reference temperature for the coolant temperature feedback ($/K)(float)'''
        return(self._reference_temperature_coolant)

    @property
    def energy_fission(self):
        ''' Returns the energy released by each fission
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The energy released by each fission (J)(float)'''
        return(self._energy_fission)

    @property
    def heat_capacity_fuel(self):
        ''' Returns the absolute heat capacity of the fuel
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The absolute heat capacity of the fuel (J/K)(float)'''
        return(self._heat_capacity_fuel)

    @property
    def total_height(self):
        ''' Returns the total height of the simulated domain
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The total height of the simulated domain (m)(float)'''
        return(self._total_height)

    @property
    def heat_transfer_coefficient(self):
        ''' Returns the linear heat transfer coefficient between the fuel and the coolant
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The linear heat transfer coefficient between the fuel and the coolant (W/K/m)(float)'''
        return(self._heat_transfer_coefficient)

    @property
    def thermal_conductivity_fuel(self):
        ''' Returns the constant related to thermal conductivity of the fuel
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The constant related to the thermal conductivity of the fuel (m^2/s)(float)'''
        return(self._thermal_conductivity_fuel)

    @property
    def heat_capacity_coolant(self):
        ''' Returns the absolute heat capacity of the coolant
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The absolute heat capacity of the coolant(J/K)(float)'''
        return(self._heat_capacity_coolant)

    @property
    def speed_coolant(self):
        ''' Returns the speed of the coolant
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The speed of the coolant (m/s)(float)'''
        return(self._speed_coolant)

    @property
    def inlet_temperature_coolant(self):
        ''' Returns the inlet temperature of the coolant
        self -- The problem specification the value is being returned from (ProblemSpecification)
        [return] -- The inlet temperature of the coolant (K)(float)'''
        return(self._inlet_temperature_coolant)
        