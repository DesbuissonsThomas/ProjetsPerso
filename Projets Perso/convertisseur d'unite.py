import tkinter as tk
from tkinter import ttk

# Fonctions de conversion
def convert_length(value, from_unit, to_unit):
    length_units = {'m': 1, 'km': 0.001, 'cm': 100, 'mm': 1000, 'mi': 0.000621371, 'yd': 1.09361, 'ft': 3.28084, 'in': 39.3701}
    converted_value = value * length_units[from_unit] / length_units[to_unit]
    return converted_value

def convert_weight(value, from_unit, to_unit):
    weight_units = {'kg': 1, 'g': 1000, 'mg': 1e6, 'lb': 2.20462, 'oz': 35.274}
    converted_value = value * weight_units[from_unit] / weight_units[to_unit]
    return converted_value

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return (value * 9/5) + 32
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    elif from_unit == 'F' and to_unit == 'K':
        return (value + 459.67) * 5/9
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (value * 9/5) - 459.67
    else:
        return value  # Aucune conversion nécessaire pour les mêmes unités

def convert_volume(value, from_unit, to_unit):
    volume_units = {'l': 1, 'ml': 1000, 'gal': 0.264172, 'qt': 1.05669, 'pt': 2.11338, 'cup': 4.22675, 'fl oz': 33.814}
    converted_value = value * volume_units[from_unit] / volume_units[to_unit]
    return converted_value

# Classe de l'application
class UnitConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertisseur d'Unités")
        self.root.geometry("400x250")

        # Configuration du style des widgets
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TLabel", background="#f0f0f0")
        self.style.configure("TButton", background="#4caf50", foreground="#ffffff")

        # Cadre principal
        self.main_frame = ttk.Frame(root, padding=(20, 10))
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Widgets de l'interface utilisateur
        self.value_label = ttk.Label(self.main_frame, text="Valeur:", style="TLabel")
        self.value_entry = ttk.Entry(self.main_frame, font=('Arial', 12))
        self.value_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.value_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.from_label = ttk.Label(self.main_frame, text="De:", style="TLabel")
        self.from_unit_combobox = ttk.Combobox(self.main_frame, font=('Arial', 12))
        self.from_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.from_unit_combobox.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.to_label = ttk.Label(self.main_frame, text="À:", style="TLabel")
        self.to_unit_combobox = ttk.Combobox(self.main_frame, font=('Arial', 12))
        self.to_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.to_unit_combobox.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.result_label = ttk.Label(self.main_frame, text="Résultat:", style="TLabel")
        self.result_value = tk.StringVar()
        self.result_entry = ttk.Entry(self.main_frame, textvariable=self.result_value, font=('Arial', 12), state='readonly')
        self.result_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.result_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        self.convert_button = ttk.Button(self.main_frame, text="Convertir", command=self.convert, style="TButton")
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=15)

        # Initialisation des listes déroulantes
        self.init_unit_comboboxes()

    def init_unit_comboboxes(self):
        length_units = ['m', 'km', 'cm', 'mm', 'mi', 'yd', 'ft', 'in']
        self.from_unit_combobox['values'] = length_units
        self.to_unit_combobox['values'] = length_units

    def convert(self):
        try:
            # Récupération des valeurs
            value = float(self.value_entry.get())
            from_unit = self.from_unit_combobox.get()
            to_unit = self.to_unit_combobox.get()

            # Vérification si les unités sont identiques
            if from_unit == to_unit:
                result = value
            # Sélection de la fonction de conversion en fonction de l'unité
            elif from_unit in {'m', 'km', 'cm', 'mm', 'mi', 'yd', 'ft', 'in'}:
                result = convert_length(value, from_unit, to_unit)
            elif from_unit in {'kg', 'g', 'mg', 'lb', 'oz'}:
                result = convert_weight(value, from_unit, to_unit)
            elif from_unit in {'C', 'F', 'K'}:
                result = convert_temperature(value, from_unit, to_unit)
            elif from_unit in {'l', 'ml', 'gal', 'qt', 'pt', 'cup', 'fl oz'}:
                result = convert_volume(value, from_unit, to_unit)
            else:
                raise ValueError("Unit not supported")

            # Affichage du résultat
            self.result_value.set(result)
        except ValueError:
            # Gestion de l'erreur en cas de saisie incorrecte
            self.result_value.set("Erreur de conversion")

# Exécution de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterApp(root)
