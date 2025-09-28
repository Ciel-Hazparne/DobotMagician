from DobotEDU import *

# ===================================
# === fiche1 : quelques commandes ===
# ===================================

# Déplacer le bras à la position en mode 1 (x=200, y=0, z=0, r=0)
magician.ptp(1, 200, 0, 0, 0)

# Attendre 2 secondes
magician.wait(2)

# Activer la pompe (suction cup ON)
magician.set_endeffector_suctioncup(True, True)

# Attendre encore 2 secondes
magician.wait(2)

# Désactiver la pompe (suction cup OFF)
magician.set_endeffector_suctioncup(True, False)
