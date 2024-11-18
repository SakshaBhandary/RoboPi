int ir=8;
int led=13;

void setup()
{
  Serial.begin(9600);
  pinMode(ir,INPUT);
  pinMode(led,OUTPUT);
}
void loop()
{
  if(digitalRead(ir)==1)
  {
    digitalWrite(led,HIGH);
    Serial.println("LED ON");
  }
  else
  {
    digitalWrite(led,LOW);
  }
}
