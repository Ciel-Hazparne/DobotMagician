from DobotEDU import *

# ==================
# === TP6_TestCapteurIR ===
# ==================
HOME = (186, 0, 52, 0)
PLACE = (250, 0, 0, 0)

# Activer capteur IR sur GP2
magician.set_infrared_sensor(port=2, enable=True, version=1)

# Lecture capteur
detect = magician.get_infrared_sensor(port=2)
detect1 = magician.get_di(io="DI_02")  # pour info uniquement

print("Lecture GP2 :", detect)
print("Lecture I/O2 :", detect1)

def go_place():
    magician.ptp(mode=2, x=PLACE[0], y=PLACE[1], z=PLACE[2], r=PLACE[3])
    magician.wait(second=0.5)

def go_home():
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=HOME[3])
    magician.wait(second=0.5)

# Correction : utiliser la clé 'status'
if detect['status'] == 1:
    go_place()
    print("Robot en position PLACE")
    magician.wait(second=0.5)
    go_home()
    print("Robot en position HOME")
else:
    print("Aucune detection sur GP2")
