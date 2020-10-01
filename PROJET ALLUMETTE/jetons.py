from turtle import*

#réalisation des jetons (décoration)
def jetons (x,y,c1,c2,r):
    seth(0)
#base du jeton
    color(c1)
    up()
    goto(x,y)
    down()
    begin_fill()
    circle(r,360)
    end_fill()

#cercle epais discontinue   
    color(c2)
    up()
    left(90)
    forward(r/5)
    right(90)
    down()
    width(r/25)
    circle((4/5)*r,360)
    

    up()
    right(90)
    forward(r/10)
    left(90)
    width(r/5)
    down()
    i=0
    circle((9/10)*r,15)
    while i<360:
        up()
        circle((9/10)*r,30)
        down()
        circle((9/10)*r,30)
        i=i+60
    
#contour du jeton
    width(r/25)
    right(90)
    up()
    forward(r/10)
    left(90)
    down()
    color("black")
    circle(r,360)
    
#design intérieur du jeton
    color(c2)
    up()
    left(90)
    forward(r/3)
    right(90)
    down()
    y=0
    circle((9/14)*r,15)
    while y<360:
        up()
        circle((9/14)*r,30)
        down()
        circle((9/14)*r,30)
        y=y+60
    right(30)





