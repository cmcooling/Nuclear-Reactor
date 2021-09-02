import numpy as np
from constant_reactivity import ConstantReactivity
from ramp_reactivity import RampReactivity
from problem_specification import ProblemSpecification

def get_value(split_lines, identifier, return_type):
    '''Attempts to find a single line which begins with the identifier and returns the following value. Lines with only one word will be ignored. If more than one line has this identifier the first value will be selected
    lines -- The lines of the input split into individual words ([[String]])
    identifier -- The identifier which is being searched for (String)
    return_type -- The type the returned value should have (Type)'''

    # Check each line
    for line in split_lines:
        # If the line isn't long enough, progress to the next
        if len(line) < 2:
            continue
        # If the line begins with the identifier, try to return the value as the specified type
        if line[0] == identifier:
            try:
                return  return_type(line[1])
            # If the value doesn't exist or can't be converted move to the next one
            except (ValueError, IndexError):
                continue
    else:
        raise (ValueError("The input did not contain a specification of the value '" + identifier + "'"))

def get_reactivity(split_lines, identifier):
    '''Attempts to find a single line which begins with the identifier which specifies a reactivity profile and the constructs that profile.
    lines -- The lines of the input split into individual words ([[String]])
    identifier -- The identifier which is being searched for (String)'''

    # Check each line
    for line in split_lines:
        # If the line isn't long enough, progress to the next
        if len(line) < 3:
            continue
        if line[0] == identifier:
            # If the line begins with the identifier, check what type of reactivity profile is being created and create it
            if line[1] == "constant":
                try:
                    return ConstantReactivity(float(line[2]))
                except (ValueError):
                    # If the value can't be converted then move on to the next line move on to the next line
                    continue
            elif line[1] == "ramp":
                try:
                    return RampReactivity(float(line[2]), float(line[3]), float(line[4]), float(line[5]))
                except (IndexError, ValueError):
                    # If the value doesn't exist on the line or can't be converted to a real move on to the next line
                    continue
    else:
        raise(ValueError("The input did not contain a specification for the reactivity."))

def read_input(file_path):
    '''Reads the an input file from a specified path, reads it, extracts the relevant values and populates an instance of ProblemSpecification
    file_path -- The relative file path to the input file (string)
    [return] -- The specification of the problem'''

    # This syntax causes the specified file to be open during the construct below
    # If there is an error the file will be closed
    # Will also the file when finishing the block
    with open(file_path) as f:
        lines = f.readlines()

    # Split each line into individual words
    split_lines = [line.split() for line in lines]

    # Find out how many delayed neutron precursor groups there are
    n_delayed = get_value(split_lines, "n_delayed", int)

    # Create the arrays to hold the values of beta and lambda fir the delayed neutron precursor groups
    betas = np.zeros([n_delayed])
    lambdas = np.zeros([n_delayed])

    for i_delayed in range(n_delayed):
        betas[i_delayed] = get_value(split_lines, "delayed_fraction_" + str(i_delayed + 1), float)
        lambdas[i_delayed] = get_value(split_lines, "delayed_decay_rate_" + str(i_delayed + 1), float)

    # Get various other values from the input file
    n_z = get_value(split_lines, "n_z", int)
    source = get_value(split_lines, "source", float)
    generation_time = get_value(split_lines, "generation_time", float)
    feedback_fuel = get_value(split_lines, "feedback_fuel", float)
    feedback_coolant = get_value(split_lines, "feedback_coolant", float)
    energy_fission = get_value(split_lines, "energy_fission", float)
    heat_capacity_fuel = get_value(split_lines, "heat_capacity_fuel", float)
    total_height = get_value(split_lines, "total_height", float)
    heat_transfer_coefficient = get_value(split_lines, "heat_transfer_coefficient", float)
    thermal_conductivity_fuel = get_value(split_lines, "thermal_conductivity_fuel", float)
    heat_capacity_coolant = get_value(split_lines, "heat_capacity_coolant", float)
    speed_coolant = get_value(split_lines, "speed_coolant", float)
    temperature_zero = get_value(split_lines, "temperature_zero", float)
    reactivity_driving = get_reactivity(split_lines, "reactivity")

    # Make and return the problem specification
    return ProblemSpecification(n_z, betas, reactivity_driving, generation_time, lambdas, source, feedback_fuel, temperature_zero, feedback_coolant, energy_fission, heat_capacity_fuel, total_height, heat_transfer_coefficient, thermal_conductivity_fuel, heat_capacity_coolant, speed_coolant)