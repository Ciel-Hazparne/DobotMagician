# version: Python3
from DobotEDU import *

# ======================
# === ==TP1_Pick&Place ======
# ======================

# === Définition des coordonnées (exemple, à remplacer par vos valeurs) ===
HOME = (170, 33, 0)                          # Position de sécurité
ABPick = (274, 33, -35)                      # Au-dessus de l’objet
ATPick = (274, 33, -55)                      # À l’objet
ABPLace = (206, 33, -35)                     # Au-dessus de la zone de dépôt
ATPLace = (206, 33, -55)                     # À la zone de dépôt

# 1. Aller à la position Home (sécurité → JUMP)
magician.ptp(mode=0, x=HOME[0], y=HOME[1], z=HOME[2], r=0)
magician.wait(second=1)

# ZONE OBJET
# 2. Aller au-dessus de l’objet (sécurité → JUMP)
magician.ptp(mode=0, x=ABPick[0], y=ABPick[1], z=ABPick[2], r=0)
magician.wait(second=1)

# 3. Descendre jusqu’à l’objet (linéaire → MOVL)
magician.ptp(mode=2, x=ATPick[0], y=ATPick[1], z=ATPick[2], r=0)
magician.wait(second=1)

# 4. Activer la ventouse
magician.set_endeffector_suctioncup(enable=True, on=True)
magician.wait(second=1)

# 5. Remonter au-dessus de l’objet (linéaire → MOVL)
magician.ptp(mode=2, x=ABPick[0], y=ABPick[1], z=ABPick[2], r=0)
magician.wait(second=1)

# ZONE DEPOT
# 6. Déplacer au-dessus de la zone de dépôt (sécurité → JUMP)
magician.ptp(mode=0, x=ABPLace[0], y=ABPLace[1], z=ABPLace[2], r=0)
magician.wait(second=1)

# 7. Descendre au point de dépôt (linéaire → MOVL)
magician.ptp(mode=2, x=ATPLace[0], y=ATPLace[1], z=ATPLace[2], r=0)
magician.wait(second=1)

# 8. Désactiver la ventouse
magician.set_endeffector_suctioncup(enable=True, on=False)
magician.wait(second=1)

# 9. Remonter au-dessus de la zone de dépôt (linéaire → MOVL)
magician.ptp(mode=2, x=ABPLace[0], y=ABPLace[1], z=ABPLace[2], r=0)
magician.wait(second=1)

# 10. Retourner à Home (sécurité → JUMP)
magician.ptp(mode=0, x=HOME[0], y=HOME[1], z=HOME[2], r=0)
magician.wait(second=1)