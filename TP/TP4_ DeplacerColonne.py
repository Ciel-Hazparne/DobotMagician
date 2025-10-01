from DobotEDU import *

# ============================
# ==== TP4_DeplacerLigne =====
# ============================

# ---------------------------------
# Constantes
# ---------------------------------
HOME_X, HOME_Y, HOME_Z = (218.5, 78, 0)    # position de reposau dessus du carré bleu 160, 34, 0
COMMON_Z_ABOVE = 0                         # hauteur d’approche
COMMON_Z_AT = -45                       # hauteur de saisie/dépôt

# Grille (position 0)
MATRIX_X0, MATRIX_Y0 = (183, 34.5)
STEP = 35     # entraxe entre cubes en mm

# ---------------------------------
# Routine Pick & Place pour un cube
# ---------------------------------
def pick_and_place(from_x, from_y, to_x, to_y):
    # 1. Aller au-dessus du cube source
    magician.ptp(mode=2, x=from_x, y=from_y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(0.5)

    # 2. Descendre et aspirer
    magician.ptp(mode=2, x=from_x, y=from_y, z=COMMON_Z_AT, r=0)
    magician.wait(0.5)
    magician.set_endeffector_suctioncup(True, True)
    magician.wait(0.5)

    # 3. Remonter
    magician.ptp(mode=2, x=from_x, y=from_y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(0.5)

    # 4. Aller au-dessus de la destination
    magician.ptp(mode=2, x=to_x, y=to_y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(0.5)

    # 5. Descendre et relâcher
    magician.ptp(mode=2, x=to_x, y=to_y, z=COMMON_Z_AT, r=0)
    magician.wait(0.5)
    magician.set_endeffector_suctioncup(True, False)
    magician.wait(0.5)

    # 6. Remonter puis retour maison
    magician.ptp(mode=2, x=to_x, y=to_y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(0.5)
    magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
    magician.wait(0.5)


# ---------------------------------
# Programme principal
# ---------------------------------
# Position de départ
magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
magician.wait(0.5)

# Déplacer les cubes de la colonne 1 (j=0) vers la colonne 3 (j=2)
for i in range(3):  # lignes
    from_x = MATRIX_X0 + i * STEP      # colonne 1
    from_y = MATRIX_Y0 - 0 * STEP
    to_x   = from_x                    # même ligne
    to_y   = MATRIX_Y0 - 2 * STEP      # colonne 3
    pick_and_place(from_x, from_y, to_x, to_y)
