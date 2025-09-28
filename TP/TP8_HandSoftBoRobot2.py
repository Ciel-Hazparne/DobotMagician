# version: Python3
from DobotEDU import *

# ============================
# === TP8_HandSoftBoRobot2 ===
# ============================

# Variable partagée
signal = 0

# Robot 2 - Attente signal puis Pick & Place
magician.home()

# Attente du signal de Robot 1
while signal != 1:
    magician.delay(100)

# Pick
magician.move_to(150, 50, -50, 0)
magician.set_end_effector_suctioncup(enable=True, on=True)
magician.delay(1000)

# Place
magician.move_to(200, 50, -50, 0)
magician.set_end_effector_suctioncup(enable=True, on=False)
magician.delay(1000)

# Retour Home
magician.home()

# Remise à zéro du signal
signal = 0
print("Robot 2 a terminé et remis signal =", signal)