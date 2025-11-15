## Suivi des taux de change du Dirham Marocain (MAD)

Projet de scraping, transformation et visualisation des taux de change du dirham marocain (MAD) face aux principales devises étrangères.  
Les données sont extraites quotidiennement depuis le site officiel de Bank Al-Maghrib.

### 1. Objectif
Mettre en place une pipeline ETL automatisée pour collecter, nettoyer, stocker et analyser les taux de change quotidiens.

### 2. Stack technique
- Selenium, Pandas – extraction et transformation  
- Airflow – orchestration de la pipeline  
- PostgreSQL (Aiven Cloud) – stockage des données  
- Looker Studio – visualisation interactive  

### 3. Résultats
- Suivi des taux d’achat, de vente et du taux moyen  
- Analyse temporelle et détection des écarts  
- Tableau de bord connecté à la base PostgreSQL  

Exemples de visualisations issues du tableau de bord :
#### a. Comparaison globale des taux de change
<img width="1006" height="1061" alt="img1" src="https://github.com/user-attachments/assets/6781a473-de95-466f-b037-9078cde33fec" />

#### b. Analyse temporelle des taux de change
<img width="1249" height="897" alt="img2" src="https://github.com/user-attachments/assets/62b61ece-f550-4cdb-9906-4eeb26a7de7a" />
