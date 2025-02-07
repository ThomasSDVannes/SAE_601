# Projet Étudiant : Analyse des Salaires en Data Science

## Présentation du projet

**Nom des membres du projet** :  
- Thomas Defoulounoux  
- Lukas Le Plaire  

Ce projet fait partie de la SAE 6-01-VCOD : **Développement et test d'un outil décisionnel** dans le cadre de notre formation en **BUT Science des Données (SD)**, **3ème année**.

## Description

L'objectif de ce projet est de développer un outil interactif permettant l'analyse et la visualisation des salaires dans le domaine de la Data Science. Nous avons utilisé des données provenant de plusieurs sources pour étudier les tendances salariales en fonction de critères tels que le niveau d'expérience, la taille de l'entreprise, le rôle et bien d'autres variables. Ce projet se concentre sur l'exploitation et la visualisation des données à travers différentes méthodes graphiques, telles que les graphiques interactifs avec **Plotly** et **Streamlit**.

L'outil permet également d'analyser des informations clés comme les salaires médians par expérience et taille d'entreprise, ainsi que l'impact du télétravail sur les salaires selon le pays.

## Fonctionnalités

- Visualisation des salaires par titre de poste et taille d'entreprise.
- Exploration de la distribution des salaires en fonction du niveau d'expérience.
- Analyse des tendances salariales par catégorie (expérience, type d'emploi, titre de poste, etc.).
- Visualisation des corrélations entre les variables numériques.
- Exploration interactive des variations salariales pour les postes les plus courants.
- Analyse de l'impact du télétravail sur les salaires selon les pays.
- Filtres dynamiques permettant de sélectionner une plage de salaire et d'analyser les données en fonction de différents critères.

## Technologies utilisées

- **Python** (avec les librairies pandas, numpy, matplotlib, seaborn, plotly, streamlit)
- **Streamlit** : pour la création d'une interface interactive.
- **Plotly** : pour les visualisations interactives des données.
- **pandas** et **numpy** : pour la manipulation et l'analyse des données.

## Installation

Pour installer toutes les dépendances nécessaires, vous pouvez créer un environnement virtuel et installer les librairies avec la commande suivante :

**Anaconda Prompt**

conda create -n projet python pandas numpy matplotlib jupyterlab kagglehub seaborn streamlit plotly
conda activate projet
streamlit run app.py