# Hybrid-Realness-Verification-System
A multimodal deepfake detection system that analyzes images, videos, and audio to classify content as "Real" or "Fake." This project integrates advanced machine learning techniques and is designed for educational and research purposes.
# Hybrid Realness Verification System

## Overview

This project detects deepfakes across multiple modalities:

- **Image Detection:**  
  Uses a fine-tuned **Vision Transformer (ViT)** for binary classification of real vs fake images.  
  Download dataset: [Real and Fake Face Detection](https://www.kaggle.com/datasets/ciplab/real-and-fake-face-detection)

- **Video Detection:**  
  Utilizes **Optical Flow** features with a **Support Vector Machine (SVM)** to analyze temporal patterns in videos.  
  Download dataset: [DFDC Dataset](https://www.kaggle.com/datasets/ashifurrahman34/dfdc-dataset)

- **Audio Detection:**  
  Applies a **Convolutional Neural Network (CNN)** on Mel Spectrograms to detect synthetic speech.  
  Download dataset: [Deep Voice Deepfake Voice Recognition](https://www.kaggle.com/datasets/birdy654/deep-voice-deepfake-voice-recognition?select=KAGGLE)

- **Deployment:**  
  Hosted via **Flask** web app allowing file uploads and result visualization.

---

## Features

- Supports **image files**: `.jpg`, `.jpeg`, `.png`  
- Supports **video files**: `.mp4`, `.avi`  
- Supports **audio files**: `.mp3`, `.wav`  
- Returns **classification results with confidence scores**  
- Maximum upload file size: **100MB**

---

## To Execute

### Clone the repository

bash
git clone https://github.com/harshitha-809/Hybrid_Realness_Verification_System.git
cd Hybrid_Realness_Verification_System

**Setup and Usage**

**Create and Activate Virtual Environment**

#### Create virtual environment (Windows)
bash
python -m venv venv
#### Activate virtual environment (Windows)
bash
venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### Train
Download audio dataset into folder datasets which contains real, fake folders train using python training/train_audio.py ->which creates weights folder with .pth file for image and video download the datasets and place them in your google drive, use google collab to train, use runtime gpu for faster process add the dowloaded .pth files of image and video in weights folder

### Run
python app.py

Running on http://127.0.0.1:5000/


