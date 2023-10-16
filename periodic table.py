import tkinter as tk

# imports the elements of the periodic table
elements = {
    1: {"name": "Hydrogen", "symbol": "H", "atomic_number": 1, "atomic_mass": 1.008},
    2: {"name": "Helium", "symbol": "He", "atomic_number": 2, "atomic_mass": 4.0026},
    3: {"name": "Lithium", "symbol": "Li", "atomic_number": 3, "atomic_mass": 6.94},
    4: {"name": "Beryllium", "symbol": "Be", "atomic_number": 4, "atomic_mass": 9.0122},
    5: {"name": "Boron", "symbol": "B", "atomic_number": 5, "atomic_mass": 10.81},
    6: {"name": "Carbon", "symbol": "C", "atomic_number": 6, "atomic_mass": 12.01},
    7: {"name": "Nitrogen", "symbol": "N", "atomic_number": 7, "atomic_mass": 14.01},
    8: {"name": "Oxygen", "symbol": "O", "atomic_number": 8, "atomic_mass": 16.00},
    9: {"name": "Fluorine", "symbol": "F", "atomic_number": 9, "atomic_mass": 19.00},
    10: {"name": "Neon", "symbol": "Ne", "atomic_number": 10, "atomic_mass": 20.18},
    11: {"name": "Sodium", "symbol": "Na", "atomic_number": 11, "atomic_mass": 22.99},
    12: {"name": "Magnesium", "symbol": "Mg", "atomic_number": 12, "atomic_mass": 24.31},
    13: {"name": "Aluminum", "symbol": "Al", "atomic_number": 13, "atomic_mass": 26.98},
    14: {"name": "Silicon", "symbol": "Si", "atomic_number": 14, "atomic_mass": 28.09},
    15: {"name": "Phosphorus", "symbol": "P", "atomic_number": 15, "atomic_mass": 30.97},
    16: {"name": "Sulfur", "symbol": "S", "atomic_number": 16, "atomic_mass": 32.07},
    17: {"name": "Chlorine", "symbol": "Cl", "atomic_number": 17, "atomic_mass": 35.45},
    18: {"name": "Argon", "symbol": "Ar", "atomic_number": 18, "atomic_mass": 39.95},
}

def show_element_details(atomic_number):
    if atomic_number in elements:
        element = elements[atomic_number]
        element_details.config(text=f"Name: {element['name']}\nSymbol: {element['symbol']}\nAtomic Number: {element['atomic_number']}\nAtomic Mass: {element['atomic_mass']}")

root = tk.Tk()
root.title("Interactive Periodic Table")

element_details = tk.Label(root, text="", justify="left")
element_details.grid(row=0, column=1)

# Create buttons for the table
for atomic_number in elements.keys():
    button = tk.Button(root, text=str(atomic_number), width=2, height=1, command=lambda n=atomic_number: show_element_details(n))
    button.grid(row=(atomic_number // 18) + 1, column=(atomic_number % 18))

root.mainloop()
