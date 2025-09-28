# version: Python3
from DobotEDU import *

# ============================
# === TP7_HandHardBfRobot2 ===
# ============================

# -------------------------------
# Fonctions utilitaires
# -------------------------------
def wait_for(seconds):
    magician.wait(second=seconds)

def get_pose_xyzr():
    """Renvoie x, y, z, r actuels sous forme de tuple."""
    pose = magician.get_pose()
    return pose['x'], pose['y'], pose['z'], pose['r']

def jump_to(x, y, z, r=0, jump_height=50):
    """Déplacement par 'saut' : monte, se déplace horizontalement, descend."""
    x_cur, y_cur, z_cur, r_cur = get_pose_xyzr()
    # Monter
    magician.ptp(mode=2, x=x_cur, y=y_cur, z=z_cur + jump_height, r=r_cur)
    wait_for(0.5)
    # Horizontal en hauteur
    magician.ptp(mode=2, x=x, y=y, z=z + jump_height, r=r)
    wait_for(0.5)
    # Descendre
    magician.ptp(mode=2, x=x, y=y, z=z, r=r)
    wait_for(0.5)

# -------------------------------
# Coordonnées repères
# -------------------------------
HOME     = (200, 0, 50, 0)
ABPick   = (150, 100, 50, 0)
ATPick   = (150, 100, 10, 0)
ABPlace  = (250, -100, 50, 0)
ATPlace  = (250, -100, 10, 0)

# -------------------------------
# Routine Pick & Place
# -------------------------------
def pick_and_place():
    # Position de départ
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=HOME[3])
    wait_for(0.5)

    # Aller au-dessus de l'objet puis à l'objet
    magician.ptp(mode=2, x=ABPick[0], y=ABPick[1], z=ABPick[2], r=ABPick[3])
    wait_for(0.5)
    magician.ptp(mode=2, x=ATPick[0], y=ATPick[1], z=ATPick[2], r=ATPick[3])
    wait_for(0.5)

    # Activer l'aspiration
    magician.set_endeffector_suctioncup(enable=True, on=True)
    wait_for(0.5)

    # Déplacement vers la zone de dépôt avec Jump
    jump_to(*ABPlace)
    magician.ptp(mode=2, x=ATPlace[0], y=ATPlace[1], z=ATPlace[2], r=ATPlace[3])
    wait_for(0.5)

    # Relâcher l'objet
    magician.set_endeffector_suctioncup(enable=True, on=False)
    wait_for(0.5)

    # Remonter et retourner au départ
    magician.ptp(mode=2, x=ABPlace[0], y=ABPlace[1], z=ABPlace[2], r=ABPlace[3])
    wait_for(0.5)
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=HOME[3])
    wait_for(0.5)

# -------------------------------
# Boucle finie
# -------------------------------
N = 5
for i in range(N):
    pick_and_place()

# -------------------------------
# Boucle infinie (optionnelle)
# -------------------------------
# while True:
#     pick_and_place()
