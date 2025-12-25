from src.compte import CompteBancaire

if __name__ == "__main__":
    

    paul = CompteBancaire("Paul")
    pierre = CompteBancaire("Pierre")

 
    paul.deposer(100)
    print(paul)  
    print(pierre)

    print("\n--- Virement de 50€ de Paul à Pierre ---")
    paul.virement(pierre, 50)


    print(paul)   
    print(pierre) 

    print("\n--- Tentative de fraude ---")
    try:
        paul.virement(pierre, 200) 
    except ValueError as e:
        print(f"Erreur attrapée : {e}")