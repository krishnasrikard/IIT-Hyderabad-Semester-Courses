## Procedure for Running Spice Simulations
### Steps:
1. Go to folder named 'spice'. Run the following commands to create .dat files containing the output of two .net files.
```
ngspice ee18btech11014_1.net
ngspice ee18btech11014_2.net
```
2. Use the python code 'EE18BTECH11014_Simulation-1.py' to plot the responses/outputs from two .dat files.

### Description
1. ee18btech11014_1.net contains a Closed-Loop Feedback Circuit with Phase-Margin = 90 degrees. Here the input to the circuit is a **Step Signal**.
2. ee18btech11014_2.net contains a Closed-Loop Feedback Circuit with Phase-Margin = 90 degrees. Here the input to the circuit is a **Sinusoidal Signal**.
