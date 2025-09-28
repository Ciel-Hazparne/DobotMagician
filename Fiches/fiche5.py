from DobotEDU import *

# ======================================
# === fiche5 : coordonnées calculées ===
# ======================================

def get_pick(row, col):
    X_ORIGIN = 200
    Y_ORIGIN = 100
    SIZE = 20
    x = X_ORIGIN - row * SIZE
    y = Y_ORIGIN + col * SIZE
    return x, y

# Test
x, y = get_pick(1, 2)
magician.ptp(1, x, y, 0, 0)
