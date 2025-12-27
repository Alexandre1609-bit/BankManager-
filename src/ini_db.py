import sqlite3


def init_db():
    with sqlite3.connect('bank.db') as con :
        cur = con.cursor()
        cur.execute("PRAGMA foreign_keys = ON")


        cur.execute("""
            CREATE TABLE IF NOT EXISTS comptes (
                nom TEXT PRIMARY KEY,
                solde REAL NOT NULL
            );
            """
            )

        try:
            cur.execute("INSERT INTO comptes (nom, solde) VALUES (?, ?)", ("Paul", 100))
            cur.execute("INSERT INTO comptes (nom, solde) VALUES (?, ?)", ("Pierre", 0))
            print("Données de test ajouté")
        except sqlite3.IntegrityError:
            print("Erreur : compte déjà existant")
        con.commit()
if __name__ == "__main__":
    init_db()