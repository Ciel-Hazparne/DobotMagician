# version: Python3
from DobotEDU import *

# ==========================
# ===== TP2_PnP_Jump_Loop ======
# ==========================

# -------------------------------
# Fonctions et repères
# -------------------------------

def jump_to(x, y, z, r=0, jump_height=50):
    """
    Déplacement par 'saut' : monte, se déplace horizontalement, descend.
    jump_height = hauteur du saut au-dessus des obstacles.
    """
    pose = magician.get_pose()  # dictionnaire avec {"x":..., "y":..., "z":..., "r":...}
    x_cur = pose["x"]
    y_cur = pose["y"]
    z_cur = pose["z"]
    r_cur = pose["r"]

    # Monter depuis la position actuelle
    magician.ptp(mode=2, x=x_cur, y=y_cur, z=z_cur + jump_height, r=r_cur)
    magician.wait(second=0.5)

    # Aller horizontalement à la position cible en restant en hauteur
    magician.ptp(mode=2, x=x, y=y, z=z + jump_height, r=r)
    magician.wait(second=0.5)

    # Descendre à la hauteur finale
    magician.ptp(mode=2, x=x, y=y, z=z, r=r)
    magician.wait(second=0.5)

# Coordonnées repères
HOME    = (170,  33,   0)   # Position de sécurité
ABPick  = (274,  33, -35)   # Au-dessus de l’objet
ATPick  = (274,  33, -55)   # À l’objet
ABPlace = (206,  33, -35)   # Au-dessus de la zone de dépôt
ATPlace = (206,  33, -55)   # À la zone de dépôt

# -------------------------------
# Routine Pick & Place
# -------------------------------

def pick_and_place():
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=0)
    magician.wait(second=1)

    magician.ptp(mode=2, x=ABPick[0], y=ABPick[1], z=ABPick[2], r=0)
    magician.wait(second=0.5)

    magician.ptp(mode=2, x=ATPick[0], y=ATPick[1], z=ATPick[2], r=0)
    magician.wait(second=0.5)

    magician.set_endeffector_suctioncup(enable=True, on=True)
    magician.wait(second=1)

    jump_to(ABPlace[0], ABPlace[1], ABPlace[2], r=0)
    magician.ptp(mode=2, x=ATPlace[0], y=ATPlace[1], z=ATPlace[2], r=0)
    magician.wait(second=0.5)

    magician.set_endeffector_suctioncup(enable=True, on=False)
    magician.wait(second=1)

    magician.ptp(mode=2, x=ABPlace[0], y=ABPlace[1], z=ABPlace[2], r=0)
    magician.wait(second=0.5)

    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=0)
    magician.wait(second=1)

# -------------------------------
# Boucle finie
# -------------------------------

N = 5
for i in range(N):
    pick_and_place()

# -------------------------------
# Boucle infinie : répéter indéfiniment
# -------------------------------

# Décommenter pour tester la boucle infinie
# while True:
#     pick_and_place()