from turtle import*

def main(x,y,l,L):
    up()
    goto(x,y)
    forward(-l/4)
    left(90)
    down()
    begin_fill()
    color("sandybrown")
    forward(L/5)
    right(90)
    circle(l/4,90)
    forward((3*L/5)-(l/4))
    i=0
    while i<3:
        circle((l/8),180)
        forward((3/10)*L)
        backward((3/10)*L)
        left(180)
        i=i+1
    circle((l/8),180)
    forward((3/10)*L)
    right(125)
    forward(2*L/10)
    circle((l/8),180)
    forward((3/10)*L)
    right(55)
    forward((L/5)-(3*l/8))
    circle(l/4,90)
    right(90)
    forward(L/5)
    left(90)
    end_fill()
    up()
    goto(x,y)
    forward(-l/4)
    left(90)
    down()
    color("black")
    forward(L/5)
    right(90)
    circle(l/4,90)
    forward((3*L/5)-(l/4))
    i=0
    while i<3:
        circle((l/8),180)
        forward((3/10)*L)
        backward((3/10)*L)
        left(180)
        i=i+1
    circle((l/8),180)
    forward((3/10)*L)
    right(125)
    forward(2*L/10)
    circle((l/8),180)
    forward((3/10)*L)
    right(55)
    forward((L/5)-(3*l/8))
    circle(l/4,90)
    right(90)
    forward(L/5)

    left(90)
    begin_fill()
    color("white")
    forward(L/4)
    right(90)
    forward(l/8)
    right(90)
    forward(L/4)
    right(90)
    forward(l/8)
    end_fill()
    
    backward(l/8)
    right(90)
    begin_fill()
    color("black")
    forward(L/4)
    right(90)
    forward(l/8)
    right(90)
    forward(L/4)
    right(90)
    forward(l/8)
    end_fill()
    
    
    

