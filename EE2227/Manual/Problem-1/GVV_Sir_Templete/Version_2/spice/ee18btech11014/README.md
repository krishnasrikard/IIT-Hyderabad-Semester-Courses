## Procedure for Running Spice Simulations
### Steps:
1. Go to folder named 'spice'. Run the following command to create .dat file containing the output of .net file.
```
ngspice filename
```
2. Use the python codes to run .dat files
  - 'EE18BTECH11014_Simulation-1,2.py' to plot the responses/outputs from two ee18btech11014_1.dat and ee18btech11014_2.dat files.
  - 'EE18BTECH11014_Simulation-3.py' to plot the responses/outputs from ee18btech11014_3.dat file.
  - 'EE18BTECH11014_Simulation-a.py' to plot the responses/outputs from ee18btech11014_a.dat file.

### Description
1. ee18btech11014_1.net contains a Closed-Loop Feedback Circuit with Phase-Margin = 90 degrees. Here the input to the circuit is a **Unit-Step Signal**.
2. ee18btech11014_2.net contains a Closed-Loop Feedback Circuit with Phase-Margin = 90 degrees. Here the input to the circuit is a **Sinusoidal Signal**.
3. ee18btech11014_3.net contains a Closed-Loop Feedback Circuit of an Unstable. Here the input to the circuit is a **Unit-Step Signal**.
4. ee18btech11014_a.net contains a Closed-Loop Feedback Circuit with Phase-Margin = 72 degrees. Here the input to the circuit is a **DC Signal**.
