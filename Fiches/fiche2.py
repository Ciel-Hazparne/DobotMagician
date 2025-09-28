from DobotEDU import *

# ========================================
# === fiche2 : variables et constantes ===
# ========================================

# Constante
Z_SAFE = 50

# Variables
x = 250
y = 0
z = 0

# Déplacement principal
magician.ptp(1, x, y, z, 0)

# Montée de sécurité
magician.ptp(1, x, y, Z_SAFE, 0)
