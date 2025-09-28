from DobotEDU import *

# ===============================
# === fiche6 : double boucle  ===
# ===============================

for row in range(3):
    for col in range(3):
        x = 200 - row * 20
        y = 100 + col * 20
        magician.ptp(1, x, y, 0, 0)
        magician.set_endeffector_suctioncup(True, True)
        magician.wait(0.2)
        magician.set_endeffector_suctioncup(True, False)

