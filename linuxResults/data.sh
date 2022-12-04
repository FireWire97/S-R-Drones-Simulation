#!/bin/bash

## This outputs <after this many minutes> <this many people were found>
## That is, after running the simulation N times.
## Output goes directly in terminal if nothing is done with it.
## Made for histograms

if [ $# != 5 ]; then
   echo "Error: $0 <result.file to read> <range> <speed of drone> <simulations> <number of drones>"
   exit
fi

pythonFile=$1
battery=$2
speed=$3
simulations=$4
drones=$5

#echo "Reading results.."

# Gather information from text file
pythonResults=$(cat $pythonFile | tr -d '[]')

# Calculate results into an array using C program
function _calculate {
   for (( i=1; i<=$simulations; i++ )); do      # loop for all N simulations
      ticks=$(echo $pythonResults | awk -F',' -v var="$i" '{print $var; }')
      calcResults=$(./speedCalc $speed $ticks)
      #echo $calcResults >> $file
      blah+=("$calcResults")
   done
   minutes=$(echo ${blah[@]} | awk 'BEGIN{RS=" ";} {print $1}' | sort -n)
   #echo ${minutes[@]}
   
   max=0
   for n in ${minutes[@]}; do
      if (( $n > $max )); then
         max=$n
      fi
   done
   #echo $max
}

# Make a data with results
function _data {
   for (( k=0; k<=$max; k++ )); do
      count=0
      for number in ${minutes[@]}; do 
         if [[ $number =~ ^[$k]$ ]] && [[ $k -lt 10 ]]; then
            (( count++ ))
         elif [[ $number =~ $k ]] && [[ $k -ge 10 ]]; then
            (( count++ ))
         fi
      done
      echo $k $count
      #echo $k $count >> $file
      #blaah[$k]=$count
   done
   #echo ${blaah[@]}
}

#echo "Calculating.."
_calculate
_data


