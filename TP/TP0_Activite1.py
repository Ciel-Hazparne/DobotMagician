# version: Python3
from DobotEDU import *

# ====================
# ===TP0_Activite1 ===
# ====================

# === Définition des coordonnées (exemple, à remplacer par vos valeurs) ===
HOME = (218.5, 78, -60)              # position HOME au dessus du carré bleu
ABP1 = (179.44, 0, -60)              # Au-dessus de la position 1
ABP7 = (251, 0, -60)                 # Au-dessus de la position 7

# 1. Aller à la position Home (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=HOME[0], y=HOME[1], z=HOME[2], r=0)
magician.wait(second=0.5)

# 2. Aller à la position 1 (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=ABP1[0], y=ABP1[1], z=ABP1[2], r=0)
magician.wait(second=0.5)

# 3. Aller à la position 7 (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=ABP7[0], y=ABP7[1], z=ABP7[2], r=0)
magician.wait(second=0.5)

# 4. Aller à la position Home (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=HOME[0], y=HOME[1], z=HOME[2], r=0)
magician.wait(second=0.5)

# 5. Aller à la position 7 (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=ABP7[0], y=ABP7[1], z=ABP7[2], r=0)
magician.wait(second=1)

# 6. Aller à la position 1 (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=ABP1[0], y=ABP1[1], z=ABP1[2], r=0)
magician.wait(second=0.5)

# 7. Aller à la position Home (sécurité → JUMP) et attendre 0,5s
magician.ptp(mode=0, x=HOME[0], y=HOME[1], z=HOME[2], r=0)