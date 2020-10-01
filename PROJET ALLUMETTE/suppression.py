
from turtle import*
from pile_carte import *
from tapis import *
##def supprime(x,y,nbcarte):
##    i=0
##    while i<nbcarte and y<=200:
##        begin_fill()
##        rectangle(x,y,85,115)
##        left(90)
##        end_fill()
##        if  x<=-350:
##            y=y+100
##            x=350
##        x=x-95
##        i=i+1
##    return x
##
##supprime(-100,-100,3)
##print(x)



def supprime(x,y,choix,nb):
    color("green")
    i=0
    while i<choix:
        if nb>20:
            begin_fill()
            rectangle(x+(nb-21)*100,y-360,85,115)
            left(90)
            end_fill()
        elif nb<=20 and nb>10:
            begin_fill()
            rectangle(x+(nb-11)*100,y-230,85,115)
            left(90)
            end_fill()
        else:
            begin_fill()
            rectangle(x+(nb-1)*100,y-100,85,115)
            end_fill()
            left(90)
        nb=nb-1
        i=i+1




