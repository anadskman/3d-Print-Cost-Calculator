import tkinter as tk
from tkinter import ttk

def calculate_material_cost(density, diameter, length, price_per_kg):
    material_cost = (density * 3.14159 * (diameter/2)**2 * length) * price_per_kg / 1000
    return material_cost

def calculate_labor_cost(time, hourly_rate):
    labor_cost = time * hourly_rate
    return labor_cost

def calculate_final_price(material_cost, labor_cost, markup):
    final_price = (material_cost + labor_cost) * (1 + markup/100)
    return final_price

def calculate_cost():
    material_type = material_var.get()
    if material_type == "Custom":
        density = float(density_entry.get())
    else:
        densities = {
            "ABS": 1.05,
            "PLA": 1.27,
            "PETG": 1.25,
            "PETT": 1.45,
            "HIPS": 1.04,
            "TPU": 1.30,
            "abs": 1.05,
            "pla": 1.27,
            "petg": 1.25,
            "pett": 1.45,
            "hips": 1.04,
            "tpu": 1.30
        }
        density = densities[material_type]

    diameter = float(diameter_entry.get())
    length = float(length_entry.get())
    price_per_kg = float(price_per_kg_entry.get())

    time = float(time_entry.get())
    hourly_rate = float(hourly_rate_entry.get())

    markup = float(markup_entry.get())

    material_cost = calculate_material_cost(density, diameter, length, price_per_kg)
    labor_cost = calculate_labor_cost(time, hourly_rate)
    final_price = calculate_final_price(material_cost, labor_cost, markup)

    material_cost_label.config(text="Material cost: €{:.2f}".format(material_cost))
    labor_cost_label.config(text="Labor cost: €{:.2f}".format(labor_cost))
    final_price_label.config(text="Final price: €{:.2f}".format(final_price))

root = tk.Tk()
root.title("3D Printing Cost Calculator")

frame = ttk.LabelFrame(root, text="Input parameters")
frame.grid(column=0, row=0, padx=10, pady=10, sticky="w")

material_var = tk.StringVar(frame)
material_var.set("PLA")

material_options = ["ABS", "PLA", "PETG", "PETT", "HIPS", "TPU", "Custom"]
material_option_menu = ttk.OptionMenu(frame, material_var, *material_options)
material_option_menu.grid(column=0, row=0, padx=5, pady=5, sticky="w")

density_label = ttk.Label(frame, text="Material density (g/cm³):")
density_label.grid(column=0, row=1, padx=5, pady=5, sticky="w")
density_entry = ttk.Entry(frame,width=10)
density_entry.grid(column=1, row=1, padx=5, pady=5, sticky="w")

diameter_label = ttk.Label(frame, text="Filament diameter (mm):")
diameter_label.grid(column=0, row=2, padx=5, pady=5, sticky="w")
diameter_entry = ttk.Entry(frame,width=10)
diameter_entry.grid(column=1, row=2, padx=5, pady=5, sticky="w")

length_label = ttk.Label(frame, text="Filament length (m):")
length_label.grid(column=0, row=3, padx=5, pady=5, sticky="w")
length_entry = ttk.Entry(frame,width=10)
length_entry.grid(column=1, row=3, padx=5, pady=5, sticky="w")

price_per_kg_label = ttk.Label(frame, text="Material price per kilogram (€):")
price_per_kg_label.grid(column=0, row=4, padx=5, pady=5, sticky="w")
price_per_kg_entry = ttk.Entry(frame,width=10)
price_per_kg_entry.grid(column=1, row=4, padx=5, pady=5, sticky="w")

time_label = ttk.Label(frame, text="Printing time (hours):")
time_label.grid(column=0, row=5, padx=5, pady=5, sticky="w")
time_entry = ttk.Entry(frame,width=10)
time_entry.grid(column=1, row=5, padx=5, pady=5, sticky="w")

hourly_rate_label = ttk.Label(frame, text="Hourly rate (€):")
hourly_rate_label.grid(column=0, row=6, padx=5, pady=5, sticky="w")
hourly_rate_entry = ttk.Entry(frame,width=10)
hourly_rate_entry.grid(column=1, row=6, padx=5, pady=5, sticky="w")

markup_label = ttk.Label(frame, text="Markup percentage (%):")
markup_label.grid(column=0, row=7, padx=5, pady=5, sticky="w")
markup_entry = ttk.Entry(frame,width=10)
markup_entry.grid(column=1, row=7, padx=5, pady=5, sticky="w")

material_cost_label = ttk.Label(root, text="Material cost: €0.00")
material_cost_label.grid(column=0, row=1, padx=5, pady=5, sticky="w")

labor_cost_label = ttk.Label(root, text="Labor cost: €0.00")
labor_cost_label.grid(column=0, row=2, padx=5, pady=5, sticky="w")

final_price_label = ttk.Label(root, text="Final price: €0.00")
final_price_label.grid(column=0, row=3, padx=5, pady=5, sticky="w")

calculate_button = ttk.Button(root, text="Calculate", command=calculate_cost)
calculate_button.grid(column=0, row=4, padx=5, pady=5, sticky="w")

root.mainloop()