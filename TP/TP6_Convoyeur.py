# version: Python3
from DobotEDU import *

# =========================
# ===== TP6_Convoyeur =====
# =========================

# Ports et vitesse convoyeur
IR_port = 4      # GP4
Color_port = 2   # GP2
Conveyor_speed = 80

# Positions zones (x, y, z, r)
HOME = (250, 0, -8, 0)
ZONE_A = (300, -50, -8, 0)
ZONE_B = (300, 50, -8, 90)
REBUT = (200, 0, -8, -90)
PICK_POS = (200, 0, -8, 0)

def wait_for(seconds):
    magician.wait(second=seconds)

def safe_home():
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=HOME[3])
    wait_for(0.5)

def pick_cube(pos):
    magician.ptp(mode=2, x=pos[0], y=pos[1], z=pos[2], r=pos[3])
    magician.set_endeffector_suctioncup(enable=True, on=True)
    wait_for(0.3)

def place_cube(pos):
    magician.ptp(mode=2, x=pos[0], y=pos[1], z=pos[2], r=pos[3])
    magician.set_endeffector_suctioncup(enable=True, on=False)
    wait_for(0.3)

def conveyor_control(state, speed=Conveyor_speed):
    magician.set_conveyor_speed(speed)
    magician.set_conveyor_state(state)

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

    if red_count >= 2:
        return "RED"
    elif green_count >= 2:
        return "GREEN"
    return None

# Boucle de production
try:
    conveyor_control(state=1)
    while True:
        ir_status = magician.get_infrared_sensor(port=IR_port)['status']
        if ir_status == 1:
            conveyor_control(state=0)  # stop conveyor
            magician.set_color_sensor(port=2, enable=True, version=1)
            # Lecture de la couleur (tolérante)
            color = read_color_tolerant()
            wait_for(0.5)
            if color == "RED":
                place_cube(ZONE_A)
                print("Cube rouge vers Zone A")
            elif color == "GREEN":
                place_cube(ZONE_B)
                print("Cube vert vers Zone B")
            else:
                place_cube(REBUT)
                print("Cube indéterminé vers REBUT")
            safe_home()
            conveyor_control(state=1)
        wait_for(0.1)
except KeyboardInterrupt:
    conveyor_control(state=0)
    safe_home()
    print("Production stoppée")