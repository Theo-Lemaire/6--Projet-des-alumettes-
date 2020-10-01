from random import *
from resultats import*
from suppression import*
from time import*

#l'ordinateur est faible, il joue des chiffres aléatoires
def jeu_ordi_faible(x,regle):
    #si le nb de cartes sur la table est inférieur au nombre de cartes qu'on peut retirer, alors le jeu s'arrète: égalité
    if x-regle[0]<0 and x-regle[1]<0 and x-regle[2]<0:
        resultats("égalité")
        return 0
    #sinon l'ordi joue normalement et de façon aléatoire 
    else:
        coup=randint(0,2)
        while x-regle[coup]<0:
            coup=randint(0,2)
        supprime(-500,200,regle[coup],x)
        x=x-regle[coup]
        color("green")
        begin_fill()
        rectangle(-37,-250,20,20)
        end_fill()
        color("black")
        write(x, font=("Arial", 15, "normal"))
        
        up()
        goto(190,280)
        down()
        color("black")
        write(" L'ordinateur a pris     cartes", font=("Arial", 15 , "normal"))

        
        color("green")
        left(180)
        begin_fill()
        rectangle(380,280,20,20)
        end_fill()
        up()
        goto(365,280)
        down()
        color("black")
        write(regle[coup], font=("Arial", 15, "normal"))
        
       
        if x==0:
            resultats("PERDU!")
            return(x)
        else:
            return(x)
        
#l'ordinateur est moyen
def jeu_ordi_moyen(x,regle):
    #idem que pour ordi faible 
    print("ordinateur, a vous")
    if x-regle[0]<0 and x-regle[1]<0 and x-regle[2]<0:
        resultats("égalité")
        return 0
    #l'ordinateur est un minimum intelligent, si il reste le meme nombre de cartes sur la table que celui qu'il y a dans la règle, il prend ce nombre de carte
    else:
        coup=coup_moyen(x,regle)
        supprime(-500,200,regle[coup],x)
        x=x-regle[coup]
      
        if x==0:
            resultats("PERDU!")
            return(x)
        else:
            return(x)

    
def coup_moyen(x,regle):
    if x==regle[0]:
        return 0
    elif x==regle[1]:
        return 1
    elif x==regle[2]:
        return 2
    else:
        coup=randint(0,2)
        while x-regle[coup]<0:
            coup = randint(0,2)
        return coup

#lors de jouer, le joueur choisis si il veut un ordi faible ou un ordi moyen
def jeu_ordi(x,regle,ordi):
    sleep(2)
    if ordi==1:
        return jeu_ordi_faible(x,regle)
    if ordi==2:
        return jeu_ordi_moyen(x,regle)
