from DobotEDU import *

# ==========================
# === TP4_Palettisation ====
# ==========================

# ---------------------------------
# Constantes
# ---------------------------------
HOME_X, HOME_Y, HOME_Z = (218.5, 78, 0)    # position de reposau dessus du carré bleu
COMMON_Z_ABOVE = 10                         # hauteur d’approche
COMMON_Z_AT = -45                       # hauteur de saisie/dépôt

# Grille (position 0)
MATRIX_X0, MATRIX_Y0 = (183, 34.5)
STEP = 35     # entraxe entre cubes en mm

# Emplacement d eprise de cube
PLACE_X, PLACE_Y = (77, -180)   # à ajuster selon votre espace


# ---------------------------------
# Fonction jump_to sécurisée
# ---------------------------------
def jump_to(x, y, z, r=0, jump_height=50):
    pose = magician.get_pose()
    x_cur, y_cur, z_cur, r_cur = pose["x"], pose["y"], pose["z"], pose["r"]

    # Monter depuis la position actuelle
    magician.ptp(mode=2, x=x_cur, y=y_cur, z=z_cur + jump_height, r=r_cur)
    magician.wait(second=0.5)

    # Aller horizontalement au-dessus de la cible
    magician.ptp(mode=2, x=x, y=y, z=z + jump_height, r=r)
    magician.wait(second=0.5)

    # Descendre à la position finale
    magician.ptp(mode=2, x=x, y=y, z=z, r=r)
    magician.wait(second=0.5)

# ---------------------------------
# Routine de distribution depuis la pile commune
# ---------------------------------
def distribute_from_common():
    for i in range(3):
        for j in range(3):
            x_dst = MATRIX_X0 + j * STEP
            y_dst = MATRIX_Y0 + i * STEP

            # Prendre dans la pile commune
            magician.ptp(mode=2, x=PLACE_X, y=PLACE_Y, z=COMMON_Z_ABOVE, r=0)
            magician.wait(second=0.5)
            magician.ptp(mode=2, x=PLACE_X, y=PLACE_Y, z=COMMON_Z_AT, r=0)
            magician.wait(second=0.5)
            magician.set_endeffector_suctioncup(enable=True, on=True)
            magician.wait(second=0.5)

            # Déposer dans la matrice
            jump_to(x_dst, y_dst, COMMON_Z_ABOVE)
            magician.ptp(mode=2, x=x_dst, y=y_dst, z=COMMON_Z_AT, r=0)
            magician.wait(second=0.5)
            magician.set_endeffector_suctioncup(enable=True, on=False)
            magician.wait(second=0.5)
            magician.ptp(mode=2, x=x_dst, y=y_dst, z=COMMON_Z_ABOVE, r=0)
            magician.wait(second=0.5)

# ---------------------------------
# Programme principal
# ---------------------------------
# Retour à la position Home
magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
magician.wait(second=0.5)

# Lancer directement la palettisation
distribute_from_common()