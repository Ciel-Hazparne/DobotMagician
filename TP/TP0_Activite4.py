# version: Python3
from DobotEDU import *

# ======================
# === TP0_Activite4 =====
# ======================

# --- Constantes / positions ---
HOME = (218.5, 78, 0)              # position HOME au dessus du carré bleu

# Hauteur d’approche Z
COMMON_Z = -35

# Coordonnées des positions occupées par les cubes (x = cube présent)
# Grille symbolique (indices selon la grille)
positions = {
    0: (183, 34.5, COMMON_Z),
    1: (183, -0.5, COMMON_Z),
    2: (183, -35.5, COMMON_Z),
    3: (218, 34.5, COMMON_Z),
    4: (218,  -0.5, COMMON_Z),
    5: (218, -35.5, COMMON_Z),
    6: (253, 34.5, COMMON_Z),
    7: (253, -0.5, COMMON_Z),
    8: (253, -35.5, COMMON_Z)
}

# Parcours L : suivre la ligne
parcours_L = [0, 1, 2]

# --- Fonction utilitaire pour déplacement ---
def go_to(pos, mode=0, wait_sec=0.5):
    """Déplace le bras vers la position pos avec le mode choisi et temporisation"""
    magician.ptp(mode=mode, x=pos[0], y=pos[1], z=pos[2], r=0)
    magician.wait(second=wait_sec)

# --- Programme principal ---
for mode in [0, 1, 2]:  # Séquence 3 fois pour mode=0,1,2
    print(f"=== Début séquence avec mode={mode} ===")

    # 1. Aller à HOME
    go_to(HOME, mode=0)

    # 2  Suivre la ligne
    for idx in parcours_L:
        go_to(positions[idx], mode=mode)

    # 4. Retour à HOME pour terminer le cycle
    go_to(HOME, mode=0)

    print(f"=== Fin séquence avec mode={mode} ===")
