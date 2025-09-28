from DobotEDU import *

# ===================================
# === fiche8 : condition if ===
# ===================================

# Fonction simplifiée pour la ventouse
def aspirer(state):
    magician.set_endeffector_suctioncup(True, state)


Z_SAFE = 30  # hauteur de sécurité
Z_PICK = -45  # hauteur de préhension
Z_PLACE = -3  # hauteur de dépose sur le tapis

# Parcourir la grille 3x3
for row in range(3):
    for col in range(3):
        if row == 0:  # seulement la première ligne
            # Calcul des coordonnées du cube
            x = 200 - row * 20
            y = 100 + col * 20

            # Prendre le cube
            magician.ptp(1, x, y, Z_SAFE, 0)
            magician.ptp(1, x, y, Z_PICK, 0)
            aspirer(True)
            magician.ptp(1, x, y, Z_SAFE, 0)

            # Déposer le cube
            magician.ptp(1, 250, 0, Z_SAFE, 0)  # position dépôt
            magician.ptp(1, 250, 0, Z_PLACE, 0)
            aspirer(False)
            magician.ptp(1, 250, 0, Z_SAFE, 0)
