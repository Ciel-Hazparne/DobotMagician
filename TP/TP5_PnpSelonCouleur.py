# version: Python3
from DobotEDU import *

# ============================
# ===== TP5_PnpSelonCouleur ===
# ============================

# Positions de base
HOME_X, HOME_Y, HOME_Z = (259, 0, 50)    # position de repos au dessus du tapis
ABPick_X, ABPick_Y, ABPick_Z = (161.5, 178.27, 0)
ATPick_X, ATPick_Y, ATPick_Z = (161.5, 178.27, -44.74)
ABPlace_X, ABPlace_Y, ABPlace_Z = (33.75, -178.47, 0)
ATPlace_X, ATPlace_Y, ATPlace_Z = (33.75, -178.47, -44)

# Capteur de couleur
SENSOR_X, SENSOR_Y, SENSOR_ABOVE_Z = (191.28, -2.69, 50)  # 50 =>hauteur de sécurité, hauteur idéale 8-12 mm => 40.17

# Grille 3x3
STEP = 35
CUBE_SIZE = 25
ROW_BLUE = 0
ROW_GREEN = 1
ROW_RED = 2

# Suivi de la prochaine colonne libre pour chaque ligne
next_col = {ROW_RED: 0, ROW_GREEN: 0, ROW_BLUE: 0}

# -----------------------------
# Fonctions utilitaires
# -----------------------------
def wait_for(seconds):
    magician.wait(second=seconds)

def get_pose_xyzr():
    p = magician.get_pose()  # renvoie un dictionaire
    return p["x"], p["y"], p["z"], p.get("r", 0)

def jump_to(x, y, z, r=0, jump_height=0):
    """
    Déplace le robot en 'sautant' : monte, traverse, descend.
    """
    x_cur, y_cur, z_cur, r_cur = get_pose_xyzr()
    # monter verticalement
    magician.ptp(mode=2, x=x_cur, y=y_cur, z=z_cur + jump_height, r=r_cur)
    wait_for(0.4)
    # translation en hauteur
    magician.ptp(mode=2, x=x, y=y, z=z + jump_height, r=r)
    wait_for(0.4)
    # descendre
    magician.ptp(mode=2, x=x, y=y, z=z, r=r)
    wait_for(0.4)

def read_color_tolerant():
    magician.set_color_sensor(port=2, enable=True, version=1)
    magician.wait(second=0.1)
    _ = magician.get_color_sensor()  # purge première lecture toujours fausse d'après le test TP5_RetourCaptCouleu

    readings = []
    for _ in range(3):
        c = magician.get_color_sensor()
        if isinstance(c, dict):
            readings.append(c)
        magician.wait(second=0.1)

    magician.set_color_sensor(port=2, enable=False, version=1)

    if not readings:
        return None

    red_count = sum(1 for r in readings if r.get('red') == 1)
    green_count = sum(1 for r in readings if r.get('green') == 1)
    blue_count = sum(1 for r in readings if r.get('blue') == 1)

    if red_count >= 2:
        return "RED"
    elif green_count >= 2:
        return "GREEN"
    elif blue_count >= 2:
        return "BLUE"
    return None

def pick_and_place_with_color(x_pick, y_pick):
    # Aller au-dessus du cube (approche)
    magician.ptp(mode=2, x=x_pick, y=y_pick, z=ABPick_Z, r=0)
    wait_for(0.3)
    # Descendre pour saisir
    magician.ptp(mode=2, x=x_pick, y=y_pick, z=ATPick_Z, r=0)
    wait_for(0.3)
    # Activer la ventouse
    magician.set_endeffector_suctioncup(enable=True, on=True)
    wait_for(0.6)
    # Remonter au-dessus de la prise
    magician.ptp(mode=2, x=x_pick, y=y_pick, z=ABPick_Z, r=0)
    wait_for(0.3)
    # Aller  à HOME pour éviter la mise en sécurité x)
    magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
    wait_for(0.3)
    # Amener le cube au capteur couleur
    jump_to(SENSOR_X, SENSOR_Y, SENSOR_ABOVE_Z)
    # activer  le capteur de couleur
    magician.set_color_sensor(port=2, enable=True, version=1)
    wait_for(0.1)
    # Descendre pour être à la bonne distance (10 mm)
    magician.ptp(mode=2, x=SENSOR_X, y=SENSOR_Y, z=45, r=0)
    wait_for(0.1)
    # Lecture de la couleur (tolérante)
    color = read_color_tolerant()
    wait_for(0.5)
    if color == "RED":
        row = ROW_RED
    elif color == "GREEN":
        row = ROW_GREEN
    elif color == "BLUE":
        row = ROW_BLUE
    else:
        # si lecture incorrecte revenir en position initiale
        print("Erreur: lecture couleur invalide ->", color)
        magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
        wait_for(0.3)

    # Colonne libre
    col = next_col[row]
    next_col[row] += 1

    # Calcul position de dépôt (ABPlace_X/Y servent de référence)
    x_place = ABPlace_X - col * STEP   # vers la droite du robot (X-)
    y_place = ABPlace_Y - row * STEP   # vers le haut (Y-)
    # désactiver  le capteur de couleur
    magician.set_color_sensor(port=2, enable=False, version=1)
    wait_for(0.1)
     # Aller  au point intermédiiare pour éviter la mise en sécurité axes
    magician.ptp(mode=2, x=162, y=-182, z=26, r=0)
    # Aller au-dessus de la zone de dépôt, puis descendre et lâcher
    jump_to(x_place, y_place, ABPlace_Z)
    magician.ptp(mode=2, x=x_place, y=y_place, z=ATPlace_Z, r=0)
    wait_for(0.3)
    magician.set_endeffector_suctioncup(enable=True, on=False)
    wait_for(0.4)
    magician.ptp(mode=2, x=x_place, y=y_place, z=ABPlace_Z, r=0)
    wait_for(0.3)

    # Aller  au point intermédiiare pour éviter la mise en sécurité axes
    magician.ptp(mode=2, x=162, y=-182, z=26, r=0)
    # Retour à HOME entre cycles (optionnel)
    magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
    wait_for(0.3)

# -----------------------------
# Programme principal
# -----------------------------
# Position de départ
magician.ptp(mode=1, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
wait_for(0.2)

# Parcours de la grille 3x3 de départ (ordre original adapté)
for i in range(3):      # lignes
    for j in range(3):  # colonnes
        x_cube = ABPick_X - j * STEP
        y_cube = ABPick_Y + i * STEP
        pick_and_place_with_color(x_cube, y_cube)
