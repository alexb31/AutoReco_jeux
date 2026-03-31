from sqlalchemy import create_engine
from load_data import load_games

df = load_games()
engine = create_engine("sqlite:///backend/data/games.db")
df.to_sql("games", engine, if_exists="replace", index=False)

print("Base de données créée !")