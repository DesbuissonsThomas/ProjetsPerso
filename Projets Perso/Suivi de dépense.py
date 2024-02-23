import json
from datetime import datetime

def load_expenses():
    try:
        with open('expenses.json', 'r') as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    return expenses

def save_expenses(expenses):
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file)

def add_expense(category, amount, date=None):
    expenses = load_expenses()
    new_expense = {'category': category, 'amount': amount, 'date': date or str(datetime.now())}
    expenses.append(new_expense)
    save_expenses(expenses)

def view_expenses(start_date, end_date):
    expenses = load_expenses()

    if start_date and end_date:
        filtered_expenses = [expense for expense in expenses if start_date <= expense['date'] <= end_date]
        print(f"Total des dépenses pour la période {start_date} à {end_date}:")
    else:
        filtered_expenses = expenses
        print("Total des dépenses totales :")

    total_amount = sum(expense['amount'] for expense in filtered_expenses)
    
    print(f"Montant total: {total_amount}")

    for expense in filtered_expenses:
        print(f"{expense['date']} | Catégorie: {expense['category']} | Montant: {expense['amount']}")

def total_spent():
    expenses = load_expenses()
    total_amount = sum(expense['amount'] for expense in expenses)
    print(f"Montant total dépensé jusqu'à présent : {total_amount}")

# Ajouter d'autres fonctionnalités selon vos besoins.

if __name__ == "__main__":
    while True:
        print("\n=== Suivi de Dépenses Quotidien ===")
        print("1. Ajouter une dépense")
        print("2. Visualiser les dépenses pour une période")
        print("3. Visualiser les dépenses totales")
        print("4. Afficher le montant total dépensé jusqu'à présent")
        print("5. Quitter")

        choice = input("Choisissez une option (1/2/3/4/5): ")

        if choice == '1':
            category = input("Entrez la catégorie de la dépense : ")
            amount = float(input("Entrez le montant de la dépense : "))
            date = input("Entrez la date de la dépense (format YYYY-MM-DD) ou appuyez sur Entrée pour la date actuelle : ")
            add_expense(category, amount, date)
        elif choice == '2':
            start_date = input("Entrez la date de début (format YYYY-MM-DD) : ")
            end_date = input("Entrez la date de fin (format YYYY-MM-DD) : ")
            view_expenses(start_date, end_date)
        elif choice == '3':
            view_expenses(None, None)  # Visualiser les dépenses totales
        elif choice == '4':
            total_spent()
        elif choice == '5':
            break
        else:
            print("Option non valide. Veuillez réessayer.")
