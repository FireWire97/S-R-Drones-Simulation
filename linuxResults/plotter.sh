#!/bin/bash

if [ $# != 8 ]; then
   echo "Error: $0 <name> <data.file to read> <range> <speed of drone> <simulations> <number of drones> <average> <algorithm>"
   exit
fi

name=$1
file=$2
battery=$3
speed=$4
simulations=$5
drones=$6
avg=$7
alg=$8


if [[ "$alg" == "snake" ]]; then
   alg="Snake algorithm"
elif [[ "$alg" == "pathfollow" ]]; then
   alg="Path following algorithm"
fi

function _gnuplot {
   filePlt=$(echo $file | sed 's/\.dat/\.plt/')
   filePng=$(echo $file | sed 's/\.dat/\.png/')
   #batteryCap=$(echo "scale=0; $battery * 0.25756" | bc -l)  
   #batteryCap=$(awk 'BEGIN {print int('$battery' * 0.25756)}')
   echo "set term png size 800,600 enhanced font 'Helvetica,20'" > $filePlt
   echo "set output 'png/$filePng'" >> $filePlt
   echo "set title \"$alg: $name \n{/*0.5 Number of drones: $drones, speed of drone: $speed m/s, range: $battery km, samples: $simulations}\"" >> $filePlt
   echo "set xlabel '{/*0.8 Time(min)}'" >> $filePlt
   echo "set ylabel '{/*0.8 People found}'" >> $filePlt
   echo "set xrange [0:]" >> $filePlt
   echo "set yrange [0:]" >> $filePlt
   #echo "set xrange [0:200]" >> $filePlt
   #echo "set yrange [0:20]" >> $filePlt
   echo "set boxwidth 0.9 relative" >> $filePlt
   echo "set grid ytics linestyle 0" >> $filePlt

   echo "set style fill solid 0.20 border" >> $filePlt 
   echo "set style data histogram" >> $filePlt
   #echo "set style histogram rowstacked" >> $filePlt

   #echo "set terminal svg size 1200,800" >> $filePlt

   echo "plot 'histodat/$file' u 2 with histogram lc 6 t '{/*0.6 Average: $avg}'" >> $filePlt
   #echo "plot '$file' u 1:2 w l t 'blah' " >> $filePlt
   #echo "binwidth=1" >> $filePlt
   #echo "bin(x,width)=width*floor(x/width)" >> $filePlt
   #echo "plot '$file' using (bin(\$1,binwidth)):(1.0) smooth freq with boxes" >> $filePlt

   echo "image ready in png/$filePng"
}


cd plt
_gnuplot
cd ..
gnuplot -p plt/$filePlt


