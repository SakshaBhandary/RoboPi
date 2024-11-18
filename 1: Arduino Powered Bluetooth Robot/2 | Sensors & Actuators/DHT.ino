#include "DHT.h"
DHT dht(8,DHT22);

void setup()
{
  Serial.begin(9600);
  dht.begin();
}

void loop()
{
  float temp = dht.readTemperature();
  Serial.print("Temp:");
  Serial.print(temp);
  Serial.println(" °C");
  delay(1000);
}



