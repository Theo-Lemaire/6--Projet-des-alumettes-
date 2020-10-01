from turtle import*
from tapis import*

#design de la carte
def carte(x,y,taille):
    #contour de la carte 
    color("black")
    rectangle(x,y,0.75*taille+1,taille+1)
    left(90)

    color("white")
    begin_fill()
    rectangle(x,y+1,0.75*taille,taille)
    left(90)
    end_fill()

    #intérieur de la carte
    color("red")
    begin_fill()
    rectangle(x+0.1*taille,y+0.1*taille,0.54*taille,0.8*taille)
    right(180)
    end_fill()

    up()
    forward(0.18*taille)
    right(90)
    forward(0.27*taille)
    down()
    color("white")
    begin_fill()
    circle(taille*0.22,360)
    end_fill()
    
    #étoile centrale
    color("black")
    up()
    left(180)
    forward(0.03*taille)
    right(90)
    down()
    begin_fill()
    z=0
    while z<5:
        forward(0.45*taille)
        right(160)
        forward(0.45*taille)
        right(160)
        z=z+1
    end_fill()

    #4 points dans les coins
    up()
    left(95)
    forward(0.27*taille)
    down()
    color("black")
    begin_fill()
    circle(0.02*taille,360)
    end_fill()
    up()
    left(150)
    forward(0.40*taille)
    down()
    begin_fill()
    circle(0.02*taille,360)
    end_fill()
    up()
    left(92)
    forward(0.73*taille)
    down()
    begin_fill()
    circle(0.02*taille,360)
    end_fill()
    up()
    left(90)
    forward(0.40*taille)
    down()
    begin_fill()
    circle(0.02*taille,360)
    end_fill()
    up()
    goto(x,y)
    left(3)
    down()
    

    
    
