set term png size 800,600 enhanced font 'Helvetica,20'
set boxwidth 0.6
set grid ytics linestyle 0
set style fill solid 0.20 border 

set style data histograms
set style histogram clustered gap 1
#set xrange [0:]

set title "Path-follow algorithm"
set xlabel "Units used in simulation"
set ylabel "Average minutes for units \n to find lost person"

set output 'PATHBABY.png'
plot 'PATHBABY-histo.dat' using 3:xtic(1) ti col, '' u 4 ti col
set output 'PATHBABY-B.png'
plot 'PATHBABY-histo.dat' using 3:xtic(1) ti col, '' u 4 ti col, '' u 2 ti col
