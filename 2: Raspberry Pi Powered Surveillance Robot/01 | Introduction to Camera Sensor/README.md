## What is a Camera Sensor? <img width="22" height="22" alt="image" src="https://github.com/user-attachments/assets/5c52b6e3-eb2e-4770-8e03-d57d248516cb" />

<img width="350" height="350" alt="image" src="https://github.com/user-attachments/assets/6dcd73cd-1bb0-4e10-9d17-c2b8195e62ab" />

A camera sensor is the electronic component that captures light and converts it into an electrical signal. Two major types:
1. CMOS (Complementary Metal Oxide Semiconductor)
2. CCD (Charge Coupled Device)

Camera sensors convert light into electrical signals using photodiodes. CMOS sensors process data on-chip, offering faster and more power-efficient operation, while CCD sensors provide higher image quality with better low-light performance but at higher cost and power consumption.
Each pixel on the sensor measures the intensity of light and converts it to a digital value.

### How it Works?
- **Light** enters through the lens
- Hits the **sensor array** (2D grid of photodiodes)
- Analog signal is **amplified and digitized**
- Output is processed to form an image/video frame

<img width="400" height="400" src="https://github.com/user-attachments/assets/b601d2c3-134b-4da2-b1fb-0295d0163bbb">

## Image Acquisition and Conversion to Digital Signals
When light hits the sensor, each pixel generates an analog voltage proportional to light intensity. This signal is then amplified, digitized via an ADC (Analog-to-Digital Converter), and processed to form a digital image.

## Interfacing Camera Modules with Embedded Systems
Camera modules are connected to embedded boards (like Raspberry Pi or Jetson Nano) via interfaces such as MIPI CSI, USB, or SPI, enabling real-time image capture and processing using onboard CPUs or GPUs.

## Basics of Real-Time Image Capture and Processing
Real-time image capture involves continuously reading frames from a camera feed and analyzing them using libraries like OpenCV for tasks such as filtering, edge detection, object tracking, or AI-based recognition.

## Applications of Camera Sensors in Real-World Systems
Camera sensors are used in autonomous robots, surveillance, medical imaging, agriculture monitoring, and AR/VR systems, enabling machines to "see" and make decisions based on visual data.
