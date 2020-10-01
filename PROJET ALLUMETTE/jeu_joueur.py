from resultats import*
from suppression import*
from tapis import*
from time import*

def jeu_joueur(x,regle):

    
    
    #si le nombre de cartes sur la table est inférieur au nb de cartes que l'on peut retirer alors égalité le jeu s'arrète
    if x-regle[0]<0 and x-regle[1]<0 and x-regle[2]<0:
        resulats("égalité")
        return 0
    
    #si le joueur ne retire pas le bon nombre de carte autorisé, il reessaye jusqu'a ce que le chiffre appartienne dans la règle du jeu
    else:
        choix=int(numinput("Choix des cartes","combien de cartes voullez vous enlever ?"))
        while((choix!=regle[0]) and (choix!=regle[1]) and (choix!=regle[2])) or (x-choix<0):
            choix=int(numinput("ERREUR","vous ne pouvez pas choisir celui la, choisssez en un autre. Autre choix ?"))
        supprime(-500,200,choix,x)
        x=x-choix
        color("green")
        begin_fill()
        rectangle(-37,-250,20,20)
        end_fill()
        color("black")
        write(x, font=("Arial", 15, "normal"))
        left(90)
        if x==0:
            resultats("GAGNE!")
            return(x)
        else:
            return (x)
    sleep(4) 
