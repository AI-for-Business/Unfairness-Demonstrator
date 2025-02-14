# Real-Life Demonstrator for Disparate Performance with AI-Based Drowsiness Detection

## Overview

This project demonstrates how **drowsiness detection** can be simulated using blink tracking and how **AI bias against glasses-wearers** can be illustrated. The system detects drowsiness based on blinking patterns and simulates the difficulty of detecting blinks for glasses-wearers by lowering the **Eye Aspect Ratio (EAR) threshold** for them.

### Key Aspects:
1. **drowsiness Detection Simulation**
   - Detects drowsiness by analyzing blink frequency and eye closure patterns.
   - Recognizes reduced blinking over time as an indicator of drowsiness.

2. **Unfairness Simulation for Glasses-Wearers**
   - Simulates how drowsiness detection systems might perform worse for users with glasses.
   - Adjusts EAR thresholds to make it harder to detect blinks when glasses are worn.

## How It Works
- **Blink detection** is based on the Eye Aspect Ratio (EAR), which measures the openness of the eyes.
- **drowsiness is determined** if a user blinks too infrequently or closes their eyes for prolonged periods.
- **Glasses-wearers face detection bias**, as their EAR values are harder to detect, simulating real-world AI challenges.

## Educational Purpose
This project helps users understand:
- **Computer vision** principles behind blink detection.
- **Bias in AI models** affecting real-world applications.
- The role of **real-time detection systems** in human behavior tracking (e.g., in gaming like **TrackMania**).

## Project Structure

### Core Components:
1. **`main.py`** - The primary script running the simulation in a standalone Python file.
2. **`demonstrator.ipynb`** - A Jupyter Notebook for interactive demonstration of drowsiness and bias.
3. **`trackmania.ipynb`** - A Jupyter Notebook integrating the system into **TrackMania**.

### Key Directories:
- **`src/`** - Contains implementation files (`main.py`, `trackmania.ipynb`, etc.).
- **`data/`** - Labeled datasets for training blink and glasses detection models.
- **`models/`** - Pre-trained **YOLO** models for blink and glasses recognition.

## Running the Demonstrator

### 1. Installation
#### Clone the Repository:
```bash
git clone https://github.com/your-repo/drowsiness-fairness-demonstrator.git
cd drowsiness-fairness-demonstrator
```
#### Install Dependencies:
```bash
pip install -r requirements.txt
```

### 2. Running the Main Simulation
To execute the **drowsiness and bias detection** system:
```bash
python src/main.py
```

### 3. Running in TrackMania
#### Setup TrackMania:
1. Open **Ubisoft Connect** (not the Game Launcher!).
2. Log in with your credentials.
3. Navigate to **Library** and start **TrackMania**.
4. Select **Create** → **Track Editor**.
5. Choose **Edit a Track**.
6. Navigate to **My Local Tracks** → **My Maps**.
7. Click **Test**.
8. Press the **green (or yellow) flag** to start the track.

#### Start the Demonstrator:
1. Open **Visual Studio Code** as Administrator.
   - Right-click **Visual Studio Code** in the Windows menu.
   - Select **Run as Administrator**.
2. Open the project folder: **File** → **Open Folder** → **unfairness_demonstrator**.
3. Open **`trackmania.ipynb`** in Jupyter Notebook. Or execude the **`main.py`** File
4. Run the first two code cells to start the simulation.

## Scientific Basis
This project is based on research in drowsiness detection and AI bias:
- [Dong et al. (2011)](https://web.archive.org/web/20170808091400id_/http:/cvrr.ucsd.edu/ece285/Spring2014/papers/Dong_TITS2011.pdf)
- [Blinks and saccades as indicators of drowsiness](https://www.researchgate.net/publication/5287545_Blinks_and_saccades_as_indicators_of_drowsiness_in_sleepiness_warnings_Looking_tired/link/02e7e536f97a6a8387000000/download?_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InB1YmxpY2F0aW9uIiwicGFnZSI6InB1YmxpY2F0aW9uIn19)
- [drowsiness Detection in Electronics](https://www.mdpi.com/2079-9292/11/19/3183#B17-electronics-11-03183)
- [drowsiness Monitoring Studies](https://peerj.com/articles/cs-943/)
- [Blink Research](https://www.blinkingmatters.com/research)
- [drowsiness and Eye Tracking](https://www.sciencedirect.com/science/article/pii/S1077314216300054#sec0009)
- [drowsiness Detection via Blinks](https://www.mdpi.com/2076-3417/11/18/8441)

---
