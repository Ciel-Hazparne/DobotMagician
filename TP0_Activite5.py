# version: Python3
from DobotEDU import *

# ======================
# === TP0_ActiviteU =====
# ======================

# --- Constantes / positions ---
ABP0 = (170, 33, 0)   # Position d’attente (départ)
HOME = (170, 33, 0)   # Position HOME

# Hauteur d’approche Z
COMMON_Z = -35

# Coordonnées des positions occupées par les cubes (x = cube présent)
# Grille symbolique (indices selon la grille)
positions = {
    0: (205, 0, COMMON_Z),
    1: (240, 0, COMMON_Z),
    2: (275, 0, COMMON_Z),
    3: (205, 35, COMMON_Z),
    4: (240, 35, COMMON_Z),
    5: (275, 35, COMMON_Z),
    6: (205, 70, COMMON_Z),
    7: (240, 70, COMMON_Z),
    8: (275, 70, COMMON_Z)
}

# Parcours en U : suivre l'intérieur des cubes
parcours_U = [0, 1, 5, 7, 6]

# --- Fonction utilitaire pour déplacement ---
def go_to(pos, mode=0, wait_sec=0.5):
    """Déplace le bras vers la position pos avec le mode choisi et temporisation"""
    magician.ptp(mode=mode, x=pos[0], y=pos[1], z=pos[2], r=0)
    magician.wait(second=wait_sec)

# --- Programme principal ---
for mode in [0, 1, 2]:  # Séquence 3 fois pour mode=0,1,2
    print(f"=== Début séquence avec mode={mode} ===")

    # 1. Aller à ABP0
    go_to(ABP0, mode=0)

    # 2. Aller à HOME
    go_to(HOME, mode=0)

    # 3. Suivre le parcours en U
    for idx in parcours_U:
        go_to(positions[idx], mode=mode)

    # 4. Retour à HOME pour terminer le cycle
    go_to(HOME, mode=0)

    print(f"=== Fin séquence avec mode={mode} ===")
