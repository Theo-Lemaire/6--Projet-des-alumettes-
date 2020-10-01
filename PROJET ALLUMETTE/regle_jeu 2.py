from turtle import*

def regle_jeu():
    #le joueur choisit lui même la règle a laquelle il veut jouer ( = le nb de cartes autorisé à retirer)
    regle=[]
    i=0
    while i<3:
        a=int(numinput("Choix des regles","Choisissez 3 nombres entre 1 et 9 pour definir les regles, ces nbs seront le nb de cartes autorisé à retirer, entre un nombre:"))
        if a>0 and a<10:
            regle.append(a)
            i=i+1
        else:
            a=int(numinput("ERREUR" ,"il faut choisir un nombre entre 0 et 9"))
    return regle
