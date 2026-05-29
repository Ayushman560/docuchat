# Driver's Drowsiness Detection System

A real-time driver drowsiness detection system using computer vision and deep learning that monitors eye state to detect fatigue and trigger alerts, helping prevent road accidents caused by drowsy driving.

## Demo
The system continuously monitors the driver's eyes through a webcam. When drowsiness is detected for consecutive frames, an audio alarm is triggered immediately.

## Features
- Real-time eye state detection via webcam
- Facial landmark detection with 68 keypoints using dlib
- CNN-based eye classifier trained on open/closed eye dataset
- Audio alert system triggered on drowsiness detection
- Works under varying lighting conditions and head poses

## How It Works
1. Webcam captures real-time video frames
2. dlib detects 68 facial landmarks on the face
3. Eye region is extracted from the landmarks
4. CNN model classifies eye as open or closed
5. If eyes remain closed for N consecutive frames, alarm triggers

## Tech Stack
- Python
- OpenCV
- dlib
- TensorFlow / Keras
- PyTorch
- pygame
- CNN (Convolutional Neural Network)
- Eye Aspect Ratio (EAR)

## Project Structure
