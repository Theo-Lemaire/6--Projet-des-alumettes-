from turtle import*
from random import*

def regle_jeu():
    r=randint(1,3)
    if r==1:
        regle=[1,2,3]
    elif r==2:
        regle=[1,3,5]
    else:
        regle=[2,4,6]
    
    up()
    goto(-100,-300)
    down()
    write("Les regles sont",font=("Arial",15,"normal"))
    up()
    goto(50,-300)
    down()
    write(regle,font=("Arial",15,"normal"))

    return regle
