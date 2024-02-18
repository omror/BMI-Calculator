import tkinter as tk

def calculate_bmi():
    height = float(entry_height.get()) / 100 # converting height to meters
    weight = float(entry_weight.get())
    bmi = weight / (height * height)
    label_result.config(text=f"BMI: {bmi:.2f}")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels
label_title = tk.Label(root, text="Calculate Your BMI", font=("Helvetica", 16))
label_title.grid(row=0, columnspan=2, padx=10, pady=5)

label_height = tk.Label(root, text="Height (cm):")
label_height.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=5)

label_weight = tk.Label(root, text="Weight (kg):")
label_weight.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_weight = tk.Entry(root)
entry_weight.grid(row=2, column=1, padx=10, pady=5)

# Create calculate button
button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.grid(row=3, columnspan=2, padx=10, pady=10)

# Create label to display result
label_result = tk.Label(root, text="")
label_result.grid(row=4, columnspan=2)


# Run the main event loop
root.mainloop()



