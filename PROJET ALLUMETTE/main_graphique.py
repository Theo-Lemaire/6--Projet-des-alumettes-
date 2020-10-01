#principal dessin, interface graphique
from jetons import*
from turtle import*
from tapis import*
from main import*


setup(width=2000, height=700, startx=0, starty=0)

speed("fastest")
def interface_graphique_fixe():
    tapis(-650,-325)
    jetons(580,-260,"yellow","white",50)
    jetons(520,-310,"blue","white",50)
    jetons(460,-280,"black","white",50)

    up()
    left(125)
    down()
    main(583,322,80,160)

    up()
    left(90)
    down()
    main(-580,-315,80,160)



