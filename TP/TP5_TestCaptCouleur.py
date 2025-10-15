# version: Python3
from DobotEDU import *

# =========================
# === TP5_TestCaptCouleur ===
# =========================

# -----------------------------
# Fonction détection couleur
# -----------------------------
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



# -----------------------------
# Test : détection et tri rouge / vert
# -----------------------------
for i in range(2):
    # Placer la ventouse au-dessus du capteur, activer la pompe et aspirer un cube vert ou rouge
    magician.ptp(mode=2, x=191.28, y=-2.69, z=80, r=0)
    magician.set_endeffector_suctioncup(enable=True, on=True)
    magician.wait(second=1)

    # Activer le capteur de couleur
    magician.set_color_sensor(port=2, enable=True, version=1)
    magician.wait(second=0.1)

    # Descendre à la bonne distance (≈10 mm)
    magician.ptp(mode=2, x=191.28, y=-2.69, z=48, r=0)
    magician.wait(second=0.1)

    # Lecture de la couleur (tolérante)
    color = read_color_tolerant()
    magician.wait(second=0.5)

    if color == "RED":
        print("Cube detecte : ROUGE")
        magician.ptp(mode=2, x=280, y=60, z=50, r=0)
        magician.set_endeffector_suctioncup(enable=True, on=False)

    elif color == "GREEN":
        print("Cube detecte : VERT")
        magician.ptp(mode=2, x=280, y=-90, z=50, r=0)
        magician.set_endeffector_suctioncup(enable=True, on=False)

    else:
        # Si lecture incorrecte, revenir en position initiale
        print("Erreur : lecture couleur invalide ->", color)
        magician.ptp(mode=2, x=280, y=-13, z=50, r=0)
        magician.wait(second=0.3)
