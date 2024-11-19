char command; // Variable to store the received command
int ledPin = 13; // LED connected to digital pin 13

void setup() {
  Serial.begin(9600);  // Initialize serial communication at 9600 baud rate
  pinMode(ledPin, OUTPUT);  // Set the LED pin as an output
  Serial.println("Bluetooth Ready - Send '1' to turn ON LED and '0' to turn OFF LED");
}

void loop() {
  if (Serial.available()) {  // Check if data is available to read
    command = Serial.read(); // Read the incoming character

    // Respond to the command
    if (command == '1') {
      digitalWrite(ledPin, HIGH);  // Turn ON the LED
      Serial.println("LED ON");
    }
    else if (command == '0') {
      digitalWrite(ledPin, LOW);   // Turn OFF the LED
      Serial.println("LED OFF");
    }
    else {
      Serial.println("Invalid Command. Send '1' to turn ON or '0' to turn OFF.");
    }
  }
}
