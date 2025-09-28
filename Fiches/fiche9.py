from DobotEDU import *

# =======================
# === fiche9 : Listes ===
# =======================

# Définir les positions (X, Y, Z)
positions = [
    (205, 0, -35),   # position 0
    (240, 0, -35),   # position 1
    (275, 35, -35),  # position 5
    (240, 70, -35),  # position 7
    (205, 70, -35)   # position 6
]

# Fonction pour aller à une position
def go_to(pos):
    magician.ptp(0, pos[0], pos[1], pos[2], 0)
    magician.wait(0.5)

# Parcourir toutes les positions de la liste
for pos in positions_U:
    go_to(pos)

# Retour à HOME
go_to((170, 33, 0))