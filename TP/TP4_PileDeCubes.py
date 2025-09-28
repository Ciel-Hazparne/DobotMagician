from DobotEDU import *

# ============================
# ===== TP4_PileDeCubes ======
# ============================

# ---------------------------------
# Constantes
# ---------------------------------
HOME_X, HOME_Y, HOME_Z = (200, 0, 50)
COMMON_Z_ABOVE = 50
COMMON_Z_AT    = 10
MATRIX_X0, MATRIX_Y0 = (150, 100)
STEP = 35
STACK_X, STACK_Y = (250, -150)
STACK_HEIGHT = 25  # taille d’un cube en Z

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
# Routine empiler les cubes
# ---------------------------------
def stack_cubes():
    k = 0
    for i in range(3):
        for j in range(3):
            x_src = MATRIX_X0 + j * STEP
            y_src = MATRIX_Y0 + i * STEP
            z_place = COMMON_Z_AT + k * STACK_HEIGHT
            z_above = COMMON_Z_ABOVE + k * STACK_HEIGHT

            # Prendre le cube
            magician.ptp(mode=2, x=x_src, y=y_src, z=COMMON_Z_ABOVE, r=0)
            magician.wait(second=0.5)
            magician.ptp(mode=2, x=x_src, y=y_src, z=COMMON_Z_AT, r=0)
            magician.wait(second=0.5)
            magician.set_endeffector_suctioncup(enable=True, on=True)
            magician.wait(second=0.5)

            # Déposer dans la pile
            jump_to(STACK_X, STACK_Y, z_above)
            magician.ptp(mode=2, x=STACK_X, y=STACK_Y, z=z_place, r=0)
            magician.wait(second=0.5)
            magician.set_endeffector_suctioncup(enable=True, on=False)
            magician.wait(second=0.5)
            magician.ptp(mode=2, x=STACK_X, y=STACK_Y, z=z_above, r=0)
            magician.wait(second=0.5)

            k += 1

# ---------------------------------
# Programme principal
# ---------------------------------
# Position de départ
magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
magician.wait(second=0.5)

# Lancer la pile de cubes
stack_cubes()