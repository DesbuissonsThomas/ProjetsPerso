import random
import string

# Saisie des préférences utilisateur : longueur du mdp, maj ou minuscules, chiffres, caractères spéciaux
longueur = int(input("Entrez la longueur du mot de passe : "))
majuscules = input("Inculure des lettres majuscules ? (oui/non) ").lower() == 'oui'
nombres = input("Inculure des nombres ? (oui/non) ").lower() == 'oui'
specials_caracteres = input("Inculure des caractères spéciaux ? (oui/non) ").lower() == 'oui'

#Génération  du mdp : créer une liste de caractères en fonctions des préférences de l'utilisateur
characters = string.ascii_lowercase
if majuscules:
    characters += string.ascii_uppercase
if nombres:
    characters += string.digits
if specials_caracteres:
    characters += string.punctuation

password = "".join(random.choice(characters) for _ in range(longueur))
print("Mot de passe généré :", password)

# Boucle du programme
while True:
    generate_another = input('Voulez-vous générer un autre mot de passe ? (oui/non)').lower()
    if generate_another == 'non':
        print("Fin du programme")
        break
    elif generate_another == "oui":
        password = "".join(random.choice(characters) for _ in range(longueur))
        print("Mot de passe généré :", password)
    else:
        print('Veuillez répondre par "oui" ou par "non"')