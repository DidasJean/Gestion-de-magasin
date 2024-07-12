from vente import *
from produit import *

def afficher_rapport_ventes():
    print("----- VOICI LE RAPPORT DE TOUTE LES VENTES DE PRODUITS SUR LE MAGASIN ------" )
    for vente in ventes:
        print(f"Client: {vente['client']}, Produit: {vente['produit']}, Quantité: {vente['quantite']}, Date: {vente['date']}")

def generer_rapport_produit():
    print("---- VOICI LE RAPPORT DE TOUT LE PRODUITS EN STOCK ----")
    for produit in produits:
        print(f"Nom: {produit['nom']}, Quantité en stock: {produit['quantite']}")

def generer_rapport_ventes_periode(debut, fin):
    print(f"----- RAPPORT DES VENTES DU {debut.strftime('%Y-%m-%d')} AU {fin.strftime('%Y-%m-%d')} -----")
    for vente in ventes:
        if debut <= vente['date'] <= fin:
            print(f"Client: {vente['client']}, Produit: {vente['produit']}, Quantité: {vente['quantite']}, Date: {vente['date'].strftime('%Y-%m-%d')}")