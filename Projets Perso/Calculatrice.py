import tkinter as tk

def on_click(button_value):
    if button_value == '=':
        calculate()
    else :
        current_text = entry.get()
        new_text = current_text + str(button_value)
        entry.delete(0, tk.END)
        entry.insert(0, new_text)
    
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')
        
# Création de la fenêtre principale
window = tk.Tk()
window.title('Calculatrice')

# Entry pour afficher les chiffres et résultats
entry = tk.Entry(window, width=20, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

# Bouttons pour les chiffres et les opérateurs
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(window, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1
        
# Button clear
tk.Button(window, text="C", width=5, height=2, command= lambda: entry.delete(0, tk.END)).grid(row=row_val, column=col_val)

# Association de la touche Entrée pour le calcul
window.bind('<Return>', lambda event=None: calculate())

# Affichage de la fenêtre
window.mainloop()