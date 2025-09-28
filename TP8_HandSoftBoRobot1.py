# version: Python3
from DobotEDU import *

# ============================
# === TP8_HandSoftBoRobot1 ===
# ============================

# Variable partagée
signal = 0

# Robot 1 - Pick & Place puis envoi du signal
magician.home()

# Pick
magician.move_to(200, 0, -50, 0)
magician.set_end_effector_suctioncup(enable=True, on=True)
magician.delay(1000)

# Place
magician.move_to(250, 0, -50, 0)
magician.set_end_effector_suctioncup(enable=True, on=False)
magician.delay(1000)

# Retour Home
magician.home()

# Envoi du signal à Robot 2
signal = 1
print("Robot 1 a envoyé signal =", signal)