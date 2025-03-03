ChatCloser – Identifie les conversations qui aboutissent 
#### le nom du chat est modifiable

ChatCloser est un projet visant à analyser et classifier automatiquement des conversations entre vendeurs et acheteurs afin de déterminer si une vente est conclue ou non.


Fonctionnalités
Classification des Chats : Un modèle NLP (basé sur un pipeline TF-IDF + Logistic Regression ou un modèle avancé) identifie automatiquement si la conversation est positive (vente aboutie) ou negative (vente non conclue).
API REST : Déploiement via FastAPI pour consommer le modèle. Un endpoint /predict permet d’envoyer les messages du chat et de recevoir un label en sortie.

Structure du Projet
data/ : Contient les fichiers JSON de conversations.
eda/ : Scripts d’Exploratory Data Analysis (analyse et visualisation des données).
models/ : Code d’entraînement du modèle et fichiers sauvegardés (p. ex. chat_classifier.pkl).
api/ : Code FastAPI (fichier main.py) pour l’API de prédiction.

