// Pin definitions for motor control
int in1 = 3;
int in2 = 4;
int in3 = 5;
int in4 = 6;
int en1 = 9;
int en2 = 10;

// Variables for Bluetooth input
char command;

void setup() 
{
  // Set up motor pins as outputs
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(en1, OUTPUT);
  pinMode(en2, OUTPUT);

  // Set PWM speed for both motors (0-255)
  analogWrite(en1, 55);  // Full speed for motor 1
  analogWrite(en2, 55);  // Full speed for motor 2

  // Start serial communication for Bluetooth module
  Serial.begin(9600);
}

void loop() 
{
  // Check if data is received via Bluetooth
  if (Serial.available() > 0) 
  {
    command = Serial.read();  // Read the incoming data

    // Control the car based on the command received
    if (command == 'F') 
    {
      // Move forward
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
      Serial.print("forawar");
    } 
    else if (command == 'B') 
    {
      // Move backward
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
      digitalWrite(in3, LOW);
      digitalWrite(in4, HIGH);
      Serial.print("backward");
    } 
    else if (command == 'R') 
    {
      // Turn left
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
      digitalWrite(in3, HIGH);
      digitalWrite(in4, LOW);
      Serial.print("left");
    } 
    else if (command == 'L') 
    {
      // Turn right
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      digitalWrite(in3, LOW);
      digitalWrite(in4, HIGH);
      Serial.print("right");
    } 
    else if (command == 'S') 
    {
      // Stop
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      digitalWrite(in3, LOW);
      digitalWrite(in4, LOW);
      Serial.print("stop");
    }
  }
}