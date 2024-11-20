# SERIAL COMMUNICATION

<img src="https://images.javatpoint.com/tutorial/coa/images/serial-communication-in-computer-organization10.png" alt="Serial" width="500" height="250">

Serial Communications is like a one-lane road, where the 1s and 0s are transmitted in single file. The speed of transmission is either referred to as the “BAUD” rate.

# PARALLEL COMMUNICATION

<img src="https://images.javatpoint.com/tutorial/coa/images/serial-communication-in-computer-organization11.png" alt="Parallel" width="500" height="350">

Parallel Communications is like a multi lane expressway, where the 1s and 0s are transmitted side by side.

# COMMUNICATION PROTOCOLS

<img src="https://github.com/user-attachments/assets/0142424a-09f3-41c3-b6b7-956ac5224e33" alt="Comm_Pro" width="150" height="150">

Communication protocols define the rules and standards for exchanging data between devices in embedded systems. Serial communication allows for transmitting data over a communication channel, where data is sent one bit at a time. Ex: UART, SPI, and I2C, each designed to meet different needs in terms of speed, complexity, and connectivity.

## UART (Universal Asynchronous Receiver Transmitter)

<img src="https://dwma4bz18k1bd.cloudfront.net/tutorials/uart-duplex-communication-connections.jpg" alt="uart" width="400" height="300">

• Enables serial communication between devices by converting parallel data to serial and vice versa.
• Two-Wire Communication: Uses Tx (Transmit) and Rx (Receive) lines for data transmission.
• Packet Structure: Includes a start bit, data frame, parity bit (for error checking), and stop bits.
• Asynchronous: No clock signal; relies on both devices sharing the same baud rate for timing.
• Bidirectional: Supports both half-duplex (one way at a time) and full-duplex (two-way) communication.
• Configurable: Developers can adjust parameters like baud rate and data format.
