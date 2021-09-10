# Nuclear Reactor Example Project

This example project involves simulating a nuclear reactor in a very simplified way.
The population of neutrons and dealyed neutron precursors, fuel temeprature and coolant temperature are simulated.
The reactor is modeled as a single discretised vertical channel.
The equation solved are outlined in the Equations notebook.
The code is written in Python and heavily uses Numpy and Scipy.

## Key Skills

The following key skills are used in this project:

* Python
* Reading from a file
* Numpy and Scipy
* Initial Value Problems
* Matplotlib

## Running the Code

This project is designed to be run in the terminal from the "code" directory. The main file to run is "nuclear_reactor.py". It should be run with an additional command line argument to specify the path to the input file to be used. For example, to use the supplied input file, you might use the command "python nuclear_reactor.py inputs/sample_input1.txt" on Linux or Mac or "python nuclear_reactor.py inputs\sample_input1.txt" on Windows. The output will go to the directory specified by the "simulation_name" line of the input file. For example, "sample_input1.txt" has the line "simulation_name sample1" and so the output will be sent to outputs/sample1.

## Project Overview

The following files are found in the project:

* inputs/sample1: A sample input file
* constant_reactivity: A description of a constant reactivity
* derivative: A function which defines the rate of change of the different variables which describe the state of the system as a function of the current state of the system
* future_states: A function which calculates and returns future states of the system based on an initial state of the system
* input_reader: Functions which reads and input file and constructs a specification of the problem
* nuclear_reactor: The main file which calls various other functions and plots the output of the simulation
* problem_specification: a class which contains a specification of the problem being solved
* ramp_reactivity: A description of a reactivity as a function of time which is initially stable, then changes linearly, then holds constant
* state_variables: A class which holds the main variables being solved for - the ones which are solved for using the main equations
* state: A class which inherits from StateVariables which also contains a variety of properties which calcualte useful values of the state of the system

## Points of Interest

* Both the ConstantReactivity and RampReactivity classes implement the "\_\_call\_\_" magic method, allowing instances of those classes to be called like a function.
* The ProblemSpecification class includes the member variable "\_reactivity_driving" which may be an instance of ConstantReactivity or RampReactivity. In this way, this variable and the code which uses it is polymorphic.
* ProblemSpecification is a class whose instances are designed to approximate immutability - the constructor creates variables which are intended to be treated as private (indicated by the preceding "\_") and are accessed by properties with no associated setters.
* StateVairables is a class designed to hold the variables which are directly solved for by the Orindary Differential Equation (ODE) solver. It contains methods to populate it from an array or to populate an array using its data. This allows it to be used to conveniently store data in the "derivative" function for the rate of change of the function by accessing variables like "gradient.t_fuel", rather than having to work out which element of the array to alter. Once the "gradient" variable has been populated, an array can be created to be returned and used by "odeint".
* State is a class which inherits from StateVariables and so also has this functionality, allowing data to be accessed from naturally-named variables like "state.n_neutron" in "derivative" once the "state" variable has been populated from the array passed in. It also contains a number of properties which calculate useful values of the current state.
* "get_reactivity" and "get_value" contain some moderately complex logic including loop control, error handling and have a "for" loop with an "else" statement which is executed if the loop is not ended by a "break" or "return" statement.
* "nuclear_reactor.py" uses "os.path.join" to form the path to the outputs - this gets the slashes the right way around in the path whichever Operating System is being used.
* "derivative.py" uses a lot of Numpy functions to remove the need for loops and improve the speed of the code.

## Exercises
* Create an input file by copying "sample_input1.txt". Modify some input values and observe the change on the output.
* Look at "input_reader.py" - change the reactivity profile to a constant value by modifying the input file.
* You might be interested in the total energy created by the system. In this case dE/dt = P where E is the energy released and P is the power where E(t=0) = 0. Modify state_variables.py and derivative.py to add in this new variable and solve this new equation?
* Add to "nuclea_reactor.py" to cause the reactivity as a function of time to be plotted. Extension: Produce a plot which has the different components of reactivity (driving, fuel temperature and coolant temeprature) as well as the total.
* Add to "nuclear_reactor.py" so a plot is created which shows the fuel and coolant temperature profiles (i.e. the temepratures as a function of z) at the end of the simulation.

## Citing this Project

This project is distributed under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode). As such, you may take inspiration from or it adapt it or aspects of it into non-commecial work as you wish. If you use a substantial portion of the content of this project (for example, to produce a research code), please reference this project in any journal papers, conference papers, ec to acknolwedge its use. A bibtex reference is provided below for convenience:

```bibtex
@misc{Cooling2021,
  author = {Cooling, Chris},
  title = {Nuclear-Reactor},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/coolernato/Nuclear-Reactor}},
  note = {Imperial College London Graduate School}
}
```
