#include "Servo.h"
int servopin=8;

Servo s;

void setup()
  {
    s.attach(servopin);
  }
void loop()
  {
   s.write(0);
   delay(1000);
   s.write(90);
   delay(1000);
   s.write(180);
   delay(1000);
  }


  