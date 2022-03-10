import random


print('Bienvenue dans un jeu ou tu dois trouver la pomme cachée derrière une des portes')
chances=1
nbPortes=60
while nbPortes<0 or nbPortes>6:
    nbPortes = int(input('Combien de portes voulez-vous ajouter ? :'))
    if 0<nbPortes<=6 :
        tabPortes = ['-' for i in range(nbPortes)]
        posPomme = random.randint(0,nbPortes)
        tabPortes[posPomme]='pomme'
        choix = 8 
        while choix > nbPortes or chances != 4:
            print(tabPortes)
            choix = int(input('Quel est la porte que vous souhaitez choisir : '))
            if choix == posPomme+1:
                print('Félicitation vous avez réussis')
                exit()
            elif chances == 3:
                print('vous avez perdu')
                exit()
            else:
                print('Faites attention !')
                chances+=1

                
    else:
        print('veuillez-choisir une valeur entre 0 et 6')
        

