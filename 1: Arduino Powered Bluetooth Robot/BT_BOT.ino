#include <NewPing.h>

// --- Ultrasonic Sensor ---
#define TRIG_PIN 9
#define ECHO_PIN 8
#define MAX_DISTANCE 200
NewPing sonar(TRIG_PIN, ECHO_PIN, MAX_DISTANCE);

// --- Motor Driver Pins ---
#define ENA 5
#define IN1 6
#define IN2 7
#define IN3 10
#define IN4 11
#define ENB 3

// --- Bluetooth ---
char command = ' ';

void setup() {
  Serial.begin(9600);  // Bluetooth Serial

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  stopMotors();
}

void loop() {
  if (Serial.available()) {
    command = Serial.read();
    handleBluetoothCommand(command);
  } else {
    autonomousNavigation();  // No command? Go autonomous
  }
}

// --- Bluetooth Command Handler ---
void handleBluetoothCommand(char cmd) {
  switch (cmd) {
    case 'F': moveForward(); break;
    case 'B': moveBackward(); break;
    case 'L': turnLeft(); break;
    case 'R': turnRight(); break;
    case 'S': stopMotors(); break;
  }
}

// --- Autonomous Mode ---
void autonomousNavigation() {
  delay(50);
  int distance = sonar.ping_cm();
  if (distance == 0) distance = 250;

  if (distance < 20) {
    stopMotors();
    delay(200);
    turnRight();
    delay(400);
  } else {
    moveForward();
  }
}

// --- Motor Control ---
void moveForward() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 180);
  analogWrite(ENB, 180);
}

void moveBackward() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(ENA, 180);
  analogWrite(ENB, 180);
}

void turnLeft() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 180);
  analogWrite(ENB, 180);
}

void turnRight() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(ENA, 180);
  analogWrite(ENB, 180);
}

void stopMotors() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
}
