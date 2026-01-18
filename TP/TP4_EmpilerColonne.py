from DobotEDU import *

# ==========================
# === TP4_EmpilerColonne ===
# ==========================

# ---------------------------------
# Constantes
# ---------------------------------
HOME_X, HOME_Y, HOME_Z = (218.5, 78, 10)    # position de repos au dessus du carré bleu
COMMON_Z_ABOVE = 10                         # hauteur d’approche
COMMON_Z_AT = -45                           # hauteur de saisie/dépôt
STACK_HEIGHT = 30                           # hauteur d’un cube en mm (avec 5mm de sécurité)

# Grille (position 0)
MATRIX_X0, MATRIX_Y0 = (183, 34.5)
STEP = 35     # entraxe entre cubes en mm

# Coordonnées de la case 0 (destination)
DEST_X = MATRIX_X0 + 0 * STEP   # j=0
DEST_Y = MATRIX_Y0 - 0 * STEP   # i=0

# ---------------------------------
# Routine Pick & Place pour un cube
# ---------------------------------
def pick_and_place(from_x, from_y, to_x, to_y, stack_level=0):
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

    # 5. Descendre à la bonne hauteur pour empiler
    z_drop = COMMON_Z_AT + stack_level * STACK_HEIGHT
    magician.ptp(mode=2, x=to_x, y=to_y, z=z_drop, r=0)
    magician.wait(0.5)
    magician.set_endeffector_suctioncup(True, False)
    magician.wait(0.5)

    # 6. Remonter puis retour HOME
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

# Déplacer les cubes de la colonne de droite (cases 2,5,8) vers la case 0 en pile
for i in range(3):  # lignes 0,1,2
    from_x = MATRIX_X0 + i * STEP      # lignes i=0..2
    from_y = MATRIX_Y0 - 2 * STEP      # colonne 2 (j=2)
    pick_and_place(from_x, from_y, DEST_X, DEST_Y, stack_level=i)