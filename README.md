# Chronic Kidney Disease Detection

This is a Tkinter-based desktop application for detecting chronic kidney disease using pre-trained machine learning models. The application allows users to input various medical features and select a model to predict the presence of chronic kidney disease.

## Features

- **Model Selection:** Choose from multiple pre-trained models stored in the `models` directory.
- **Input Features:** Enter values for various medical features used in chronic kidney disease detection.
- **Prediction:** Get a prediction result based on the selected model and input features.
- **User-Friendly Interface:** A fully customizable and colorized GUI for enhanced user experience.

## Requirements

- Python 3.x
- `tkinter` library
- `joblib` library

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/mo-zekry/chronic_kidney_classifier.git
    cd chronic_kidney_classifier
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```


## Usage

1. **Run the application:**
    ```sh
    python main.py
    ```

2. **Using the GUI:**
    - Select a model from the dropdown menu.
    - Enter values for all required features.
    - Click the "Classify" button to get the prediction result.


### Input Features

The following medical features are used for the prediction:

- Age
- Blood Pressure
- Specific Gravity
- Albumin
- Sugar
- Red Blood Cells
- Pus Cell
- Pus Cell Clumps
- Bacteria
- Blood Glucose Random
- Blood Urea
- Serum Creatinine
- Sodium
- Potassium
- Haemoglobin
- Packed Cell Volume
- White Blood Cell Count
- Red Blood Cell Count
- Hypertension
- Diabetes Mellitus
- Coronary Artery Disease
- Appetite
- Peda Edema
- Aanemia