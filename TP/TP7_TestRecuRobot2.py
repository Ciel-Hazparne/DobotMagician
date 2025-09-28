# version: Python3
from DobotEDU import *

# ============================
# ==== TP7_TestRecuRobot2 ====
# ============================

# -------------------------------
# Fonctions et repères
# -------------------------------

# Fonction JumpTo : combine monter, déplacement horizontal, descendre
def jump_to(x, y, z, jump_height=50):
    """
    Déplacement par 'saut' : monte, se déplace horizontalement, descend.
    jump_height = hauteur du saut au-dessus des obstacles.
    """
    # Monter depuis la position actuelle
    magician.set_ptpcmd(1, magician.get_pose()[0], magician.get_pose()[1], magician.get_pose()[2] + jump_height, 0)
    # Aller horizontalement à la position cible, en restant en hauteur
    magician.set_ptpcmd(1, x, y, z + jump_height, 0)
    # Descendre à la hauteur finale
    magician.set_ptpcmd(1, x, y, z, 0)

# Coordonnées repères (exemple, à adapter selon le poste)
HOME     = (200,   0, 50, 0)
ABPick   = (150, 100, 50, 0)
ATPick   = (150, 100, 10, 0)
ABPlace  = (250, -100, 50, 0)
ATPlace  = (250, -100, 10, 0)

# -------------------------------
# Routine Pick & Place
# -------------------------------

def pick_and_place():
    """
    Exécute une routine Pick & Place complète.
    """
    # Étape 1 : position de départ
    magician.set_ptpcmd(1, *HOME)

    # Étape 2-3 : aller au-dessus de l'objet puis à l'objet
    magician.set_ptpcmd(1, *ABPick)
    magician.set_ptpcmd(1, *ATPick)

    # Étape 4 : activer l'aspiration pour prendre l'objet
    magician.set_endeffector_suctioncup(True)

    # Étape 5-7 : déplacement vers la zone de dépôt avec Jump
    jump_to(*ABPlace)
    magician.set_ptpcmd(1, *ATPlace)

    # Étape 8 : relâcher l'objet
    magician.set_endeffector_suctioncup(False)

    # Étape 9-10 : remonter et revenir au départ
    magician.set_ptpcmd(1, *ABPlace)
    magician.set_ptpcmd(1, *HOME)

# -------------------------------
# Boucle finie : répéter N fois
# -------------------------------

N = 5  # nombre de répétitions
for i in range(N):
    pick_and_place()

# -------------------------------
# Boucle infinie : répéter indéfiniment
# -------------------------------

# Décommenter pour tester la boucle infinie
# while True:
#     pick_and_place()