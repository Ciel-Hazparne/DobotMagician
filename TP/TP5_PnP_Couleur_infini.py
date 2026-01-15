# version: Python3
from DobotEDU import *
import random

# ============================
# PARAMÈTRES GÉNÉRAUX
# ============================
HOME_X, HOME_Y, HOME_Z = (259, 0, 50)

ABPick_X, ABPick_Y, ABPick_Z = (161.5, 178.27, 0)
ATPick_X, ATPick_Y, ATPick_Z = (161.5, 178.27, -44.74)

ABPlace_X, ABPlace_Y, ABPlace_Z = (33.75, -178.47, 0)
ATPlace_X, ATPlace_Y, ATPlace_Z = (33.75, -178.47, -44)

SENSOR_X, SENSOR_Y, SENSOR_ABOVE_Z = (191.28, -2.69, 50)

STEP = 35

ROW_BLUE  = 0
ROW_GREEN = 1
ROW_RED   = 2

NB_CYCLES = 100

# ============================
# OUTILS
# ============================
def wait_for(s):
    magician.wait(second=s)

def jump_to(x, y, z, r=0, h=30):
    p = magician.get_pose()
    px, py, pz = p["x"], p["y"], p["z"]
    pr = p.get("r", 0)

    magician.ptp(2, px, py, pz + h, pr)
    wait_for(0.2)
    magician.ptp(2, x, y, z + h, r)
    wait_for(0.2)
    magician.ptp(2, x, y, z, r)
    wait_for(0.2)

def read_color_tolerant():
    magician.set_color_sensor(2, True, 1)
    wait_for(0.1)
    magician.get_color_sensor()

    readings = []
    for _ in range(3):
        c = magician.get_color_sensor()
        if isinstance(c, dict):
            readings.append(c)
        wait_for(0.1)

    magician.set_color_sensor(2, False, 1)

    r = sum(x.get("red", 0) for x in readings)
    g = sum(x.get("green", 0) for x in readings)
    b = sum(x.get("blue", 0) for x in readings)

    if r >= 2: return "RED"
    if g >= 2: return "GREEN"
    if b >= 2: return "BLUE"
    return None

def pick(x, y):
    magician.ptp(2, x, y, ABPick_Z, 0)
    magician.ptp(2, x, y, ATPick_Z, 0)
    magician.set_endeffector_suctioncup(True, True)
    wait_for(0.4)
    magician.ptp(2, x, y, ABPick_Z, 0)

def place(x, y):
    jump_to(x, y, ABPlace_Z)
    magician.ptp(2, x, y, ATPlace_Z, 0)
    magician.set_endeffector_suctioncup(True, False)
    wait_for(0.3)
    magician.ptp(2, x, y, ABPlace_Z, 0)

# ============================
# GÉNÉRATION DES GRILLES
# ============================
def generate_start_grid():
    return [(ABPick_X - j*STEP, ABPick_Y + i*STEP)
            for i in range(3) for j in range(3)]

def generate_end_grid():
    return [(ABPlace_X - j*STEP, ABPlace_Y - i*STEP)
            for i in range(3) for j in range(3)]

start_grid = generate_start_grid()
end_grid   = generate_end_grid()

# ============================
# PROGRAMME PRINCIPAL
# ============================
magician.ptp(1, HOME_X, HOME_Y, HOME_Z, 0)
wait_for(0.5)

for cycle in range(NB_CYCLES):

    # --- TRI PAR COULEUR ---
    next_col = {ROW_RED: 0, ROW_GREEN: 0, ROW_BLUE: 0}
    cubes_to_sort = start_grid[:]   # photographie initiale

    for (x, y) in cubes_to_sort:
        pick(x, y)

        magician.ptp(2, HOME_X, HOME_Y, HOME_Z, 0)
        jump_to(SENSOR_X, SENSOR_Y, SENSOR_ABOVE_Z)
        magician.ptp(2, SENSOR_X, SENSOR_Y, 45, 0)

        color = read_color_tolerant()

        if color == "RED":
            row = ROW_RED
        elif color == "GREEN":
            row = ROW_GREEN
        elif color == "BLUE":
            row = ROW_BLUE
        else:
            magician.set_endeffector_suctioncup(True, False)
            continue

        col = next_col[row]
        if col >= 3:
            magician.set_endeffector_suctioncup(True, False)
            magician.ptp(2, HOME_X, HOME_Y, HOME_Z, 0)
            continue
        next_col[row] += 1
        idx = row * 3 + col

        place(*end_grid[idx])
        magician.ptp(2, HOME_X, HOME_Y, HOME_Z, 0)

    # --- REMISE ALÉATOIRE ---
    shuffled_start = start_grid[:]
    random.shuffle(shuffled_start)

    for src, dst in zip(end_grid, shuffled_start):
        pick(*src)
        place(*dst)
        magician.ptp(2, HOME_X, HOME_Y, HOME_Z, 0)