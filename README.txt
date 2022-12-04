%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Search and Rescue drones.   %%
%% DTU-02333                   %%
%% Group 19                    %%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
README file for using our programs.

Here we have our Main.py that is our
simulator to simulate different scenarios
for drone searching.

To use the direct simulation, please
use the terminal:

python3 Main.py <numberOfDrones> <batteryCapacity> <number of simulations> <snake/pathfollow> <show simulation: True/False>

For example:
python3 Main.py 1 100 1 snake True

This will show you what is going on with the simulation, that is if <show simulation> is set to True.
This will also output results in number of ticks/boxes.

LINUX
This is in folder <linuxResults>.
To get real results, Linux terminal is used (Bash script):
./main.sh <name of run> <name of drone> <# Drones> <Battery range km> <samples> <speed m/s> <snake or pathfollow> <show simulation: True/False>

For example:
./main.sh TestRun Drone3000 1 100 1 20 snake False
- it is suggested to turn off the show if running many simulations in one run.

This will output the average mintutes taken to find the lost person, as well as data files to help with plotting.
Some plots are made in folder <name of run>/png.

That should do it!


 
