import json
import csv
from produit import *
ventes = []

def charger_ventes():
    global ventes
    try:
        with open('ventes.json', 'r') as file:
            ventes = json.load(file)
    except FileNotFoundError:
        ventes = []

def sauvegarder_ventes():
    with open('ventes.json', 'w') as file:
        json.dump(ventes, file, indent=4)

def enregistrer_vente():
    while True:
        print("=== === === LES INFORMATIONS SUR LA VENTE === === ===")
       
        client = input("Entrez le nom du client: ")
        if client.isalpha():
            break
        else:
            print("Le nom du client ne doit contenir que des lettres.")

    while True:
        choix_recherche = input("Voulez-vous rechercher le produit a vendre par nom ou par ID ? (nom/id): ").lower()
        if choix_recherche in ['nom', 'id']:
            break
        else:
            print("Choix invalide, veuillez entrer 'nom' ou 'id'.")

    produit_trouve = None
    if choix_recherche == 'nom':
        while True:
            nom_produit = input("Entrez le nom du produit: ")
            if nom_produit.isalpha():
                produit_trouve = next((produit for produit in produits if produit['nom'] == nom_produit), None)
                if produit_trouve:
                    break
                else:
                    print("Produit non trouvé.")
            else:
                print("Le nom du produit ne doit contenir que des lettres.")
    else:  # choix_recherche == 'id'
        while True:
            try:
                id_produit = int(input("Entrez l'ID du produit: "))
                produit_trouve = next((produit for produit in produits if produit['id_produit'] == id_produit), None)
                if produit_trouve:
                    break
                else:
                    print("Produit non trouvé.")
            except ValueError:
                print("Veuillez entrer un ID valide.")

    while True:
        try:
            quantite = int(input("Entrez la quantité vendue: "))
            if quantite > 0:
                break
            else:
                print("La quantité doit être un entier positif.")
        except ValueError:
            print("Veuillez entrer un nombre entier.")
            
    date = input("Entrez la date de la vente (YYYY-MM-DD): ")
    notes = input("Entrez les notes pour cette vente (optionnel): ")

    if produit_trouve['quantite'] >= quantite:
        vente = {'client': client, 'produit': produit_trouve['nom'], 'quantite': quantite, 'date': date}
        ventes.append(vente)
        produit_trouve['quantite'] -= quantite
        sauvegarder_ventes()
        sauvegarder_produits()  # Sauvegarder les produits mis à jour
        print("Vente enregistrée avec succès!")
    else:
        print("Quantité insuffisante en stock.")

def afficher_ventes():
    print("=== ==== === AFFICHAGE DE LA VENTE === === =====")
    if not ventes:
        print("Aucune vente enregistrée.")
    else:
        for vente in ventes:
            print(f"Client: {vente['client']}, Produit: {vente['produit']}, Quantité: {vente['quantite']}, Date: {vente['date']}")

def ventes_par_client():
    print("=== === === LES INFORMATIONS DE LA VENTE D'UN CLIENT SPÉCIFIQUE === === ===")
    while True:
        client = input("Entrez le nom du client: ")
        if client.isalpha():
            break
        else:
            print("Le nom du client ne doit contenir que des lettres.")

    ventes_client = [vente for vente in ventes if vente['client'] == client]
    if not ventes_client:
        print("Aucune vente trouvée pour ce client.")
    else:
        for index, vente in enumerate(ventes_client, start=1):
            print(f"{index}. Produit: {vente['produit']}, Quantité: {vente['quantite']}, Date: {vente['date']}")

        choix_suppression = input("Voulez-vous supprimer une de ces ventes ? (oui/non): ").lower()
        if choix_suppression == "oui":
            try:
                numero_vente = int(input("Entrez le numéro de la vente à supprimer: "))
                vente_a_supprimer = ventes_client[numero_vente - 1]
                supprimer_vente(vente_a_supprimer)
                print("*** *** *** VENTE SUPPRIMÉE AVEC SUCCÈS *** *** ***")
            except (IndexError, ValueError):
                print("Numéro de vente invalide.")

def supprimer_vente(vente_a_supprimer):
    global ventes
    ventes = [vente for vente in ventes if vente != vente_a_supprimer]
    sauvegarder_ventes()

def filtrer_ventes_par_date():
    date_debut = input("Entrez la date de début (YYYY-MM-DD): ")
    date_fin = input("Entrez la date de fin (YYYY-MM-DD): ")
    ventes_filtrees = [vente for vente in ventes if date_debut <= vente['date'] <= date_fin]
    if not ventes_filtrees:
        print("Aucune vente trouvée pour cette période.")
    else:
        for vente in ventes_filtrees:
            print(f"Client: {vente['client']}, Produit: {vente['produit']}, Quantité: {vente['quantite']}, Date: {vente['date']}")

def total_ventes_par_client():
    print("=== === === TOTAL DES VENTES PAR CLIENT === === ===")
    client_totaux = {}
    for vente in ventes:
        client = vente['client']
        quantite = vente['quantite']
        if client in client_totaux:
            client_totaux[client] += quantite
        else:
            client_totaux[client] = quantite
    
    for client, total in client_totaux.items():
        print(f"Client: {client}, Total des quantités vendues: {total}")

def exporter_rapports_csv():
    with open('rapport_ventes.csv', 'w', newline='') as csvfile:
        fieldnames = ['client', 'produit', 'quantite', 'date',]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for vente in ventes:
            writer.writerow(vente)
    print("Rapport des ventes exporté avec succès dans 'rapport_ventes.csv'.")

# Charger les ventes au démarrage
charger_ventes()
