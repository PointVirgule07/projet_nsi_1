"""génère la grille de jeu de la bataille navale"""
G1 = [["." for _ in range(10)] for _ in range(10)]
G2 = [["." for _ in range(10)] for _ in range(10)]

"""dictionnaire pour convertir les abréviations en nombre de cases occupées par le bateau et le nombre de bateaux de chaque types.
   (nombre de bateaux, nombre de cases occupées par le bateau)"""
nombre_bateaux_J1 = {"PC": (1,5), "C": (1,4), "CT": (2,3), "T": (1,2)}
nombre_bateaux_J2 = {"PC": (1,5), "C": (1,4), "CT": (2,3), "T": (1,2)}

"""transforme le nom des cases en leurs coordonées (x,y) (A0 -> (0,0), A1 -> (0,1), ..., J9 -> (9,9)"""
dic = {chr(65+i)+str(j): (i,j) for i in range(10) for j in range(10)}
print(dic)

def affiche(G):
    """affiche la grille de jeu de la bataille navale
    G: list(list(str)) -> grille de jeu"""
    print("  A B C D E F G H I J")
    for i in range(10):
        print(i, end=' ')
        for j in range(10):
            print(G[i][j], end=' ')
        print()

def placeBateau(G, emplacement, bateau, direction, nombre_bateaux):
    """place un bateau sur la grille de jeu
    G: list(list(str)) -> grille de jeu
    emplacement: str -> emplacement du bateau
    bateau: str -> type de bateau
    direction: str -> direction du bateau
    nombre_bateaux: dict -> dictionnaire des bateaux
    return: bool -> True si le bateau a été placé, False sinon"""

    taille = nombre_bateaux_J1[bateau][1]
    x,y = dic[emplacement][0],dic[emplacement][1]
    if bateau not in nombre_bateaux_J1 :
        print("bateau non valide")
        return False
    elif G[x][y] != "." :
        print("case déjà occupée")
        return False
    elif not estDansGrille(x,y) :
        print("case hors grille")
        return False
    elif (direction != "H" and direction != "V"):
        print("direction non valide")
        return False
    elif nombre_bateaux_J1[bateau][0] == 0:
        print("plus de bateaux de ce type")
        return False
    else:       
        if direction == "H":
            if y+taille > 10 :
                print("bateau hors grille")
                return False
            else :
                for i in range(taille):
                    G[x][y+i] = "B"
        elif direction == "V":
            if x+taille > 10 :
                print("bateau hors grille")
                return False
            else :
                for i in range(taille):
                    G[x+i][y] = "B"

def estDansGrille(x, y):
    """vérifie si les coordonnées sont dans la grille"""
    return 0<=x<10 and 0<=y<10

def touche_ou_plouf(G, emplacement, dic):
    """vérifie si la case est occupée par un bateau
    G: list(list(str)) -> grille de jeu
    emplacement: str -> emplacement de la case
    dic: dict -> dictionnaire des emplacements
    return: bool -> True si la case est occupée par un bateau, False sinon"""
    x,y = dic[emplacement][0],dic[emplacement][1]
    if G[x][y] == "B":
        G[x][y] = "X"
        return True
    else:
        G[x][y] = "O"
        return False

#while True:
    affiche(G1)
    emplacement = input("Entrez l'emplacement du bateau: ")
    print(f"Les bateaux disponibles sont: PC {nombre_bateaux_J1['PC'][1]}, C {nombre_bateaux_J1['C'][1]}, CT {nombre_bateaux_J1['CT'][1]}, T {nombre_bateaux_J1['T'][1]}")
    bateau = input("Entrez le type de bateau: ")
    direction = input("Entrez la direction du bateau (H pour horizontal, V pour vertical): ")
    placeBateau(G1, emplacement, bateau, direction, nombre_bateaux_J1)

