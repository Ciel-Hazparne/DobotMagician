# version: Python3
from DobotEDU import *

# ============================
# === TP5_PnpSelonCouleur ====
# ============================

# Positions de base
HOME_X, HOME_Y, HOME_Z = 200, 0, 50
ABPick_X, ABPick_Y, ABPick_Z = 150, 100, 50
ATPick_X, ATPick_Y, ATPick_Z = 150, 100, 10
ABPlace_X, ABPlace_Y, ABPlace_Z = 250, -100, 50
ATPlace_X, ATPlace_Y, ATPlace_Z = 250, -100, 10

# Capteur de couleur
SENSOR_X, SENSOR_Y, SENSOR_ABOVE_Z = 180, 80, 10  # hauteur idéale 8-12 mm

# Grille 3x3
STEP = 35
CUBE_SIZE = 25
ROW_RED = 0
ROW_GREEN = 1
ROW_BLUE = 2
COLS = [0, 1, 2]

# Suivi de la prochaine colonne libre pour chaque ligne
next_col = {ROW_RED: 0, ROW_GREEN: 0, ROW_BLUE: 0}

# -----------------------------
# Fonctions utilitaires
# -----------------------------

def jump_to(x, y, z, jump_height=50):
    """
    Déplace le robot en sautant pour éviter collisions.
    jump_height : hauteur de sécurité
    """
    pose = magician.get_pose()
    magician.set_ptpcmd(1, pose[0], pose[1], pose[2] + jump_height, 0)
    magician.set_ptpcmd(1, x, y, z + jump_height, 0)
    magician.set_ptpcmd(1, x, y, z, 0)

def pick_and_place_with_color(x_pick, y_pick):
    # Aller au cube
    magician.set_ptpcmd(1, x_pick, y_pick, ABPick_Z, 0)
    magician.set_ptpcmd(1, x_pick, y_pick, ATPick_Z, 0)
    magician.set_endeffector_suctioncup(True)

    # Soulever le cube au-dessus ABPick
    magician.set_ptpcmd(1, x_pick, y_pick, ABPick_Z, 0)

    # Déplacer le cube au-dessus du capteur pour lecture
    jump_to(SENSOR_X, SENSOR_Y, SENSOR_ABOVE_Z)

    # Lire couleur
    color = magician.get_color_sensor()  # renvoie "RED", "GREEN" ou "BLUE"

    # Déterminer ligne de dépôt
    if color == "RED":
        row = ROW_RED
    elif color == "GREEN":
        row = ROW_GREEN
    elif color == "BLUE":
        row = ROW_BLUE
    else:
        row = ROW_RED  # défaut si problème de lecture

    # Calculer la colonne libre
    col = next_col[row]
    next_col[row] += 1

    # Calcul de la position de dépôt
    x_place = ABPlace_X + col * STEP
    y_place = ABPlace_Y + row * STEP

    # Déplacer vers la zone de dépôt
    jump_to(x_place, y_place, ABPlace_Z)
    magician.set_ptpcmd(1, x_place, y_place, ATPlace_Z, 0)
    magician.set_endeffector_suctioncup(False)
    magician.set_ptpcmd(1, x_place, y_place, ABPlace_Z, 0)

    # Retour à HOME
    magician.set_ptpcmd(1, HOME_X, HOME_Y, HOME_Z, 0)


# -----------------------------
# Programme principal
# -----------------------------

# Parcours de la grille 3x3 de départ
for i in range(3):      # lignes
    for j in range(3):  # colonnes
        x_cube = ABPick_X + j * STEP
        y_cube = ABPick_Y + i * STEP
        pick_and_place_with_color(x_cube, y_cube)