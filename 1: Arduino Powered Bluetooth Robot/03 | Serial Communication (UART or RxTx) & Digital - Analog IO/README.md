# SERIAL COMMUNICATION

<img src="https://images.javatpoint.com/tutorial/coa/images/serial-communication-in-computer-organization10.png" alt="Serial" width="400" height="200">

Serial Communications is like a one-lane road, where the 1s and 0s are transmitted in single file. Serial communication allows for transmitting data over a communication channel, where data is sent one bit at a time. The speed of transmission is either referred to as the “BAUD” rate.

# PARALLEL COMMUNICATION

<img src="https://images.javatpoint.com/tutorial/coa/images/serial-communication-in-computer-organization11.png" alt="Parallel" width="400" height="300">

Parallel Communications is like a multi lane expressway, where the 1s and 0s are transmitted side by side.

# COMMUNICATION PROTOCOLS

<img src="https://github.com/user-attachments/assets/0142424a-09f3-41c3-b6b7-956ac5224e33" alt="Comm_Pro" width="150" height="150">

Communication protocols define the rules and standards for exchanging data between devices in embedded systems. Ex: UART, SPI, and I2C, each designed to meet different needs in terms of speed, complexity, and connectivity.

## UART (Universal Asynchronous Receiver Transmitter)

<img src="https://dwma4bz18k1bd.cloudfront.net/tutorials/uart-duplex-communication-connections.jpg" alt="uart" width="450" height="250">

- Enables serial communication between devices by converting parallel data to serial and vice versa.
- Two-Wire Communication: Uses Tx (Transmit) and Rx (Receive) lines for data transmission.
- Packet Structure: Includes a start bit, data frame, parity bit (for error checking), and stop bits.
- Asynchronous: No clock signal; relies on both devices sharing the same baud rate for timing.
- Bidirectional: Supports both half-duplex (one way at a time) and full-duplex (two-way) communication.
- Configurable: Developers can adjust parameters like baud rate and data format.

### Arduino Serial Monitor

<img src="https://i.ytimg.com/vi/4JYX03Z--DE/maxresdefault.jpg" alt="ser_mon_1" width="450" height="250"> <img src="https://docs.arduino.cc/static/dbdbdedc515103f7a46efe109a7d9255/4ef49/serial-monitor-img03.png" alt="ser_mon_2" width="400" height="250">

- Serial Monitor in the Arduino IDE is a tool that allows you to view the data being transmitted from the Arduino to the PC and send data from the PC to the Arduino.
- You can open the Serial Monitor via `Tools > Serial Monitor` or use the shortcut `Ctrl + Shift + M`.

### Serial Functions

- **Serial.print()** <br/>
  Serial.print(val): Serial - serial port object; val - the value to print any data type
  
- **Serial.println()** <br/>
  Serial.println(val): Serial - serial port object. See the list of available serial ports for each board on the Serial main page; val - the value to print any data type

- **Serial.begin()** <br/>
  Serial.begin(speed): Serial - serial port object; speed - in bits per second (baud)

- **Serial.read()** <br/>
  Serial.read(): Serial: serial port object.

- **Serial.write()** <br/>
  Serial.write(val)/(str)/(buf, len): Serial - serial port object; val - a value to send as a single byte; str - a string to send as a series of bytes; buf - an array to send as a series of bytes; len - the number of bytes to be sent from the array
  
## SPI (Serial Peripheral Interface)

<img src="https://github.com/user-attachments/assets/507a511a-baa1-4f47-a183-f42fb021c3e2" alt="SPI" width="450" height="250">

- SPI is a protocol that is synchronous serial communication, used to communicate between the peripheral devices i.e. input and output devices and microcontrollers. 
- It is allowed to transfer high-speed data. 
- It is popular with digital communication applications and embedded systems. 
- It can transfer the data and receive data from one device to another device at a time.

## I2C (Inter-Integrated Circuit)

<img src="https://dwma4bz18k1bd.cloudfront.net/tutorials/I2C-overview-cover.jpg" alt="I2C" width="450" height="250">

- It is a bus interface connection protocol incorporated into devices for serial communication.
- It uses only 2 bi-directional open-drain lines for data communication called SDA and SCL.
- Serial Data (SDA) : Transfer of data takes place through this pin.
- Serial Clock (SCL) : It carries the clock signal.
- I2C operates in 2 modes: Master mode & Slave mode
- Each data bit transferred on SDA line is synchronized by a high to the low pulse of each clock on the SCL line.

# ANALOG & DIGITAL SIGNALS

## Digital Signal

<img src="https://media.monolithicpower.com/wysiwyg/2_28.png" alt="dig" width="550" height="250">

- They are discrete signals that represent information using binary values—typically 0 and 1.
- They switch between defined voltage levels, corresponding to the two states (0 or 1).
- They are commonly used in computers, digital electronics, and communication systems.
- They are easier to process electronically, making them ideal for modern technology systems.

## Analog Signal

<img src="https://dwma4bz18k1bd.cloudfront.net/tutorials/10V-Sine-Wave-Amplitude.png" alt="ana" width="550" height="250">

- They are continuous signals that vary smoothly over time and can take any value within a range.
- They represent real-world phenomena like sound, temperature, or light intensity.
- They are more prone to noise and interference compared to digital signals.
- They are commonly used in devices like radios, sensors, and analog telephones.

## PWM (Pulse Width Modulation)

<img src="https://exploreembedded.com/wiki/images/5/54/0_LPC1768_PWM.gif" alt="pwm" width="450" height="250">

PWM (Pulse Width Modulation) is a technique used to control the amount of power sent to an electrical device by rapidly switching it on and off.

### Examples
1. **Dimming LED Lights <img src="https://cdn-icons-png.flaticon.com/128/436/436303.png" alt="led" width="20" height="20"> :** Used to control the brightness of LED lights. By rapidly turning the light on and off, and adjusting the amount of time the light stays on, the brightness can be smoothly controlled. <br/>
2. **Motor Speed Control <img src="https://cdn-icons-png.flaticon.com/128/13968/13968163.png" alt="motor" width="20" height="20"> :** In devices like electric fans or remote-controlled cars, PWM is used to control the speed of DC motors. Adjusting the on/off ratio allows the motor to run slower or faster based on the needs of the device. <br/>
3. **Servo Motors (in Robotics) <img src="https://cdn-icons-png.flaticon.com/128/6275/6275902.png" alt="motor" width="20" height="20"> :** PWM signals control the position of servo motors in robots and RC toys. By adjusting the pulse width, the motor moves to a specific angle. <br/>

