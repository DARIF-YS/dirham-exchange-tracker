import pandas as pd
import os

def Transform():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_raw    = os.path.join(current_dir, '..', 'exchange_data', 'raw_taux_change.json')
    path_clean  = os.path.join(current_dir, '..', 'exchange_data', 'clean_taux_change.json')

    # Charger les données brutes depuis un fichier JSON
    df = pd.read_json(path_raw) 

    # Conversion des taux (string avec virgules) en float
    df['taux_achat'] = df['taux_achat'].str.replace(',', '.').astype(float)
    df['taux_vente'] = df['taux_vente'].str.replace(',', '.').astype(float)

    # Extraction de l'unité (quantité de monnaie étrangère) et du nom de la devise
    df[['unite_montant', 'nom_devise']] = df['devise_complete'].str.extract(r'(\d+)\s+(.*)')
    df['unite_montant'] = df['unite_montant'].astype(int)

    # Dictionnaire pour convertir les noms de devises en codes ISO standards
    abr_dict = {
        "EURO": "EUR",
        "DOLLAR U.S.A.": "USD",
        "DOLLAR CANADIEN": "CAD",
        "LIVRE STERLING": "GBP",
        "LIVRE GIBRALTAR": "GIP",
        "FRANC SUISSE": "CHF",
        "RIYAL SAOUDIEN": "SAR",
        "DINAR KOWEITIEN": "KWD",
        "DIRHAM E.A.U.": "AED",
        "RIYAL QATARI": "QAR",
        "DINAR BAHREINI": "BHD",
        "YENS JAPONAIS": "JPY",
        "RIYAL OMANI": "OMR"
    }

    # Ajout d'une colonne avec l'abréviation de la devise
    df['abr_devise'] = df['nom_devise'].map(abr_dict)

    # Liste des devises à traiter
    abr_devises = ['AED', 'BHD', 'CAD', 'CHF', 'EUR', 'GBP', 'GIP', 'JPY', 'KWD', 'OMR', 'QAR', 'SAR', 'USD']

    # Initialisation du DataFrame final après interpolation
    df_combined = pd.DataFrame()

    # Pour chaque devise, trier par date, interpoler les valeurs manquantes, et concaténer dans un seul DataFrame
    for abr_devise in abr_devises:
        sub_df = df[df["abr_devise"] == abr_devise]
        sub_df = sub_df.sort_values(by='date')
        sub_df = sub_df.set_index('date')
        sub_df = sub_df.interpolate(method='time', limit_direction='both')
        df_combined = pd.concat([df_combined, sub_df])

    # Conversion des taux pour 1 unité (ex. de 100 JPY à 1 JPY)
    df_combined['taux_achat'] = df_combined['taux_achat'] / df_combined['unite_montant']
    df_combined['taux_vente'] = df_combined['taux_vente'] / df_combined['unite_montant']

    # Nettoyage : suppression des colonnes non nécessaires
    df_combined.drop(["devise_complete", "unite_montant"], axis=1, inplace=True)

    # Calcul du taux moyen et de l'écart (spread)
    df_combined['taux_moyen'] = (df_combined['taux_achat'] + df_combined['taux_vente']) / 2
    df_combined['ecart']      = df_combined['taux_vente'] - df_combined['taux_achat']

    # Réinitialisation de l’index et ajout d’un identifiant unique
    df_combined       = df_combined.reset_index()
    df_combined['id'] = range(1, len(df_combined) + 1)

    # Réorganisation des colonnes
    df_combined = df_combined[['id', 'date', 'nom_devise', 'abr_devise', 'taux_achat', 'taux_vente', 'ecart', 'taux_moyen']]

    # Sauvegarde des données nettoyées dans un fichier JSON
    df_combined.to_json(path_clean, orient="records", force_ascii=False, indent=2)
