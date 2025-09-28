# version: Python3
from DobotEDU import *

# ============================
# = TP9_TP9_HotPotatoRobot2 ==
# ============================
signal = 0  # Variable partagée

while True:
    # Attente du tour de Robot 2
    while signal != 1:
        magician.delay(100)

    magician.home()

    # Pick
    magician.move_to(150, 50, -50, 0)
    magician.set_end_effector_suctioncup(enable=True, on=True)
    magician.delay(1000)

    # Place
    magician.move_to(200, 50, -50, 0)
    magician.set_end_effector_suctioncup(enable=True, on=False)
    magician.delay(1000)

    magician.home()

    # Donne la main à Robot 1
    signal = 0
    print("Robot 2 a terminé, signal =", signal)