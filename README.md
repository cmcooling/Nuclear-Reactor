# Nuclear Reactor Example Project

This example project involves simulating a nuclear reactor in a very simplified way.
The population of neutrons and dealyed neutron precursors, fuel temeprature and coolant temperature are simulated.
The reactor is modeled as a single discretised vertical channel.
The equation solved are outlined in the Equations Notebook.
The code is written in Python and heavily uses Numpy and Scipy.

## Key Skills

The following key skills are used in this project:

* Python
* Reading from a file
* Numpy and Scipy
* Initial Value Problems
* Matplotlib

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
