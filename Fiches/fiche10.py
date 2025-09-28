from DobotEDU import *

# =============================================
# === fiche10 : intégration des compétences ===
# =============================================

# Constantes
CUBE_SIZE = 25
CUBE_HEIGHT = 25
Z_SAFE = 30
Z_PICK = -45
Z_PLACE = -3
CONVEYOR_SPEED = 60

X_ORIGIN = 172
Y_ORIGIN = 116
X_PLACE = 259
Y_PLACE = 0

#fonctions principales
def move_to(x, y, z):
    magician.ptp(1, x, y, z, 0)
    magician.wait(0.5)

def pick(x, y):
    move_to(x, y, Z_SAFE)
    move_to(x, y, Z_PICK)
    magician.set_endeffector_suctioncup(True, True)
    magician.wait(0.5)
    move_to(x, y, Z_SAFE)

def place():
    move_to(X_PLACE, Y_PLACE, Z_SAFE)
    move_to(X_PLACE, Y_PLACE, Z_PLACE)
    magician.set_endeffector_suctioncup(True, False)
    magician.wait(1)

def get_pick(row, col):
    x = X_ORIGIN - row * CUBE_SIZE
    y = Y_ORIGIN + col * CUBE_SIZE
    return x, y

# Programme principal
magician.set_conveyor(0, True, CONVEYOR_SPEED)
magician.wait(1)

for row in range(3):
    for col in range(3):
        x, y = get_pick(row, col)
        pick(x, y)
        place()

magician.set_conveyor(0, False, CONVEYOR_SPEED)
