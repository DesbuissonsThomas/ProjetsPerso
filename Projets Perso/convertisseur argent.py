import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertisseur de Devises")
        self.root.geometry("600x400")

        self.currency_rates = CurrencyRates()
        self.base_currency = 'USD'
        self.currencies = list(self.currency_rates.get_rates(self.base_currency).keys())

        self.from_currency_var = tk.StringVar(value=self.base_currency)
        self.to_currency_var = tk.StringVar(value=self.currencies[0])
        self.amount_var = tk.DoubleVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.root, padding=(20, 10))
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        from_currency_label = ttk.Label(main_frame, text="De la devise:", font=('Arial', 14))
        from_currency_combobox = ttk.Combobox(main_frame, textvariable=self.from_currency_var, values=self.currencies, font=('Arial', 14), state='readonly')

        to_currency_label = ttk.Label(main_frame, text="À la devise:", font=('Arial', 14))
        to_currency_combobox = ttk.Combobox(main_frame, textvariable=self.to_currency_var, values=self.currencies, font=('Arial', 14), state='readonly')

        amount_label = ttk.Label(main_frame, text="Montant:", font=('Arial', 14))
        amount_entry = ttk.Entry(main_frame, textvariable=self.amount_var, font=('Arial', 14))

        convert_button = ttk.Button(main_frame, text="Convertir", command=self.convert, style="TButton")

        result_label = ttk.Label(main_frame, text="Résultat:", font=('Arial', 14))
        result_entry = ttk.Entry(main_frame, textvariable=self.result_var, font=('Arial', 14), state='readonly', width=40)  # Ajout de la largeur

        # Ajout d'une barre de défilement
        result_scrollbar = ttk.Scrollbar(main_frame, orient='horizontal', command=result_entry.xview)
        result_entry.config(xscrollcommand=result_scrollbar.set)

        from_currency_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        from_currency_combobox.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        to_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        to_currency_combobox.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        amount_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        amount_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        convert_button.grid(row=3, column=0, columnspan=2, pady=15)
        result_label.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
        result_entry.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)
        result_scrollbar.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)

    def convert(self):
        try:
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()
            amount = self.amount_var.get()

            rate = self.currency_rates.get_rate(from_currency, to_currency)
            converted_amount = round(amount * rate, 2)

            result_text = f"{amount} {from_currency} équivaut à {converted_amount} {to_currency}"
            self.result_var.set(result_text)
        except Exception as e:
            self.result_var.set("Erreur de conversion")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
