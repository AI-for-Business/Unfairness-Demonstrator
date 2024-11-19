# Fatigue and Fairness Demonstrator using Blink Detection and Glasses Recognition

## Overview

This project is designed to serve as a **demonstration tool** for two primary use-cases:

1. **Fatigue Detection Demonstrator**: Based on blink detection, this demonstrator identifies signs of **fatigue** by analyzing blink frequency, size, and eye closure patterns. This component can be used to detect when an individual may be too tired to perform tasks, such as operating a vehicle in **TrackMania**.

2. **Unfairness Demonstrator**: This aspect demonstrates bias or disadvantage towards users who wear **glasses**. Glasses-wearers can be unfairly penalized in certain computer vision systems, with factors like **smaller eye size** or **dirty lenses** leading to less accurate detection results. Our system simulates this disadvantage in a game-like scenario.

## Educational Purpose

This project can be utilized as an **educational tool** for learning:
- **Computer vision** concepts and **blink detection**.
- Exploring potential **biases** in AI models, such as unfairness against glasses-wearers.
- Showcasing how **real-time detection systems** can be integrated into external environments, such as video games (TrackMania).

## Project Structure

The project consists of two main components:
1. **`main.py`** - This is the primary file that **integrates the demonstrator into TrackMania**. It receives the blink and glasses detection outputs and controls the car speed or behavior based on the detected conditions (e.g. reduced speed if the driver is fatigued or wearing glasses).

2. **`demonstrator.ipynb`** - This **Jupyter Notebook** is where the core demonstrator is built and trained. It contains the logic, models, and explanations for blink detection, glasses recognition, and the related unfairness simulation.

### Important Folders:
- **`src/`** - Contains the core source files for the project including:
  - `main.py`: Integrates the fatigue and unfairness demonstrators with **TrackMania**.
  - `demonstrator.ipynb`: A Jupyter Notebook where the demonstrator logic is built and developed.
  
- **`data/`** - This directory contains the labeled datasets used for training the **blink detection** and **glasses recognition** models. The data was labeled using **RoboFlow**, a popular tool for image annotation. The datasets focus on capturing blink data and glasses-wearer specific features.

- **`models/`** - Various models were trained using the **YOLO** (You Only Look Once) framework for blink and glasses detection. These models are stored as `.pt` files in this directory.

## Blink and Glasses Recognition

- The main component of this project is a custom-built **blink detection and glasses recognition AI**, developed with data collected and labeled using **RoboFlow**. This ensures optimal training data quality.
  
- **Training Process**:
  - We trained the BLINK and GLASSES coverage models using **YOLO**, a state-of-the-art framework for object detection.
  - Using **RoboFlow**, the data was annotated to properly classify **blinks** and **glasses**. These training datasets are essential to the performance of the demonstrator.
  - The trained models can be found in the `models/` directory, which can be used for inference in the project.

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/fatigue-fairness-demonstrator.git
   cd fatigue-fairness-demonstrator
   ```

2. **Install the dependencies**:
   Install the required Python packages using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Main Demonstrator**:
   To integrate the blink and glasses detection in **TrackMania**, run the following:
   ```bash
   python src/main.py
   ```
