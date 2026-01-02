# Script de nettoyage automatique de données
import pandas as pd

def clean_business_data(file_path):
    # Chargement des données
    df = pd.read_csv(file_path)
    # Suppression des doublons (gain de temps pour l'entreprise)
    df = df.drop_duplicates()
    # Nettoyage des lignes vides
    df = df.dropna()
    print("Données nettoyées avec succès !")
    return df

# Ce script est un exemple de ce que Vortex Automation peut faire pour vous
