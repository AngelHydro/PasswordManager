import os

# Structure de données pour stocker les informations
passwords_db = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fonction pour afficher le menu
def display_menu():
    print("Menu:")
    print("1. Rechercher un site")
    print("2. Créer un nouveau site")
    print("3. Modifier un site existant")
    print("4. Supprimer un site")
    print("5. Quitter")

# Fonction pour rechercher un site
def search_site():
    site = input("Entrez le nom du site: ")
    if site in passwords_db: # Vérifie si le site existe dans la base de données
        print(f"Site: {site}")
        print(f"Nom d'utilisateur: {passwords_db[site]['username']}")
        print(f"Mot de passe: {passwords_db[site]['password']}")
    else: # Si le site n'existe pas dans la base de données, affiche un message d'erreur
        print("Ce site n'existe pas.")

# Fonction pour créer un nouveau site
def create_site():
    site = input("Entrez le nom du site: ")
    username = input("Entrez votre nom d'utilisateur: ")
    password = input("Entrez votre mot de passe: ")
    passwords_db[site] = {'username': username, 'password': password}
    print(f"Site {site} créé avec succès.")

# Fonction pour modifier un site existant
def modify_site():
    site = input("Entrez le nom du site à modifier: ")
    if site in passwords_db: # Vérifie si le site existe dans la base de données
        print(f"Ancien nom d'utilisateur: {passwords_db[site]['username']}")
        print(f"Ancien mot de passe: {passwords_db[site]['password']}")
        username = input("Entrez le nouveau nom d'utilisateur (laisser vide pour ne pas changer): ")
        password = input("Entrez le nouveau mot de passe (laisser vide pour ne pas changer): ")
        if username:
            passwords_db[site]['username'] = username
        if password:
            passwords_db[site]['password'] = password
        print(f"Site {site} modifié avec succès.")
    else: # Si le site n'existe pas dans la base de données, affiche un message d'erreur
        print("Ce site n'existe pas.")

# Fonction pour supprimer un site
def delete_site():
    site = input("Entrez le nom du site à supprimer: ")
    if site in passwords_db: # Vérifie si le site existe dans la base de données
        del passwords_db[site]
        print(f"Site {site} et ses informations supprimées avec succès.")
    else: # Si le site n'existe pas dans la base de données, affiche un message d'erreur
        print("Ce site n'existe pas.")

# Fonction principale pour exécuter le programme
def main():
    # Affiche le menu et gère les choix de l'utilisateur
    while True:
        clear_screen()
        display_menu()
        choice = input("Choisissez une option (1-5): ")
        if choice == '1':
            search_site()
        elif choice == '2':
            create_site()
        elif choice == '3':
            modify_site()
        elif choice == '4':
            delete_site()
        elif choice == '5':
            print("Au revoir!")
            break
        else: # Si l'utilisateur saisit une option invalide, affiche un message d'erreur
            print("Option invalide. Veuillez réessayer.")
        input("Appuyez sur Entrée pour continuer...")

# Point d'entrée du programme
if __name__ == "__main__":
    main()