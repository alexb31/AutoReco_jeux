import pandas as pd

df = pd.read_excel("backend/data/scraper.xlsx", sheet_name="tests")

# Supprimer la colonne inutile
df = df.drop(columns=["créé par Mad LL (madll.fr/canardpc)"])

# Renommer les colonnes
df = df.rename(columns={
    "Jeu": "title",
    "Editeur / Développeur": "publisher",
    "Genre": "genre",
    "Note": "score",
    "n°": "issue",
    "an": "year",
    "par": "reviewer"
})

# Supprimer les lignes sans titre ou sans note
df = df.dropna(subset=["title", "score"])

print(df.shape)
print(df.head())

