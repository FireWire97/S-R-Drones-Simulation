#!/bin/bash

if [ $# != 4 ]; then
   echo "Error: $0 <# Drones> <Battery cap> <samples> <speed>"
   exit
fi

_numberOfDrones=$1
_batteryCapacity=$2
_simulationSamples=$3
_speedOfDrone=$4

if [ ! -d txt ]; then
   mkdir txt
fi

txtFile="txt/d"$_numberOfDrones"b"$_batteryCapacity"s"$_simulationSamples".txt"

echo "running python.."

cd ..
python3 Main.py $_numberOfDrones $_batteryCapacity $_simulationSamples > linuxResults/$txtFile
cd linuxResults

echo "running calculation and plotting.."

./calculator.sh $txtFile $_speedOfDrone

echo "should be done!"


