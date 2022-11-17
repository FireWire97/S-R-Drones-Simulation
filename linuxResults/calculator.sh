#!/bin/bash

if [ $# != 2 ]; then
   echo "Error: $0 <result.file to read> <speed of drone>"
   exit
fi

if [ ! -d data ]; then
   mkdir data
fi

if [ ! -d plt ]; then
   mkdir plt
fi

if [ ! -d png ]; then
   mkdir png
fi

pythonFile=$1
speed=$2

echo "Reading results.."

pythonResults=$(cat $pythonFile | tr -d '[]')
drones=$(echo $pythonFile | sed 's/.*d//' | sed 's/b.*//')
battery=$(echo $pythonFile | sed 's/.*b//' | sed 's/s.*//')
simulations=$(echo $pythonFile | sed 's/.*s//' | sed 's/\..*//')
file=$(echo $pythonFile | sed 's/.*\///' | sed 's/\.txt//')
ext=".dat"
file=$(echo $file"v"$speed$ext)
#echo $drones
#echo $battery
#echo $simulations
#echo $pythonResults

j=1
while [ -e data/$file ]; do
   #echo "Output file already exists, finding new name.."
   file=$(echo "d"$drones"b"$battery"s"$simulations"v"$speed"-"$j$ext)
   j=$(($j+1))
done

function _calculate {
   for (( i=1; i<=$simulations; i++ )); do      # loop for all 100 simulations
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

function _counter {
   cd data
   for (( k=0; k<=$max; k++ )); do
      count=0
      for number in ${minutes[@]}; do 
         if [[ $number =~ ^[$k]$ ]] && [[ $k -lt 10 ]]; then
            (( count++ ))
         elif [[ $number =~ $k ]] && [[ $k -ge 10 ]]; then
            (( count++ ))
         fi
      done
      echo $k $count >> $file
      #blaah[$k]=$count
   done
   cd ../
   #echo ${blaah[@]}
}

function _printer {
   for (( j=0; j<=${#minutes[@]}; j++ )); do
      echo $minutes[$j] asda  $blaah[$j]
   done 
}

function _gnuplot {
   cd plt
   filePlt=$(echo $file | sed 's/\.dat/\.plt/')
   filePng=$(echo $file | sed 's/\.dat/\.png/')
   #batteryCap=$(echo "scale=0; $battery * 0.25756" | bc -l)  
   batteryCap=$(awk 'BEGIN {print int('$battery' * 0.25756)}')
   echo "set term png size 800,600 enhanced font 'Helvetica,20'" > $filePlt
   echo "set output 'png/$filePng'" >> $filePlt
   echo "set title \"Snake Search: Time vs. Frequency\n{/*0.5 Number of drones: $drones, speed of drone: $speed m/s, battery capacity: $batteryCap km, samples: $simulations}\"" >> $filePlt
   echo "set xlabel '{/*0.5 minutes}'" >> $filePlt
   echo "set ylabel '{/*0.5 frequency}'" >> $filePlt
   echo "set xrange [0:]" >> $filePlt
   echo "set yrange [0:]" >> $filePlt
   echo "set boxwidth 0.9 relative" >> $filePlt
   echo "set grid ytics linestyle 0" >> $filePlt

   echo "set style fill solid 0.20 border" >> $filePlt 
   echo "set style data histogram" >> $filePlt
   #echo "set style histogram rowstacked" >> $filePlt

   #echo "set terminal svg size 1200,800" >> $filePlt

   echo "plot 'data/$file' u 2 with histogram lc 6 t ''" >> $filePlt
   #echo "plot '$file' u 1:2 w l t 'blah' " >> $filePlt
   #echo "binwidth=1" >> $filePlt
   #echo "bin(x,width)=width*floor(x/width)" >> $filePlt
   #echo "plot '$file' using (bin(\$1,binwidth)):(1.0) smooth freq with boxes" >> $filePlt

   echo "gnuplot ready in plt/$filePlt"
   cd ../
}


echo "Calculating.."
_calculate
_counter
#_printer
echo "data in data/$file"
_gnuplot
echo "plotting.."
gnuplot -p plt/$filePlt
echo "plot ready in png/$filePng"


