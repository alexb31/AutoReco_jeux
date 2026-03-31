import pandas as pd

def load_games():
    df = pd.read_excel("backend/data/scraper.xlsx", sheet_name="tests")
    df = df.drop(columns=["créé par Mad LL (madll.fr/canardpc)"])
    df = df.rename(columns={
        "Jeu": "title",
        "Editeur / Développeur": "publisher",
        "Genre": "genre",
        "Note": "score",
        "n°": "issue",
        "an": "year",
        "par": "reviewer"
    })
    df = df.dropna(subset=["title", "score"])
    return df