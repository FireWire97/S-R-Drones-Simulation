#!/bin/bash 

# Just a little loop to run the program for multible different variables

if [ $# != 1 ]; then
   #echo "Error: $0 <# Drones> <samples>"
   #echo "Error: $0 <samples>"
   echo "Error: $0 <name of this simulation run>"
   exit
fi

NAME=$1
SAMPLES=25
#_drones=(1 3 5 10 25 50)
#_drones=(1 2 3 4 0 0)
_bSpeed="1.35"
_bBattery="9999"
#_drones=(1 5 10 15 20 25 30)
#_dronesF=(1 2 3 4 5 6 7 8 9 10)
_dronesF=(1 2 3 4)

# Baseline + Fixed wing info:
#_algorithm="snake"
#_speed=($_bSpeed 18 18 18)
#_battery=($_bBattery 320 100 200)
#_name=("Baseline" "Strix-400" "Albatross" "SkyEye")

# Multible rotor info:
_algorithm="pathfollow"
_speed=($_bSpeed 17 18)
_battery=($_bBattery 56 35)
_name=("Baseline" "Matrice300-RTK" "Matrice600-Pro")
_drones=(1 2 3 4)

_file="$NAME-histo.dat"
#j=1
#while [ -e $_fileF ]; do
#   _fileF=$(echo "$NAME-SNAKE-"$j".dat")
#   j=$(($j+1))
#done
#j=1
#while [ -e $_fileM ]; do
#   _fileM=$(echo "$NAME-PATH-"$j".dat")
#   j=$(($j+1))
#done

#echo "Drones  ${_name[0]} ${_name[1]} ${_name[2]} ${_name[3]}" > $_file
echo "Drones  ${_name[0]} ${_name[1]} ${_name[2]}" > $_file

   # how many drones do we want to test out
for j in {0..3} 
#for i in 2
do
# how many types of drones to test out
   for i in {0..2}
   do
      time ./main.sh $NAME ${_name[$i]} ${_drones[$j]} ${_battery[$i]} $SAMPLES ${_speed[$i]} $_algorithm
      _avg[$i]=$(awk -F' ' 'END { print $6 }' $NAME/$NAME.dat)
   done
   echo "${_drones[$j]} ${_avg[0]} ${_avg[1]} ${_avg[2]} ${_avg[3]}" >> $_file
done

mv $_file $NAME/

#../plotter2.sh $NAME $hDataFile $_batteryRange $_speedOfDrone $_simulationSamples $_numberOfDrones $avg

