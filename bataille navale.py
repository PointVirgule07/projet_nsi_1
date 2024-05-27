# Génère la grille de jeu de la bataille navale
G1 = [["." for _ in range(10)] for _ in range(10)]
G1_bis = [["." for _ in range(10)] for _ in range(10)]
G2 = [["." for _ in range(10)] for _ in range(10)]
G2_bis = [["." for _ in range(10)] for _ in range(10)]

# Dictionnaire pour convertir les abréviations en nombre de cases occupées par le bateau et le nombre de bateaux de chaque types.
# (nombre de bateaux, nombre de cases occupées par le bateau)
nombre_bateaux_J1 = {"pc": (1, 5), "c": (1, 4), "ct": (2, 3), "t": (1, 2)}
nombre_bateaux_J2 = {"pc": (1, 5), "c": (1, 4), "ct": (2, 3), "t": (1, 2)}

# Transforme le nom des cases en leurs coordonnées (x,y) (A0 -> (0,0), A1 -> (0,1), ..., J9 -> (9,9))
dic = {chr(97 + i) + str(j): (i, j) for i in range(10) for j in range(10)}

def affiche(G):
    """Affiche la grille de jeu de la bataille navale
    G: list(list(str)) -> grille de jeu"""
    print("  A B C D E F G H I J")
    for i in range(10):
        print(i, end=' ')
        for j in range(10):
            print(G[i][j], end=' ')
        print()

def placeBateau(G, emplacement, bateau, direction, nombre_bateaux):
    """Place un bateau sur la grille de jeu
    G: list(list(str)) -> grille de jeu
    emplacement: str -> emplacement du bateau
    bateau: str -> type de bateau
    direction: str -> direction du bateau
    nombre_bateaux: dict -> dictionnaire des bateaux
    return: bool -> True si le bateau a été placé, False sinon"""
    taille = nombre_bateaux[bateau][1]
    if emplacement not in dic:
        print("\033[1;31mEmplacement invalide\033[1;37m")
        return False
    x, y = dic[emplacement]

    if bateau not in nombre_bateaux or G[y][x] != "." or not estDansGrille(x, y) or direction not in {"h", "v"} or nombre_bateaux[bateau][0] == 0 or (direction == "v" and y + taille > 10) or (direction == "h" and x + taille > 10):
        print("\033[1;31mPlacement invalide\033[1;37m")
        return False

    for i in range(taille):
        if (direction == "v" and G[y + i][x] != ".") or (direction == "h" and G[y][x + i] != "."):
            print("\033[1;31mCase déjà occupée\033[1;37m")
            return False

    for i in range(taille):
        if direction == "v":
            G[y + i][x] = "B"
        else:
            G[y][x + i] = "B"
    nombre_bateaux[bateau] = (nombre_bateaux[bateau][0] - 1, nombre_bateaux[bateau][1])
    return True

def estDansGrille(x, y):
    """Vérifie si les coordonnées sont dans la grille"""
    return 0 <= x < 10 and 0 <= y < 10

def touche_ou_plouf(G, G_bis, emplacement, dic):
    """Vérifie si la case est occupée par un bateau
    G: list(list(str)) -> grille de jeu
    g_bis: list(list(str)) -> grille de tir
    emplacement: str -> emplacement de la case
    dic: dict -> dictionnaire des emplacements
    return: bool -> True si la case est occupée par un bateau, False sinon"""
    if emplacement not in dic:
        print("\033[1;31mEmplacement invalide\033[1;37m")
        return False
    x, y = dic[emplacement]
    if G[y][x] == "B":
        G[y][x] = "X"
        G_bis[y][x] = "X"
        return True
    else:
        G[y][x] = "O"
        G_bis[y][x] = "O"
        return False

def début_jeu():
    while any(nombre_bateaux_J1[b][0] > 0 for b in nombre_bateaux_J1):
        print("\033[0;32m\nJoueur 1\033[0;0m\n")
        affiche(G1)
        emplacement = input("Entrez l'emplacement du bateau: ").lower()
        print(f"Les bateaux disponibles sont: PC {nombre_bateaux_J1['pc'][0]}, C {nombre_bateaux_J1['c'][0]}, CT {nombre_bateaux_J1['ct'][0]}, T {nombre_bateaux_J1['t'][0]}")
        bateau = input("Entrez le type de bateau: ").lower()
        direction = input("Entrez la direction du bateau (H pour horizontal, V pour vertical): ").lower()
        placeBateau(G1, emplacement, bateau, direction, nombre_bateaux_J1)

    while any(nombre_bateaux_J2[b][0] > 0 for b in nombre_bateaux_J2):
        print("\033[0;32m\nJoueur 2\033[0;0m\n")
        affiche(G2)
        emplacement = input("Entrez l'emplacement du bateau: ").lower()
        print(f"Les bateaux disponibles sont: PC {nombre_bateaux_J2['pc'][0]}, C {nombre_bateaux_J2['c'][0]}, CT {nombre_bateaux_J2['ct'][0]}, T {nombre_bateaux_J2['t'][0]}")
        bateau = input("Entrez le type de bateau: ").lower()
        direction = input("Entrez la direction du bateau (H pour horizontal, V pour vertical): ").lower()
        placeBateau(G2, emplacement, bateau, direction, nombre_bateaux_J2)

def vict(G):
    """Vérifie si un joueur a gagné
    G: list(list(str)) -> grille de jeu
    return: bool -> True si un joueur a gagné, False sinon"""
    for i in range(10):
        for j in range(10):
            if G[i][j] == "B":
                return False
    return True

# Main
début_jeu()
while True:
    print("\033[0;32m\n Grille_Joueur 1\033[0;0m\n")
    affiche(G1)
    print("\033[0;32m\n Grille_De_Tir\033[0;0m\n")
    affiche(G1_bis)
    emplacement = input("Entrez l'emplacement de la case: ").lower()
    touche_ou_plouf(G2,G1_bis,emplacement, dic)
    if vict(G2):
        print("\033[0;32m\n Le joueur 1 a gagné\033[0;0m\n")
        break

    print("\033[0;32m\nGrille_Joueur 2\033[0;0m\n")
    affiche(G2)
    print("\033[0;32m\nGrille_De_Tir\033[0;0m\n")
    affiche(G2_bis)
    emplacement = input("Entrez l'emplacement de la case: ").lower()
    touche_ou_plouf(G1,G2_bis,emplacement, dic)
    if vict(G1):
        print("\033[0;32m\n Le joueur 2 a gagné\033[0;0m\n")
        break
