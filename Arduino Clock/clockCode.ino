#include <Time.h>

const byte digitalLine[9] = {2,3,4,5,9,10,11,12};

byte digitValue[4];
int x;

const byte segmentPattern[10] = {
 B11111101,
 B10010000,
 B11101011,
 B10111011,
 B10010111,
 B00111111,
 B01111111,
 B10011000,
 B11111111,
 B10111111 };
 
const byte segmentPatternTwo[10] = {
 B11111100,
 B10010000,
 B11101011,
 B10111011,
 B10010111,
 B00111111,
 B01111111,
 B10011000,
 B11111111,
 B10111111 };
 
const byte segmentPatternThree[10] = {
 B11111110,
 B10010000,
 B11101001,
 B10111001,
 B10010111,
 B00111111,
 B01111111,
 B10011000,
 B11111111,
 B10111111 };
 
const byte segmentPatternFour[10] = {
 B11111110,
 B10010000,
 B11101101,
 B10111101,
 B10010011,
 B00111111,
 B01111111,
 B10011100,
 B11111111,
 B10111111 };

void setup() {
  Serial.begin(9600);
  setTime(9,45,00,23,8,2015);
}

void loop() {
 
 // Display elapsed time in tenths of a second.
 time_t t = now();
    Serial.print(hour(t));
    Serial.println(minute(t));
    Serial.println((hour(t)*100)+minute(t));
    int x = ((hour(t)*100)+minute(t));


 
 // Turn the number to be displayed into 4 digits
 digitValue[3] = x % 10;
 digitValue[2] = x / 10 % 10;
 digitValue[1] = x / 100 % 10;
 digitValue[0] = x / 1000 % 10;
 
 // Briefly light each digit
 for (byte digit = 0; digit < 4; digit++) {
   // Set up the segments for this digit
   for (byte segment = 0; segment < 8; segment++) {

     byte useSegment = segment;
     
     // If this segment's line also happens to be the line controlling
     // the whole digit, the 9th line will be wired up instead
     if (segment == digit){
       useSegment = 8;
     }

     // look up the value for this segment for this digit
     switch(digit) {
       case 0:
           if(digitValue[digit] == 0 ){
             pinMode(digitalLine[useSegment], INPUT);
             break;
           } else {
           if (bitRead(segmentPattern[digitValue[digit]], segment) == 1) {
      
             // the segment needs to be on
             pinMode(digitalLine[useSegment], OUTPUT);
             digitalWrite(digitalLine[useSegment], LOW);
      
           }       
           else {
      
             // the segment needs to be off
             pinMode(digitalLine[useSegment], INPUT);
      
           }
           }
           break;
      case 1:
           if (bitRead(segmentPatternTwo[digitValue[digit]], segment) == 1) {
      
             // the segment needs to be on
             pinMode(digitalLine[useSegment], OUTPUT);
             digitalWrite(digitalLine[useSegment], LOW);
      
           }       
           else {
      
             // the segment needs to be off
             pinMode(digitalLine[useSegment], INPUT);
      
           }
           break;
      case 2:
          if (bitRead(segmentPatternThree[digitValue[digit]], segment) == 1) {
      
             // the segment needs to be on
             pinMode(digitalLine[useSegment], OUTPUT);
             digitalWrite(digitalLine[useSegment], LOW);
      
           }       
           else {
      
             // the segment needs to be off
             pinMode(digitalLine[useSegment], INPUT);
      
           }
           break;
      case 3:
          if (bitRead(segmentPatternFour[digitValue[digit]], segment) == 1) {
      
             // the segment needs to be on
             pinMode(digitalLine[useSegment], OUTPUT);
             digitalWrite(digitalLine[useSegment], LOW);
      
           }       
           else {
      
             // the segment needs to be off
             pinMode(digitalLine[useSegment], INPUT);
      
           }
           break;
      
   }
   }

   // all segments now ready, so switch on the digit
   pinMode(digitalLine[digit], OUTPUT);
   digitalWrite(digitalLine[digit], HIGH);

   // Wait a moment
   delay(1);

   // Switch the digit off again
   pinMode(digitalLine[digit], INPUT);
   

 }
 

}














