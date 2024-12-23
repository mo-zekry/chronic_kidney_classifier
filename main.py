import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import os

# Path to the models folder
MODELS_DIR = "models"

# Features for chronic kidney disease detection
FEATURES = [
    "age", "blood_pressure", "specific_gravity", "albumin", "sugar",
    "red_blood_cells", "pus_cell", "pus_cell_clumps", "bacteria",
    "blood_glucose_random", "blood_urea", "serum_creatinine", "sodium",
    "potassium", "haemoglobin", "packed_cell_volume", "white_blood_cell_count",
    "red_blood_cell_count", "hypertension", "diabetes_mellitus",
    "coronary_artery_disease", "appetite", "peda_edema", "aanemia"
]

def load_models(models_dir):
    """Load all models from the specified directory."""
    models = {}
    try:
        for filename in os.listdir(models_dir):
            if filename.endswith('.pkl'):
                model_name = filename.split('.')[0]
                model_path = os.path.join(models_dir, filename)
                models[model_name] = joblib.load(model_path)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load models: {e}")
    return models

def classify(model, input_data):
    """Classify input data using the selected model."""
    try:
        prediction = model.predict([input_data])[0]
        return prediction
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during classification: {e}")
        return None

def validate_input(value, feature):
    """Validate input value for a given feature."""
    if value == "":
        messagebox.showwarning("Warning", f"Please enter a value for {feature}!")
        return False
    try:
        float(value) if value.replace('.', '', 1).isdigit() else value
        return True
    except ValueError:
        messagebox.showerror("Error", f"Invalid input value for {feature}: {value}")
        return False

def on_classify(model_var, entry_vars, models):
    """Handle the classify button click event."""
    selected_model_name = model_var.get()
    if not selected_model_name:
        messagebox.showwarning("Warning", "Please select a model!")
        return

    selected_model = models.get(selected_model_name)
    input_data = []

    # Collect inputs for all features
    for feature in FEATURES:
        value = entry_vars[feature].get()
        if not validate_input(value, feature):
            return
        input_data.append(float(value) if value.replace('.', '', 1).isdigit() else value)

    # Perform classification
    prediction = classify(selected_model, input_data)
    if prediction is not None:
        messagebox.showinfo("Prediction Result", f"Prediction: {prediction}")

def create_gui():
    """Create and run the GUI application."""
    root = tk.Tk()
    root.title("Chronic Kidney Disease Detection")
    root.geometry("700x900")
    root.resizable(True, True)

    # Define custom styles
    style = ttk.Style()
    style.theme_use('clam')

    style.configure('TFrame', background='#f0f0f0')
    style.configure('TLabelFrame', background='#d3d3d3', foreground='#333333', font=('Arial', 12, 'bold'))
    style.configure('TLabel', background='#d3d3d3', foreground='#333333', font=('Arial', 10))
    style.configure('TEntry', font=('Arial', 10))
    style.configure('TButton', background='#4caf50', foreground='#ffffff', font=('Arial', 10, 'bold'))

    # Frame for model selection
    model_frame = ttk.LabelFrame(root, text="Model Selection", padding="10")
    model_frame.pack(padx=10, pady=10, fill="x")

    model_label = ttk.Label(model_frame, text="Select Model:")
    model_label.grid(row=0, column=0, padx=5, pady=5, sticky="W")

    model_var = tk.StringVar()
    model_dropdown = ttk.Combobox(model_frame, textvariable=model_var)
    model_dropdown['values'] = list(models.keys())
    model_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="E")

    # Frame for input features with scrollbar
    input_frame = ttk.LabelFrame(root, text="Input Features", padding="10")
    input_frame.pack(padx=10, pady=10, fill="both", expand=True)

    canvas = tk.Canvas(input_frame, background='#f0f0f0')
    scrollbar = ttk.Scrollbar(input_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas, style='TFrame')

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    entry_vars = {}
    for i, feature in enumerate(FEATURES):
        label = ttk.Label(scrollable_frame, text=f"{feature}:")
        label.grid(row=i, column=0, padx=5, pady=5, sticky="W")
        entry_var = tk.StringVar()
        entry_vars[feature] = entry_var
        entry = ttk.Entry(scrollable_frame, textvariable=entry_var)
        entry.grid(row=i, column=1, padx=5, pady=5, sticky="E")
        # Tooltips for better user guidance
        tooltip = ttk.Label(scrollable_frame, text="Enter the value for " + feature, foreground="grey", background='#f0f0f0')
        tooltip.grid(row=i, column=2, padx=5, pady=5, sticky="W")

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Button to make predictions
    classify_button = ttk.Button(root, text="Classify", command=lambda: on_classify(model_var, entry_vars, models))
    classify_button.pack(pady=20)

    root.mainloop()

# Load all models at the start
models = load_models(MODELS_DIR)

# Run the GUI
if __name__ == "__main__":
    create_gui()