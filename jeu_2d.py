import random
import time

def poser_question(niveau):
    # Adapter la difficulté selon le niveau
    if niveau == 1:
        # Additions simples entre 1 et 10
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = "+"
        reponse = a + b
    elif niveau == 2:
        # Additions et soustractions un peu plus grandes
        a = random.randint(5, 20)
        b = random.randint(1, 15)
        op = random.choice(["+", "-"])
        reponse = a + b if op == "+" else a - b
    else:
        # Multiplications pour les niveaux supérieurs
        a = random.randint(2, 10)
        b = random.randint(2, 10)
        op = "×"
        reponse = a * b

    question_texte = f"Combien font {a} {op} {b} ? "
    return question_texte, reponse

def lancer_jeu():
    print("=" * 50)
    print("🧠 BIENVENUE DANS LE DUEL MATHÉMATIQUE CHRONOMÉTRÉ ! 🧠")
    print("=" * 50)
    print("Règles : Vous avez exactement 6 secondes par calcul.")
    print("Plus vous marquez de points, plus le niveau s'élève !\n")
    
    input("Appuyez sur Entrée pour commencer...")
    print("\nC'est parti !")

    score = 0
    en_jeu = True

    while en_jeu:
        # Déterminer le niveau en fonction du score
        if score < 5:
            niveau = 1
        elif score < 10:
            niveau = 2
        else:
            niveau = 3

        question, bonne_reponse = poser_question(niveau)
        
        print(f"\n--- Niveau {niveau} (Score actuel : {score}) ---")
        print(question, end="", flush=True)

        # Enregistrer le temps de départ
        debut = time.time()
        
        try:
            # Récupérer la saisie de l'utilisateur
            saisie = input()
            fin = time.time()
            
            # Calculer le temps écoulé
            temps_ecoule = fin - debut

            # Vérifier si le joueur a dépassé les 6 secondes
            if temps_ecoule > 10.0:
                print(f"⏰ Temps écoulé ! (Vous avez mis {temps_ecoule:.1f} secondes).")
                en_jeu = False
                break

            # Convertir la réponse en nombre entier
            reponse_utilisateur = int(saisie)

            if reponse_utilisateur == bonne_reponse:
                print(f"✅ Bravo ! Bonne réponse en {temps_ecoule:.1f}s.")
                score += 1
            else:
                print(f"❌ Erreur ! La bonne réponse était {bonne_reponse}.")
                en_jeu = False
                break

        except ValueError:
            # Si le joueur tape autre chose qu'un nombre
            print("❌ Entrée invalide (ce n'est pas un nombre). Partie terminée !")
            en_jeu = False
            break

    print("\n" + "=" * 50)
    print("FIN DE LA PARTIE 🎮")
    print(f"Votre score final est de : {score} bonne(s) réponse(s).")
    print("=" * 50)

# Lancer le jeu
if __name__ == "__main__":
    lancer_jeu()