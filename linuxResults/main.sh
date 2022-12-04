#!/bin/bash

if [ $# != 8 ]; then
   echo "Error: $0 <name of run> <name of drone> <# Drones> <Battery cap> <samples> <speed> <snake or pathfollow> <show simulation: True/False>"
   exit
fi

_name=$1
_nameDrone=$2
_numberOfDrones=$3
_batteryRange=$4
_simulationSamples=$5
_speedOfDrone=$6
_algorithm=$7
_show=$8
_kmPerTick="0.257555542"
ALG1="snake"
ALG2="pathfollow"

#i=1
#while [ -d $_name ]; do
#   _name="$_name-$i"
#   i=$(($i+1))
#done
#mkdir $_name

if ! [[ "$_algorithm" == "$ALG1" || "$_algorithm" == "$ALG2" ]]; then
   echo "Error: $_algorithm, invalid type of algorithm - snake or pathfollow."
   exit
fi

if [ ! -d $_name ]; then
   mkdir $_name
fi

if [ ! -e speedCalc ]; then
   gcc -o speedCalc speedCalc.c
fi

cd $_name

if [ ! -d pydat ]; then
   mkdir pydat
fi

if [ ! -d histodat ]; then
   mkdir histodat
fi

if [ ! -d plt ]; then
   mkdir plt
fi

if [ ! -d png ]; then
   mkdir png
fi

if [ ! -d txt ]; then
   mkdir txt
fi


#temp file
#txtFile="txt/d"$_numberOfDrones"b"$_batteryTick"s"$_simulationSamples".txt"
txtFile="txt/temp.txt"
resultFile="$_name.dat"
hDataFile="H_r"$_batteryRange"s"$_speedOfDrone"d"$_numberOfDrones"n"$_simulationSamples".dat"
pDataFile="P_r"$_batteryRange"s"$_speedOfDrone"d"$_numberOfDrones"n"$_simulationSamples".dat"

_batteryTick=$(echo "scale=0; $_batteryRange/$_kmPerTick" | bc -l)
#echo $_batteryTick

echo " <<< $_name: $_nameDrone >>> "
echo "Running $_algorithm algorithm with $_simulationSamples simulation(s) for: $_numberOfDrones drone(s)"
echo "Drone type: $_batteryRange km ($_batteryTick ticks per battery), $_speedOfDrone m/s"

#echo "making file name.."

#j=1
if [ ! -e $resultFile ]; then
   echo "Name Range Speed Drones N Average" > $resultFile

   #resultFile=$(echo $_name"-"$j".dat")
   #j=$(($j+1))
fi



j=1
while [ -e histodat/$hDataFile ]; do
   #echo "Output file already exists, making new name.."
   hDataFile=$(echo "H_r"$_batteryRange"s"$_speedOfDrone"d"$_numberOfDrones"n"$_simulationSamples"-"$j".dat")
   j=$(($j+1))
done

j=1
while [ -e pydat/$pDataFile ]; do
   #echo "Output file already exists, making new name.."
   pDataFile=$(echo "P_r"$_batteryRange"s"$_speedOfDrone"d"$_numberOfDrones"n"$_simulationSamples"-"$j".dat")
   j=$(($j+1))
done

#echo "running python.."

cd ../..
python3 -W ignore Main.py $_numberOfDrones $_batteryTick $_simulationSamples $_algorithm > linuxResults/$_name/$txtFile $_show
cd linuxResults/$_name

#echo "running calculation and making data file.."

cd ..
./data.sh $_name/$txtFile $_batteryTick $_speedOfDrone $_simulationSamples $_numberOfDrones > $_name/histodat/$hDataFile

cd $_name

#echo "calculation average.."
 

pythonResults=$(cat $txtFile | tr -d '[]')
for (( i=1; i<=$_simulationSamples; i++ )); do      # loop for all N simulations
   ticks=$(echo $pythonResults | awk -F',' -v var="$i" '{print $var; }')
   #echo $_speedOfDrone $ticks
   calcResults=$(../speedCalc $_speedOfDrone $ticks)
   echo $calcResults >> pydat/$pDataFile
done
avg=$(cat pydat/$pDataFile | awk '{ total += $1; count++ } END { print total/count }') 


#echo "plotting the results.."

../plotter.sh $_nameDrone $hDataFile $_batteryRange $_speedOfDrone $_simulationSamples $_numberOfDrones $avg $_algorithm

echo "results: average time to find person: $avg min."
echo ""

echo "$_nameDrone $_batteryRange $_speedOfDrone $_numberOfDrones $_simulationSamples $avg" >> $resultFile

cd ..


