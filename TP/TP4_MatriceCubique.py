from DobotEDU import *

# ============================
# === TP4_MatriceCubique =====
# ============================

# ---------------------------------
# Constantes
# ---------------------------------
HOME_X, HOME_Y, HOME_Z = (160, 34, 0)   # position de repos (Z > 0 !)
COMMON_Z_ABOVE = 0                       # hauteur d’approche
COMMON_Z_AT    = -50                    # hauteur de saisie/dépôt
#Grille avec numéro en vert
# Début de la matrice (cube bas-gauche, position 4,1 face au robot)
MATRIX_X0, MATRIX_Y0 = (208, 34)
STEP = 35     # entraxe entre cubes en mm

# Emplacement commun de dépôt
PLACE_X, PLACE_Y = (77,-180)   # à ajuster selon votre espace

# ---------------------------------
# Routine Pick & Place pour un cube
# ---------------------------------
def pick_and_place(x, y):
    # 1. Aller au-dessus du cube
    magician.ptp(mode=2, x=x, y=y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(0.5)

    # 2. Descendre et aspirer
    magician.ptp(mode=2, x=x, y=y, z=COMMON_Z_AT, r=0)
    magician.wait(0.5)
    magician.set_endeffector_suctioncup(True, True)
    magician.wait(0.5)

    # 3. Remonter
    magician.ptp(mode=2, x=x, y=y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(0.5)

    # 4. Aller au-dessus de la zone de dépôt
    magician.ptp(mode=2, x=PLACE_X, y=PLACE_Y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(0.5)

    # 5. Relâcher
   # magician.ptp(mode=2, x=PLACE_X, y=PLACE_Y, z=COMMON_Z_AT, r=0)
   # magician.wait(0.5)
    magician.set_endeffector_suctioncup(True, False)
    magician.wait(0.5)

    # 6. Revenir au-dessus et retour maison
    magician.ptp(mode=2, x=PLACE_X, y=PLACE_Y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(0.5)
    magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
    magician.wait(0.5)


# ---------------------------------
# Programme principal
# ---------------------------------
# Position de départ
magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
magician.wait(0.5)

# Parcours de la matrice 3x3
for i in range(3):  # lignes
    for j in range(3):  # colonnes
        x = MATRIX_X0 + j * STEP
        y = MATRIX_Y0 - i * STEP
        pick_and_place(x, y)
