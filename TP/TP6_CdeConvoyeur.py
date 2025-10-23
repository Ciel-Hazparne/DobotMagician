# version: Python3
from DobotEDU import *

# ============================
# ===== TP6_CdeConvoyeur =====
# ============================

# Positions de base
HOME = (259, 0, 50)  # position de repos au dessus du tapis
ABPick = (171.24, 164.06, 0)
ATPick = (171.24, 164.06, -44.74)
CONVEYOR_ABOVE = (264.7, 0, 50)
CONVEYOR_PLACE = (264.7, 0, 20)

# --- Fonctions utilitaires ---
def wait_for(seconds):
    magician.wait(second=seconds)


def jump_to(x, y, z, r=0, jump_height=20):
    pose = magician.get_pose()
    x_cur, y_cur, z_cur, r_cur = pose["x"], pose["y"], pose["z"], pose["r"]

    # Monter depuis la position actuelle
    magician.ptp(mode=2, x=x_cur, y=y_cur, z=z_cur + jump_height, r=r_cur)
    wait_for(0.5)

    # Aller horizontalement à la cible
    magician.ptp(mode=2, x=x, y=y, z=z + jump_height, r=r)
    wait_for(0.5)

    # Descendre à la hauteur finale
    magician.ptp(mode=2, x=x, y=y, z=z, r=r)
    wait_for(0.5)


# --- Routine Pick & Place vers convoyeur ---
def pick_and_place_to_conveyor():
    # Aller au cube
    magician.ptp(mode=2, x=ABPick[0], y=ABPick[1], z=ABPick[2], r=0)
    wait_for(0.5)
    magician.ptp(mode=2, x=ATPick[0], y=ATPick[1], z=ATPick[2], r=0)
    wait_for(0.5)
    magician.set_endeffector_suctioncup(enable=True, on=True)
    wait_for(0.5)

    # Relever le cube
    magician.ptp(mode=2, x=ABPick[0], y=ABPick[1], z=ABPick[2], r=0)
    wait_for(0.5)

    # Déplacer au-dessus du convoyeur
    jump_to(CONVEYOR_ABOVE[0], CONVEYOR_ABOVE[1], CONVEYOR_ABOVE[2])

    # Descendre au-dessus du convoyeur
    magician.ptp(mode=2, x=CONVEYOR_PLACE[0], y=CONVEYOR_PLACE[1], z=CONVEYOR_PLACE[2], r=0)

    # Déposer
    magician.set_endeffector_suctioncup(enable=True, on=False)
    wait_for(0.5)

    # Retour HOME
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=0)
    wait_for(0.5)


# --- Gestion du convoyeur ---
def manage_conveyor():
    # Démarrer le convoyeur (Stepper1)
    magician.set_converyor(index=magician.Stepper1, enable=True, speed=100.0)

    # activer les capteur version 2 sur GP4
    magician.set_infrared_sensor(port=4, enable=True, version=1)

    while True:
        detect = magician.get_infrared_sensor(port=4)
        print("Détection IR:", detect)

        if detect["status"] == 1:  # cube détecté
            break

        wait_for(0.1)


    # Arrêter le convoyeur
    magician.set_converyor(index=magician.Stepper1, enable=False, speed=0.0)
    # désactiver les capteur version 2 sur GP4
    magician.set_infrared_sensor(port=4, enable=False, version=1)

    # Pause 2s pour traitement
    wait_for(2)

    # Redémarrer pour évacuation
    magician.set_converyor(index=magician.Stepper1, enable=True, speed=100.0)
    wait_for(3)  # ajuster selon vitesse tapis
    magician.set_converyor(index=magician.Stepper1, enable=False, speed=0.0)


# --- Programme principal ---
pick_and_place_to_conveyor()
manage_conveyor()