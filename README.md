# Suivi des taux de change du Dirham Marocain (MAD)

[Voir la démo](https://github.com/user-attachments/assets/e90c35ab-4298-4cbf-808a-fbda0b0fc157)

Projet de scraping, transformation et visualisation des taux de change du dirham marocain (MAD) face aux principales devises étrangères.  
Les données sont extraites quotidiennement depuis le site officiel de Bank Al-Maghrib.

## Objectif
Mettre en place une pipeline ETL automatisée pour collecter, nettoyer, stocker et analyser les taux de change quotidiens.

## Stack technique
- Python, Pandas – extraction et transformation  
- Airflow – orchestration de la pipeline  
- PostgreSQL (Aiven Cloud) – stockage des données  
- Looker Studio – visualisation interactive  

## Résultats
- Suivi des taux d’achat, de vente et du taux moyen  
- Analyse temporelle et détection des écarts  
- Tableau de bord dynamique connecté à la base PostgreSQL
