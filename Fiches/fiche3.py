from DobotEDU import *

# ==========================
# === fiche3 : fcnctions ===
# ==========================

def monter(z):
    magician.ptp(1, 200, 0, z, 0)
    magician.wait(1)

def aspirer(state):
    # state = True → activer la ventouse
    # state = False → désactiver la ventouse
    # Forme courte : magician.set_endeffector_suctioncup(True, False)
    # Forme complète : magician.set_endeffector_suctioncup(enable=True, on=False)
    magician.set_endeffector_suctioncup(True, state)

monter(30)
aspirer(True)   # ventouse ON
monter(60)
aspirer(False)  # ventouse OFF