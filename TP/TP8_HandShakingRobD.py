from DobotEDU import *

# --------------------------------------
# --- TP8_HandShakingRobD---
# --------------------------------------

signal_file = "H:\Dobot\signal.txt"

HOME = (250, 0, 50, 0)
LEFT = (250, -50, 50, 0)  # tourne légèrement vers la gauche

def wait_for(magician, seconds):
    magician.wait(second=seconds)

def go_home():
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=HOME[3])
    wait_for(magician, 0.5)

def turn_left():
    magician.ptp(mode=2, x=LEFT[0], y=LEFT[1], z=LEFT[2], r=LEFT[3])
    wait_for(magician, 0.5)

def write_signal(value):
    with open(signal_file, "w") as f:
        f.write(str(value))

# === Étape 1 : HOME ===
go_home()
print("RobotD en position HOME")

# === Étape 2 : tourner vers RobotG, envoyer signal = 1 ===
turn_left()
write_signal(1)
print("RobotD a envoyé le signal = 1")

# Retour HOME
go_home()
print("RobotD de retour HOME")