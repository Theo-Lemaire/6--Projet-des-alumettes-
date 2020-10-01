from carte import*
from turtle import*


def pile_carte(x,y,nb):
    seth(0)
    up()
    goto(x,y)
    down()
    nbcarte=0
    a=0
    b=0
    c=0
    while nbcarte<nb:
        if nbcarte<=9:
            carte(x+a,y-100)
            a=a+100
        elif nbcarte<=19 and nbcarte>=10:
            carte(x+b,y-230)
            b=b+100
        else:
            carte(x+c,y-360)
            c=c+100
        nbcarte=nbcarte+1

