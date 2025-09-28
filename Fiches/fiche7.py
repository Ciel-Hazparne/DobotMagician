from DobotEDU import *

# ==============================================
# === fiche7 : interaction avec le convoyeur ===
# ==============================================

def aspirer(state):
    magician.set_endeffector_suctioncup(enable=True, on=state)

# Lancer le convoyeur
magician.set_conveyor(0, True, 50)
magician.wait(1)

# Prendre le cube
magician.ptp(1, 200, 0, -45, 0)  # position du cube
aspirer(True)                     # ventouse ON
magician.wait(0.5)
magician.ptp(1, 200, 0, 30, 0)   # remonter à hauteur sécurité

# Déposer le cube sur le convoyeur
magician.ptp(1, 250, 0, 30, 0)   # position au-dessus du convoyeur
magician.ptp(1, 250, 0, -3, 0)   # descendre à hauteur dépôt
aspirer(False)                    # ventouse OFF
magician.wait(1)
magician.ptp(1, 250, 0, 30, 0)   # remonter à hauteur sécurité

# Stopper le convoyeur
magician.set_conveyor(0, False, 50)
