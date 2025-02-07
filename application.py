"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

### 1. Importation des librairies et chargement des données
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

df_data = pd.read_csv('ds_salaries.csv', sep=',', na_values='?')

### 2. Exploration visuelle des données
# Afficher un titre avec Streamlit
st.title("📊 Visualisation des Salaires en Data Science")

# Visualisation des salaires par titre de poste et taille d'entreprise
fig = px.bar(df_data, x='job_title', y='salary_in_usd', color='company_size',
             title="Répartition des salaires en fonction du poste et de la taille de l'entreprise")
st.plotly_chart(fig)

# Ajout d'une description
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")

# Afficher un aperçu des données si l'utilisateur choisit
if st.checkbox("Afficher un aperçu des données"):
    st.write(df_data.head(5))

# Affichage des statistiques générales avec describe() de pandas
st.subheader("📌 Statistiques générales")
st.write(df_data.describe())

### 3. Distribution des salaires en France par rôle et niveau d'expérience, utilisant px.box et st.plotly_chart
st.subheader("📈 Distribution des salaires en France")

# Boxplot de la distribution des salaires en fonction du niveau d'expérience
fig = px.box(df_data, x='experience_level', y='salary_in_usd',
             title="Distribution des salaires par niveau d'expérience")
st.plotly_chart(fig)

st.markdown("On peut observer que la distribution des salaires est cohérente, avec les salaires les plus faibles pour les poste en 'Entry level' tandis que les salaires les plus élevés sont pour les postes 'Expert'.")
st.markdown("En revanche, on remarque que le salaire maximum des postes 'Expert' à 416K dollars est inférieur aux salaires maximum des postes 'Senior' à 424K dollars et surtout des postes 'Mid range' à 450K dollars.")

# Boxplot de la distribution des salaires par titre de poste
fig2 = px.box(df_data, x='job_title', y='salary_in_usd',
              title="Distribution des salaires par titre de poste")
st.plotly_chart(fig2)

st.markdown("Avec cette distribution des salaires par type de poste on peut remarquer que certains postes offrent de meilleures possibilités d'évolutions que d'autres. Par exemple, le poste de 'Data Analytics Lead' possède le plus grand écart entre son salire le plus faible et le plus élevé. Tandis que le poste de 'Data DevOps engineer' n'a aucune fluctuation de salaire.")
st.markdown("En revanche, le cas du poste de 'Date DevOps Engineer' peut être lié au nombre d'individus de composant cette variable.")

### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisissant une des catégories : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 

st.subheader("Analyse des tendances de salaires")

option = st.selectbox(
    "Choisissez une catégorie pour analyser les salaires",
    ('experience_level', 'employment_type', 'job_title', 'company_location')
)
st.write("Vous avez sélectionné :", option)

# Calcul du salaire moyen par catégorie
fig3 = px.histogram(df_data, x=option, y='salary_in_usd', 
              title=f"Salaire moyen par {option}",
             histfunc='avg',
              labels={option: option.capitalize(), 'salary_in_usd': 'Salaire moyen (USD)'})
st.plotly_chart(fig3)

st.markdown("L'analyse de la catégorie 'Experience_level' nous confirme que plus le poste nécessite d'expérience plus le salaire est élevé.")
st.markdown("L'analyse de la catégorie 'Employment_type' nous montre que plus le poste est proche d'un temps plein plus le salaire est élevé. Un emploi en temps partiel étant le moins bien rémunéré.")
st.markdown("L'analyse de la catégorie 'Job_title' nous montre la rémunération pour chacuns des postes listés dans le jeu de données. Dans notre cas, le poste de 'Data Science Tech Lead' est le poste le mieux rémunéré avec une moyenne à 375K dollars.")
st.markdown("L'analyse de la catégorie 'Company_location' nous montre les pays ou la rémunération (en USD) est la plus élevée. Le salaire moyen le plus élevé est à Israël pour un montant de 271.5K dollars.")

### 5. Corrélation entre variables
# Sélectionner uniquement les colonnes numériques pour la corrélation
numeric_cols = df_data.select_dtypes(include=np.number).columns

# Calcul de la matrice de corrélation
corr_matrix = df_data[numeric_cols].corr()

# Affichage du heatmap avec sns.heatmap
st.subheader("🔗 Corrélations entre variables numériques")
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
st.pyplot(plt)

st.markdown("Avec cette heatmap nous pouvons remarquer que le salaire est fortement corrélé à l'année, pouvant s'expliquer par l'inflation par exemple.")
st.markdown("En revanche, le taux de télétravail à une corrélation négative avec l'année. Cela s'explique en très grande partie par le fait que le jeu de données commence en 2020, l'année du covid pendant laquelle la quasi totalité de la population était en télétravail.")

### 6. Analyse interactive des variations de salaire
# Une évolution des salaires pour les 10 postes les plus courants
top_job_titles = df_data['job_title'].value_counts().head(10).index
df_top_jobs = df_data[df_data['job_title'].isin(top_job_titles)]

# Calcul du salaire moyen par année pour les 10 postes les plus courants
salary_by_job = df_top_jobs.groupby(['job_title', 'work_year'])['salary_in_usd'].mean().reset_index()


# Utilisation de px.line pour afficher l'évolution des salaires
fig4 = px.line(salary_by_job, x='work_year', y='salary_in_usd', color='job_title',
              title="Évolution des salaires pour les 10 postes les plus courants")
st.plotly_chart(fig4)

st.markdown("Avec ce graphique représentant les salaires des 10 postes les plus courant on peut remarquer que certains postes n'apparaissent qu'en 2021 ou en 2022. Nous pouvons également remarquer que pour 2/3 des postes présent dès 2020 les salaires diminuent fortement. En 2023, aucuns des 10 postes les plus courant ont un salaire inférieur à 110K dollars")

### 7. Salaire médian par expérience et taille d'entreprise
# Calcul du salaire médian par niveau d'expérience et taille d'entreprise
salary_median = df_data.groupby(['experience_level', 'company_size'])['salary_in_usd'].median().reset_index()

# Affichage d'un bar chart des salaires médians
fig5 = px.bar(salary_median, x='experience_level', y='salary_in_usd', color='company_size',
              title="Salaire médian par niveau d'expérience et taille d'entreprise",
              labels={'salary_in_usd': 'Salaire médian (USD)'}, barmode="group")
st.plotly_chart(fig5)

st.markdown("Avec ce barplot des salaires médian par niveau d'expérience et de taille d'entreprise, nous pouvons remarquer que les entreprises de taille moyenne payent mieux que les plus grandes entreprises, sauf pour les poste 'Senior' pour lesquels le salaires est équivalent")
st.markdown("On peut également remarquer que les petites entreprises payent moins que les autres, sauf pour les postes 'Expert' pour lesquels les salaires sont proches de ceux des entreprises de taille moyenne et surout bien plus élevés que pour les plus grandes entreprises.")

### 8. Ajout de filtres dynamiques
st.subheader("🎛️ Filtrer les données par salaire")

# Sélection d'une plage de salaire avec un slider
min_salary, max_salary = st.slider("Sélectionnez la plage de salaire (USD)",
                                  int(df_data["salary_in_usd"].min()),
                                  int(df_data["salary_in_usd"].max()),
                                  (int(df_data["salary_in_usd"].min()), int(df_data["salary_in_usd"].max())))

st.markdown("Création d'un filtre de salaire sous forme de d'échelle avec un minimum et un maximum")

# Filtrage des données
filtered_data = df_data[(df_data["salary_in_usd"] >= min_salary) & (df_data["salary_in_usd"] <= max_salary)]
st.write(f"Nombre de postes correspondant à cette plage de salaire : {filtered_data.shape[0]}")
st.write(filtered_data.head())

st.markdown("Affichage d'un tableau composé des lignes du jeu de données dont le salaire est compris entre le minimum et le maximum du filtre présent juste au dessus.")

### 9. Impact du télétravail sur le salaire selon le pays
st.subheader("🏡 Impact du télétravail sur les salaires")
df_data['remote_ratio']= df_data['remote_ratio'].astype(str)
salary_country = df_data.groupby(['company_location', 'remote_ratio'])['salary_in_usd'].sum().reset_index()

# Visualisation des salaires en fonction du type de travail (remote_ratio) et du pays
fig6 = px.bar(salary_country, x="company_location", y="salary_in_usd", color="remote_ratio",
              title="Impact du télétravail sur le salaire selon le pays",
              labels={"remote_ratio": "Ratio de télétravail", "salary_in_usd": "Salaire en USD"}, barmode="group")
st.plotly_chart(fig6)

st.markdown("Avec ce barplot on peut visualiser le montant total des salaires versés aux employés, et ce par pays, en fonction du télétravail, soit 100% télétravail, 50% télétravail, et 0% télétravail.")
st.markdown("Avec les résultats obtenus on peut donc en déduire que la plupart des données présentes dans ce jeu de données proviennent des États-Unis car le montant total des salaires versés est à environ 250 millions de dollars pour les personnes en 0% télétravail, 200 millions de dollars pour les personnes en 100% télétravail, mais 'seulement' 5 millions de dollars pour les personnes en 50% télétravail. On peut donc en déduire que peu de personnes sont en 50% télétravail aux États-Unis.")

### 10. Filtrage avancé des données avec deux sélections
st.subheader("🎯 Filtrage avancé des données")

# Sélection des niveaux d'expérience
experience_options = df_data["experience_level"].unique()
selected_experience = st.multiselect("Sélectionnez le niveau d'expérience", experience_options, default=experience_options)

# Sélection des tailles d'entreprise
company_size_options = df_data["company_size"].unique()
selected_company_size = st.multiselect("Sélectionnez la taille d'entreprise", company_size_options, default=company_size_options)

# Filtrage des données en fonction des choix
filtered_advanced_data = df_data[(df_data["experience_level"].isin(selected_experience)) &
                                 (df_data["company_size"].isin(selected_company_size))]
st.write(f"Nombre de postes après filtrage : {filtered_advanced_data.shape[0]}")
st.write(filtered_advanced_data.head())

st.markdown("Ici nous réalisons un filtrage avancé des données. On laisse le choix du filtrage sur la variable 'experience_level', et la variable 'company_size'. Nous le réalisons avec 2 menus de sélection multiple permettant le choix de plusieurs valeurs de chacunes des 2 variables.")
st.markdown("Ce filtrage est apparent dans un tableau contenant toutes les lignes contenant les valeurs sélectionnées dans les filtres.")
