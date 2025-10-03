# version: Python3
from DobotEDU import *

# ============================
# ===== TP5_PnpSelonCouleur ===
# ============================

# Positions de base
HOME_X, HOME_Y, HOME_Z = (270, -4, 50)    # position de repos au dessus du tapis
ABPick_X, ABPick_Y, ABPick_Z = (128.87, 160.67, 0)
ATPick_X, ATPick_Y, ATPick_Z = (128.87, 160.67, -42.18)
ABPlace_X, ABPlace_Y, ABPlace_Z = (65.26, -218.96, 0)
ATPlace_X, ATPlace_Y, ATPlace_Z = (65.26, -218.96, -42.18)

# Capteur de couleur
SENSOR_X, SENSOR_Y, SENSOR_ABOVE_Z = (190.43, -28.32, 50)  # hauteur idéale 8-12 mm

# Grille 3x3
STEP = 35
CUBE_SIZE = 25
ROW_RED = 0
ROW_GREEN = 1
ROW_BLUE = 2

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

def jump_to(x, y, z, r=0, jump_height=50):
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
    """Lit la couleur et normalise la valeur ('RED','GREEN','BLUE') si possible."""
    raw = magician.get_color_sensor()
    s = str(raw).upper()
    if "RED" in s:
        return "RED"
    if "GREEN" in s:
        return "GREEN"
    if "BLUE" in s:
        return "BLUE"
    # fallback : renvoyer None si indéterminé
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
    magician.ptp(mode=2, x=SENSOR_X, y=SENSOR_Y, z=34, r=0)
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
    next_col[row] = next_col[row] + 1

    # Calcul position de dépôt (ABPlace_X/Y servent de référence)
    x_place = ABPlace_X - col * STEP
    y_place = ABPlace_Y - row * STEP
    # désactiver  le capteur de couleur
    magician.set_color_sensor(port=2, enable=False, version=1)
    wait_for(0.1)
    # Aller  à HOME pour éviter la mise en sécurité x)
    magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
    wait_for(0.3)
    # Aller au-dessus de la zone de dépôt, puis descendre et lâcher
    jump_to(x_place, y_place, ABPlace_Z)
    magician.ptp(mode=2, x=x_place, y=y_place, z=ATPlace_Z, r=0)
    wait_for(0.3)
    magician.set_endeffector_suctioncup(enable=True, on=False)
    wait_for(0.4)
    magician.ptp(mode=2, x=x_place, y=y_place, z=ABPlace_Z, r=0)
    wait_for(0.3)

    # Retour à HOME entre cycles (optionnel)
    magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
    wait_for(0.3)

# -----------------------------
# Programme principal
# -----------------------------
# Position de départ
magician.ptp(mode=2, x=HOME_X, y=HOME_Y, z=HOME_Z, r=0)
wait_for(0.2)

# Parcours de la grille 3x3 de départ (ordre original adapté)
for i in range(3):      # lignes
    for j in range(3):  # colonnes
        x_cube = ABPick_X - j * STEP
        y_cube = ABPick_Y + i * STEP
        pick_and_place_with_color(x_cube, y_cube)
