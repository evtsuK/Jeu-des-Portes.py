import random

print("----------------------------------------------------------------------------------")
print('|Bienvenue dans un jeu ou tu dois trouver la pomme cachée derrière une des portes|')
print("----------------------------------------------------------------------------------")

chances = 1 # Nombre de chance
nbPortes = 10 # Nombre de portes
choix = -1  # Choix de la porte

# Ajout de numero pour chaque portes
while nbPortes < 0 or nbPortes > 6: # While demande création de portes
    nbPortes = int(input('Combien de portes voulez-vous ajouter ? : '))
    if 0 < nbPortes <= 6 : # Condition verification tableau ]0,6]
        tabPortes = ['-' for i in range(nbPortes)] # Tableau de manipulation
        tabAffichage = ["Fermée!" for i in range(nbPortes)] # Tableau utilisé pour afficher
        posPomme = random.randint(0,nbPortes) # Chiffre aléatoire
        tabPortes[posPomme]= 'pomme' # Affecte valeur "pomme" a la position aléatoire trouvée précédemment
        while choix > nbPortes or chances != 4: # While demande porte a choisir
            print(tabAffichage)
            choix = int(input('Quel est la porte que vous souhaitez choisir : '))
            if choix == posPomme+1: # Si utilisateur gagne
                tabAffichage[posPomme] = "Pomme"
                print(tabAffichage)
                print("Félicitation vous avez trouvé la pomme !")
                exit()
            elif chances == 3: # Si atteint nombre de chance
                print("Nombre de chance autorisé atteint, vous avez perdu !")
                exit()
            else: # Autre cas (Si choix erronées, mais avec des chances restantes)
                print("Veuillez réessayer ! Attention il vous reste ", (3-chances), " chances !")
                tabAffichage[choix-1] = "Ouverte!"
                chances += 1

                
    else:
        print('veuillez-choisir une valeur entre 0 et 6')
