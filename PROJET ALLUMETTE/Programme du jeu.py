from math import *
from random import *
from jeu_joueur import *
from jeu_ordi import *
from regle_jeu import *
from main_graphique import *
from carte import *
from pile_carte import*
from turtle import*


ht()
tracer(0)
interface_graphique_fixe()
tracer(0)


#difficulté de l'ordinateur
ordi=numinput("Choix de la difficulté","Veuillez taper le  1 si vous voulez un ordi faible ou le 2 si vous voulez un ordi moyen ")
while ordi!=1 and ordi!=2:
    ordi=numinput("ERREUR"," Veuillez choisir 1 ou 2")
    
#on demande a l'utilisateur les trois chiffres qui définissent les règles
regle = regle_jeu()

# x le nombre de cartes
x=randint(15,30)
pile_carte(-500,200,x)
color("black")
up()
goto(-100,-250)
down()
write("il reste      cartes sur la table", font=("Arial", 15, "normal"))
up()
goto(-37,-250)
down()
write(x,font=("Arial", 15,"normal"))

#démarage du jeu
joueur=textinput("Le jeu commence!", "voulez-vous commencer ? oui ou non?")
while joueur!="oui" and joueur!="non":
    joueur=textinput("ERREUR","je n'ai pas compris, veuillez repondre 'oui' ou 'non' a la question 'Voulez vous commencer ?'")
if joueur=="oui":
    
    #ces fonctions ci dessous return le nombre de carte une fois que le joueur ou l'ordinateur a joué (nb de carte stocké dans la variable x)
    while x!=0:
        x=jeu_joueur(x,regle)
        if x!=0:
            x=jeu_ordi(x,regle,ordi)
elif joueur=="non":
    while x!=0:
        x=jeu_ordi(x,regle,ordi)
        if x!=0:
            x=jeu_joueur(x,regle)


