# Motor Control <img width="28" height="28" alt="image" src="https://github.com/user-attachments/assets/df83a6d3-bdec-41fd-8ddb-29f9e1b90688" />

Motors are essential for making machines move — from simple fans to robotic arms. A Raspberry Pi, although not a real-time microcontroller, can still control motors effectively using **GPIO pins**, **PWM**, and **motor drivers** like the **L298N**, **ULN2003**, or **TB6612FNG**.

<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/4569f7a6-1998-48fb-a088-174af3ed1909" />
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/1d3a4580-ce02-40b6-9612-2568d9dfa48e" />
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/41ace746-40ca-4e81-8ebc-ee93a3534757" />


### 1. GPIO Pin Control
Raspberry Pi GPIO pins can be used to control motor direction by toggling logic HIGH/LOW on driver inputs.

### 2. PWM for Speed Control
**PWM (Pulse Width Modulation)** is used to control motor speed by varying the duty cycle of the voltage signal applied to the motor.

### 3. Stepper Motor Control
Stepper motors are controlled by sending sequences of pulses to coils. The Pi sends these sequences using `RPi.GPIO` or `gpiozero`.

## Applications <img width="20" height="20" alt="image" src="https://github.com/user-attachments/assets/fd2d0bf4-5797-4420-8ff7-408462588054" />

- Line-following or maze-solving robots
- Conveyor belts and small robotic arms
- DIY CNC or 3D printing motion platforms
- Smart appliances and automation setups
