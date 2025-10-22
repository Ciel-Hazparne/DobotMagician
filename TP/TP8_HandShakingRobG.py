from DobotEDU import *

# --------------------------------------
# --- TP8_HandShakingRobG ---
# --------------------------------------

#magicianD = Dobot(port="COM5")  # adapte le port selon ton installation
signal_file = "C:/Dobot/signal.txt"

HOME = (250, 0, -8, 0)
RIGHT = (250, -50, -8, -20)  # tourne légèrement vers la droite

def wait_for(magician, seconds):
    magician.wait(second=seconds)

def go_home():
    magician.ptp(mode=2, x=HOME[0], y=HOME[1], z=HOME[2], r=HOME[3])
    wait_for(magician, 0.5)

def turn_right():
    magician.ptp(mode=2, x=RIGHT[0], y=RIGHT[1], z=RIGHT[2], r=RIGHT[3])
    wait_for(magician, 0.5)

def read_signal():
    with open(signal_file, "r") as f:
        return f.read().strip()

def write_signal(value):
    with open(signal_file, "w") as f:
        f.write(str(value))

# === Étape 1 : HOME ===
go_home()
print("RobotG en position HOME")

# === Étape 2 : attendre signal 1 de RobotD ===
print("RobotG en attente du signal...")
signal = "0"
while signal != "1":
    signal = read_signal()
    wait_for(magician, 0.2)
print("RobotG a reçu le signal = 1")

# === Étape 3 : tourne vers la droite, répond avec signal = 0 ===
turn_right()
write_signal(0)
print("RobotG a renvoyé signal = 0")

# Retour HOME
go_home()
print("RobotG de retour HOME")