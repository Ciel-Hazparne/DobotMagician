import json
from pathlib import Path

# === CONFIGURATION ===
# Chemin vers le dossier contenant les JSON
dossier_json = Path(r"C:\Python\Json par exemple")

# === PARCOURS DU DOSSIER ===
for json_file in dossier_json.glob("*.json"):
    try:
        # Lecture du JSON
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Vérifie si c'est bien un export DobotLab
        if "script" in data and "code" in data["script"] and "tabs" in data["script"]:
            codes = data["script"]["code"]
            tabs = data["script"]["tabs"]

            # Parcours tous les "onglets" / fichiers
            for tab_name, code_text in zip(tabs, codes):
                # Crée le fichier .py dans le même dossier que le JSON
                py_file = dossier_json / tab_name
                with open(py_file, "w", encoding="utf-8") as f:
                    f.write(code_text)
                print(f"Fichier créé : {py_file}")
        else:
            print(f"Ignoré (format JSON non reconnu) : {json_file}")
    except Exception as e:
        print(f"Erreur avec {json_file} : {e}")

print("Conversion terminée.")
