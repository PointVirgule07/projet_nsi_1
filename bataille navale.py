"""génère la grille de jeu de la bataille navale"""
G1 = [["." for _ in range(10)] for _ in range(10)]
G2 = [["." for _ in range(10)] for _ in range(10)]

"""dictionnaire pour convertir les abréviations en nombre de cases occupées par le bateau et le nombre de bateaux de chaque types.
   (nombre de bateaux, nombre de cases occupées par le bateau)"""
nombre_bateaux_J1 = {"pc": (1,5), "c": (1,4), "ct": (2,3), "t": (1,2)}
nombre_bateaux_J2 = {"pc": (1,5), "c": (1,4), "ct": (2,3), "t": (1,2)}

"""transforme le nom des cases en leurs coordonées (x,y) (A0 -> (0,0), A1 -> (0,1), ..., J9 -> (9,9)"""
dic = {chr(65+i)+str(j): (i,j) for i in range(10) for j in range(10)}

def affiche(G):
    """affiche la grille de jeu de la bataille navale
    G: list(list(str)) -> grille de jeu"""
    print("  A B c D E F G H I J")
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
    taille = nombre_bateaux.get(bateau, (0, 0))[1]
    x, y = dic.get(emplacement, (0, 0))

    if bateau not in nombre_bateaux or G[y][x] != "." or not estDansGrille(x, y) or direction not in {"H", "V"} or nombre_bateaux[bateau][0] == 0 or (direction == "V" and y + taille > 10) or (direction == "H" and x + taille > 10):
        print("\033[1;31mPlacement invalide\033[1;37m")
        return False

    for i in range(taille):
        if (direction == "V" and G[y + i][x] != ".") or (direction == "H" and G[y][x + i] != "."):
            print("\033[1;31mCase déjà occupée\033[1;37m")
            return False

    for i in range(taille):
        if direction == "V":
            G[y + i][x] = "B"
        else:
            G[y][x + i] = "B"
    nombre_bateaux[bateau] = (nombre_bateaux[bateau][0] - 1, nombre_bateaux[bateau][1])
    return True

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

while nombre_bateaux_J1["pc"][0] != 0 or nombre_bateaux_J1["c"][0] != 0 or nombre_bateaux_J1["ct"][0] != 0 or nombre_bateaux_J1["t"][0] != 0:
    print("\033[0;32m\nJoueur 1\033[0;0m\n")
    affiche(G1)
    emplacement = input("Entrez l'emplacement du bateau: ")
    print(f"Les bateaux disponibles sont: PC {nombre_bateaux_J1['pc'][1]}, C {nombre_bateaux_J1['c'][1]}, CT {nombre_bateaux_J1['ct'][1]},  {nombre_bateaux_J1['t'][1]}")
    bateau = input("Entrez le type de bateau: ").lower()
    direction = input("Entrez la direction du bateau (H pour horizontal, V pour vertical): ")
    placeBateau(G1, emplacement, bateau, direction, nombre_bateaux_J1)

while nombre_bateaux_J2["pc"][0] != 0 or nombre_bateaux_J2["c"][0] != 0 or nombre_bateaux_J2["ct"][0] != 0 or nombre_bateaux_J2["t"][0] != 0:
    print("\033[0;32m\nJoueur 2\033[0;0m\n")
    affiche(G2)
    emplacement = input("Entrez l'emplacement du bateau: ")
    print(f"Les bateaux disponibles sont: pc {nombre_bateaux_J2['pc'][1]}, c {nombre_bateaux_J2['c'][1]}, ct {nombre_bateaux_J2['ct'][1]}, t {nombre_bateaux_J2['t'][1]}")
    bateau = input("Entrez le type de bateau: ")
    direction = input("Entrez la direction du bateau (H pour horizontal, V pour vertical): ")
    placeBateau(G2, emplacement, bateau, direction, nombre_bateaux_J2)


