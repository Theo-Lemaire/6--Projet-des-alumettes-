from turtle import*

#pour dessiner les rectangles
def rectangle(x,y,longueur,largeur):
    up()
    goto(x,y)
    down()
    i=0
    while i<2:
        forward(longueur)
        left(90)
        forward(largeur)
        left(90)
        i=i+1
    right(90)

def tapis(x,y):
    
#pour faire le rectange vert
    color("green")
    begin_fill()
    rectangle(-650,-325,1300,655)
    end_fill()

#le rectangle marron
    color("brown")
    up()
    goto(-650,-325)
    down()
    width(20)
    forward(4)
    left(90)
    rectangle(-650,-325,1300,655)
    
#le rectangle noir
    color("black")
    width(2)
    left(90)
    rectangle(-525,-200,1050,425)
    left(90)
    up()
    goto(-300,-200)
    down()
    
#texte polytech casino
    color("green")
    forward(600)
    left(180)
    up()
    forward(450)
    down()
    color("black")
    write("PolytechCasino", font=("Lucida Handwriting", 25 , "normal"))




