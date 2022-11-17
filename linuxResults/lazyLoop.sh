#!/bin/bash 

if [ $# != 1 ]; then
   #echo "Error: $0 <# Drones> <samples>"
   echo "Error: $0 <samples>"
   exit
fi

SAMPLES=$1
_drones=(1 3 5)

# Fixed wing info:
_speedF=(18 22 22 31)
_batteryF=(971 936 1250 3059)

# Multible rotor info:
_speedM=(8.9 8.9 8.9 5 3)
_batteryM=(93 497 373 43)

for j in 0 1 2
do

   for i in 0 1 2 3 
   do
      ./main.sh ${_drones[$j]} ${_batteryF[$i]} $SAMPLES ${_speedF[$i]}
   done

done

