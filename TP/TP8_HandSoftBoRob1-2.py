# version: Python3
from DobotEDU import *
import time

# =======================================
# === TP8 - Coordination 2 Dobot Magician
# =======================================

# Connexion aux deux robots (⚠️ adapter les ports COM)
mag1 = Dobot(port="COM5")   # Robot 1
mag2 = Dobot(port="COM6")   # Robot 2


# ==================================================
# === Fonctions utilitaires communes
# ==================================================
def wait_for(magician, seconds):
    magician.wait(second=seconds)


def get_pose_xyzr(magician):
    pose = magician.get_pose()
    return pose['x'], pose['y'], pose['z'], pose['r']


def jump_to(magician, x, y, z, r=0, jump_height=50):
    x_cur, y_cur, z_cur, r_cur = get_pose_xyzr(magician)
    magician.ptp(mode=2, x=x_cur, y=y_cur, z=z_cur + jump_height, r=r_cur)
    wait_for(magician, 0.5)
    magician.ptp(mode=2, x=x, y=y, z=z + jump_height, r=r)
    wait_for(magician, 0.5)
    magician.ptp(mode=2, x=x, y=y, z=z, r=r)
    wait_for(magician, 0.5)


# ==================================================
# === Coordonnées Robot 1
# ==================================================
HOME1 = (259, 0, -8, 0)
ABPick1 = (242.47, 0, -35, 0)
ATPick1 = (242.47, 0, -44.51, 0)
ABPlace1 = (136.1, -225.96, -35, -92.09)
ATPlace1 = (136.1, -225.96, -40, -92.09)


# ==================================================
# === Coordonnées Robot 2
# ==================================================
HOME2 = (250, 0, -8, 0)
ABPick2 = (165.85, 212.07, 0, 0)
ATPick2 = (165.85, 212.07, -41, 0)
ABPlace2 = (216.44, -0.51, 0, 2.2)
ATPlace2 = (216.44, -0.51, -37.1, 2.2)


# ==================================================
# === Routine Pick & Place Robot 1
# ==================================================
def pick_and_place_robot1(magician):
    magician.ptp(mode=2, x=HOME1[0], y=HOME1[1], z=HOME1[2], r=HOME1[3])
    wait_for(magician, 0.5)

    magician.ptp(mode=2, x=ABPick1[0], y=ABPick1[1], z=ABPick1[2], r=ABPick1[3])
    wait_for(magician, 0.5)
    magician.ptp(mode=2, x=ATPick1[0], y=ATPick1[1], z=ATPick1[2], r=ATPick1[3])
    wait_for(magician, 0.5)

    magician.set_endeffector_suctioncup(enable=True, on=True)
    wait_for(magician, 0.5)

    jump_to(magician, *ABPlace1)
    magician.ptp(mode=2, x=ATPlace1[0], y=ATPlace1[1], z=ATPlace1[2], r=ATPlace1[3])
    wait_for(magician, 0.5)

    magician.set_endeffector_suctioncup(enable=True, on=False)
    wait_for(magician, 0.5)

    magician.ptp(mode=2, x=ABPlace1[0], y=ABPlace1[1], z=ABPlace1[2], r=ABPlace1[3])
    wait_for(magician, 0.5)
    magician.ptp(mode=2, x=HOME1[0], y=HOME1[1], z=HOME1[2], r=HOME1[3])
    wait_for(magician, 0.5)


# ==================================================
# === Routine Pick & Place Robot 2
# ==================================================
def pick_and_place_robot2(magician):
    magician.ptp(mode=2, x=HOME2[0], y=HOME2[1], z=HOME2[2], r=HOME2[3])
    wait_for(magician, 0.5)

    magician.ptp(mode=2, x=ABPick2[0], y=ABPick2[1], z=ABPick2[2], r=ABPick2[3])
    wait_for(magician, 0.5)
    magician.ptp(mode=2, x=ATPick2[0], y=ATPick2[1], z=ATPick2[2], r=ATPick2[3])
    wait_for(magician, 0.5)

    magician.set_endeffector_suctioncup(enable=True, on=True)
    wait_for(magician, 0.5)

    jump_to(magician, *ABPlace2)
    magician.ptp(mode=2, x=ATPlace2[0], y=ATPlace2[1], z=ATPlace2[2], r=ATPlace2[3])
    wait_for(magician, 0.5)

    magician.set_endeffector_suctioncup(enable=True, on=False)
    wait_for(magician, 0.5)

    magician.ptp(mode=2, x=ABPlace2[0], y=ABPlace2[1], z=ABPlace2[2], r=ABPlace2[3])
    wait_for(magician, 0.5)
    magician.ptp(mode=2, x=HOME2[0], y=HOME2[1], z=HOME2[2], r=HOME2[3])
    wait_for(magician, 0.5)


# ==================================================
# === Programme principal coordonné
# ==================================================
print("Démarrage coordination robots")

pick_and_place_robot1(mag1)      # Robot 1 exécute son Pick & Place
print("Robot 1 a terminé, démarrage Robot 2")

time.sleep(1)                    # Laisse 1 s entre les deux
pick_and_place_robot2(mag2)      # Robot 2 démarre ensuite
print("Robot 2 a terminé")

# Option : retour home final synchronisé
mag1.set_ptp_cmd(x=HOME1[0], y=HOME1[1], z=HOME1[2], r=HOME1[3])
mag2.set_ptp_cmd(x=HOME2[0], y=HOME2[1], z=HOME2[2], r=HOME2[3])

print("Coordination terminée")