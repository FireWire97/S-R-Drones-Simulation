// % gcc -o speedCalc speedCalc.c
// Program to calculate true time from ticks

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// fixed wing m/s: 18 - 22 - 22 - 31
// battery km: 250 - 241 - 322 - 788
// battery ticks: 971 - 936 - 1250 - 3059 
//    (calculated in excel using 0,25756km per tick ($disT))

// multi roto m/s: 8,9 - 8,9 - 8,9 - 5,3
// battery km: 24 - 128 - 96 - 11
// battery ticks: 93 - 497 - 373 - 43 (calculated in excel)

const double mapX = 22.14; //[km] width of the map on x axis
const double mapY = 5.26;  //[km] length of the map on y axis
const double simX = 60;    //X range of simulator 
const double simY = 36;    //Y range of simulator
//const double speedFixed[4] = {18, 22, 22, 31};
//const double speedDrone[4] = {8.9, 8.9, 8.9, 5.3};

int main(int argc, char *argv[]){
   float speed, disX, disY, disT;
   float ticks;
   float seconds, minutes;

   // using arguments 
   if( argc != 3 ) {
      printf("Error:%s <speed of drone> <number of ticks>\n",argv[0]);
      return 1;
   }
   speed = atof(argv[1]);              // speed of drone
   ticks = atof(argv[2]);              // drone movement
   //printf("speed: %f\tticks: %f\n", speed, ticks);

   // calculating distance for each 'tick'
   disX = 1000 * mapX / simX;          //distance per tick in meters
   disY = 1000 * mapY / simY;          //distance per tick in meters
   disT = (disX + disY)/2;             //taking the average
   // disT = 0.257555542 [km], 
   // used to change battery range [km] into ticks per battery life   

   // calculating the time for the drone to travel
   seconds = 1/(speed / (disT*ticks));
   minutes = seconds / 60;

   // output results [min]
   printf("%.f\t\n", minutes);

   return 0;
}

