import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

def Load():
    # Charger les variables d'environnement depuis le fichier .env
    load_dotenv()

    # Lire les paramètres de connexion depuis les variables d'environnement
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")
    host     = os.getenv("DB_HOST")
    port     = os.getenv("DB_PORT")
    database = os.getenv("DB_NAME")

    # Construire l'URL de connexion PostgreSQL
    DATABASE_URL = f"postgresql://{username}:{password}@{host}:{port}/{database}"

    # Créer le moteur SQLAlchemy
    engine = create_engine(DATABASE_URL)

    # Charger les données depuis le fichier JSON nettoyé
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_clean  = os.path.join(current_dir, '..', 'exchange_data', 'clean_taux_change.json')

    df = pd.read_json(path_clean)

    # Arrondir les valeurs numériques
    df = df.round(6)

    # S'assurer que la colonne 'date' est bien au format date
    #df['date'] = pd.to_datetime(df['date']).dt.date
    df['date'] = pd.to_datetime(df['date']).dt.date

    # Exporter vers PostgreSQL (remplacer si la table existe déjà)
    df.to_sql("final_taux_change", con=engine, if_exists="replace", index=False)

    print("✅ Données importées avec succès dans PostgreSQL.")
