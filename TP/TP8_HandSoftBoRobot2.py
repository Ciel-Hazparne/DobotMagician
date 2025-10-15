# version: Python3
from DobotEDU import *

# ============================
# === TP8_HandHardBoRobot1 ===
# ============================

# Variable partagée
signal = 0


# -------------------------------
# Fonctions utilitaires
# -------------------------------

def wait_for(seconds):
    magician.wait(second=seconds)


def get_pose_xyzr():
    """Renvoie x, y, z, r actuels sous forme de dictionnaire compatible DobotLab."""
    pose = magician.get_pose()  # renvoie dict {'x':..., 'y':..., 'z':..., 'r':...}
    return pose['x'], pose['y'], pose['z'], pose['r']


def jump_to(x, y, z, r=0, jump_height=50):
    """
    Déplacement par 'saut' : monte, se déplace horizontalement, descend.
    """
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
HOME = (250, 0, -8, 0)
ABPick = (165.85, 212.07, 0, 0)
ATPick = (165.85, 212.07, -41, 0)
ABPlace = (216.44, -0.51, 0, 2.2)
ATPlace = (216.44, -0.51, -37.1, 2.2)


# -------------------------------
# Routine Pick & Place
# -------------------------------
def pick_and_place():
    # Étape 1 : position de départ
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=HOME[3])
    wait_for(0.5)

    # Étape 2-3 : aller au-dessus de l'objet puis à l'objet
    magician.ptp(mode=2, x=ABPick[0], y=ABPick[1], z=ABPick[2], r=ABPick[3])
    wait_for(0.5)
    magician.ptp(mode=2, x=ATPick[0], y=ATPick[1], z=ATPick[2], r=ATPick[3])
    wait_for(0.5)

    # Étape 4 : activer l'aspiration
    magician.set_endeffector_suctioncup(enable=True, on=True)
    wait_for(0.5)

    # Étape 5-7 : déplacement vers la zone de dépôt avec Jump
    jump_to(*ABPlace)
    magician.ptp(mode=2, x=ATPlace[0], y=ATPlace[1], z=ATPlace[2], r=ATPlace[3])
    wait_for(0.5)

    # Étape 8 : relâcher l'objet
    magician.set_endeffector_suctioncup(enable=True, on=False)
    wait_for(0.5)

    # Étape 9-10 : remonter et revenir au départ
    magician.ptp(mode=2, x=ABPlace[0], y=ABPlace[1], z=ABPlace[2], r=ABPlace[3])
    wait_for(0.5)
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=HOME[3])
    wait_for(0.5)


# -------------------------------
# programme principal
# -------------------------------

# Robot 2 - Attente signal puis Pick & Place
if signal == 1:
    pick_and_place()

# Remise à zéro du signal
signal = 0
print("Robot 2 a terminé et remis signal =", signal)

# -------------------------------
# Boucle finie
# -------------------------------
# N = 5
# for i in range(N):
#    pick_and_place()

# -------------------------------
# Boucle infinie (optionnelle)
# -------------------------------
# while True:
#     pick_and_place()
