# version: Python3
from DobotEDU import *

# ============================
# === TP3_PnP-1FDC-2Clics ====
# ============================

# Coordonnées à adapter
HOME = (170, 33, 0)                          # Position de sécurité
ABPick = (274, 33, -35)                      # Au-dessus de l’objet
ATPick = (274, 33, -55)                      # À l’objet
ABPlace = (206, 33, -35)                     # Au-dessus de la zone de dépôt
ATPlace = (206, 33, -55)                     # À la zone de dépôt

# ---------------------------------
# Fonction utilitaire
# ---------------------------------
# Fonction JumpTo
def jump_to(x, y, z, r=0, jump_height=50):
    pose = magician.get_pose()
    x_cur, y_cur, z_cur, r_cur = pose["x"], pose["y"], pose["z"], pose["r"]

    # Monter depuis la position actuelle
    magician.ptp(mode=2, x=x_cur, y=y_cur, z=z_cur + jump_height, r=r_cur)
    magician.wait(second=0.5)

    # Aller horizontalement au-dessus de la cible
    magician.ptp(mode=2, x=x, y=y, z=z + jump_height, r=r)
    magician.wait(second=0.5)

    # Descendre à la position finale
    magician.ptp(mode=2, x=x, y=y, z=z, r=r)
    magician.wait(second=0.5)

# Fonction attente double-clic bouton DI_05
def wait_for_double_click():
    count = 0
    while count < 2:
        if magician.get_di(io="DI_05") == 1:
            count += 1
            while magician.get_di(io="DI_05") == 1:
                pass  # Attendre relâchement

# --- Programme principal ---
# Position initiale
jump_to(*HOME)

# Étape 1 : attendre double clic bouton -> Pick
wait_for_double_click()
jump_to(*ABPick)
jump_to(*ATPick)
magician.set_endeffector_suctioncup(enable=True, on=True)
jump_to(*ABPick)
jump_to(*HOME)

# Étape 2 : attendre double clic bouton -> Place
wait_for_double_click()
jump_to(*ABPlace)
jump_to(*ATPlace)
magician.set_endeffector_suctioncup(enable=True, on=False)
jump_to(*ABPlace)
jump_to(*HOME)