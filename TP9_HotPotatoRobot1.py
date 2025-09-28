# version: Python3
from DobotEDU import *

# ============================
# = TP9_TP9_HotPotatoRobot1 ==
# ============================

signal = 0  # Variable partagée, Robot 1 commence

while True:
    # Attente du tour de Robot 1
    while signal != 0:
        magician.delay(100)

    magician.home()

    # Pick
    magician.move_to(200, 0, -50, 0)
    magician.set_end_effector_suctioncup(enable=True, on=True)
    magician.delay(1000)

    # Place
    magician.move_to(250, 0, -50, 0)
    magician.set_end_effector_suctioncup(enable=True, on=False)
    magician.delay(1000)

    magician.home()

    # Donne la main à Robot 2
    signal = 1
    print("Robot 1 a terminé, signal =", signal)