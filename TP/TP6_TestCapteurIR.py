# version: Python3
from DobotEDU import *

# =========================
# === TP6_TestCapteurIR ===
# =========================
magician.wait(second=1)
magician.set_infrared_sensor(port=4, enable=True, version=1)
for i in range(5):
    IR_raw = magician.get_infrared_sensor(port=4)
    print("Lecture brute :", IR_raw)
    magician.wait(second=1)
