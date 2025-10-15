from DobotEDU import *
# =====================
# === TP5_RetourCaptCouleu ===
# =====================

# Placer un cube à 10 mm au dessus du capteur et lire la couleur detectée (la 1ère mesure sera fausse)

magician.set_color_sensor(port=2, enable=True, version=1)

for i in range(5):
    color_raw = magician.get_color_sensor()
    print("Lecture brute :", color_raw)
    magician.wait(second=0.5)

magician.set_color_sensor(port=2, enable=False, version=1)