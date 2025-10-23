from DobotEDU import *

# ============================
# === TP4_Matrice-1FDC =====
# ============================

# ---------------------------------
# Constantes
# ---------------------------------
HOME_X, HOME_Y, HOME_Z = (200, 0, 50)
COMMON_Z_ABOVE = 50
COMMON_Z_AT    = 10

MATRIX_X0, MATRIX_Y0 = (150, 100)
STEP = 35
PLACE_X, PLACE_Y = (250, -100)

# ---------------------------------
# Fonction jump_to sécurisée
# ---------------------------------
def jump_to(x, y, z, r=0, jump_height=50):
    pose = magician.get_pose()
    x_cur, y_cur, z_cur, r_cur = pose["x"], pose["y"], pose["z"], pose["r"]

    magician.ptp(mode=2, x=x_cur, y=y_cur, z=z_cur + jump_height, r=r_cur)
    magician.wait(second=0.5)
    magician.ptp(mode=2, x=x, y=y, z=z + jump_height, r=r)
    magician.wait(second=0.5)
    magician.ptp(mode=2, x=x, y=y, z=z, r=r)
    magician.wait(second=0.5)

# ---------------------------------
# Fonction attente bouton
# ---------------------------------
def wait_for_button(input_port=5):
    """Attend que le bouton branché sur DI[input_port] soit pressé (état haut)."""
    io_map = {5: "DI_05", 6: "DI_06"}  # mapper le port DobotLab
    io_pin = io_map.get(input_port, "DI_05")
    while magician.get_di(io=io_pin) == 0:
        magician.wait(second=0.1)

# ---------------------------------
# Routine Pick & Place pour un cube
# ---------------------------------
def pick_and_place(x, y):
    magician.ptp(mode=2, x=x, y=y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(second=0.5)
    magician.ptp(mode=2, x=x, y=y, z=COMMON_Z_AT, r=0)
    magician.wait(second=0.5)
    magician.set_endeffector_suctioncup(enable=True, on=True)
    magician.wait(second=0.5)

    jump_to(PLACE_X, PLACE_Y, COMMON_Z_ABOVE)
    magician.ptp(mode=2, x=PLACE_X, y=PLACE_Y, z=COMMON_Z_AT, r=0)
    magician.wait(second=0.5)
    magician.set_endeffector_suctioncup(enable=True, on=False)
    magician.wait(second=0.5)
    magician.ptp(mode=2, x=PLACE_X, y=PLACE_Y, z=COMMON_Z_ABOVE, r=0)
    magician.wait(second=0.5)
    magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
    magician.wait(second=0.5)

# ---------------------------------
# Programme principal
# ---------------------------------
# Position de départ
magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
magician.wait(second=0.5)

# Attendre appui bouton pour lancer la routine
wait_for_button(5)

# Parcours de la matrice 3x3
for i in range(3):
    for j in range(3):
        x = MATRIX_X0 + j * STEP
        y = MATRIX_Y0 + i * STEP
        pick_and_place(x, y)
