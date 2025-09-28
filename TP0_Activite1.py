# version: Python3
from DobotEDU import *

# ======================
# ===TP0_Activite1 =====
# ======================

# === Définition des coordonnées (exemple, à remplacer par vos valeurs) ===
ABP0 = (170, 33, 0)                        # Position d’attente
HOME = (170, 33, 0)                        # Position HOME
ABP1 = (274, 33, -35)                      # Au-dessus de la position 1
ATP7 = (274, 33, -35)                      # Au-dessus de la position 7

# 1. Aller à la position Home (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=HOME[0], y=HOME[1], z=HOME[2], r=0)
magician.wait(second=0.5)

# 2. Aller à la position 1 (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=ABP1[0], y=ABP1[1], z=ABP1[2], r=0)
magician.wait(second=0.5)

# 3. Aller à la position 7 (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=ABP1[0], y=ABP1[1], z=ABP1[2], r=0)
magician.wait(second=0.5)

# 4. Aller à la position Home (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=HOME[0], y=HOME[1], z=HOME[2], r=0)
magician.wait(second=0.5)

# 5. Aller à la position 7 (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=ABP1[0], y=ABP1[1], z=ABP1[2], r=0)
magician.wait(second=1)

# 6. Aller à la position 1 (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=ABP1[0], y=ABP1[1], z=ABP1[2], r=0)
magician.wait(second=0.5)

# 7. Aller à la position Home (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=HOME[0], y=HOME[1], z=HOME[2], r=0)