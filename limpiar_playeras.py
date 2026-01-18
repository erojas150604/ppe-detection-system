import os

# Cambia esta ruta a donde tengas tu dataset descargado
DATASET_PATH = r"C:\Users\eduar\Documents\Universidad Anahuac Puebla\7mo Semestre\Sistemas de Visión Industrial\Códigos\Proyecto Final\prueba6\data.yaml"

CLASS_TO_REMOVE = 6  # playera

def limpiar_directorio(label_dir):
    for fname in os.listdir(label_dir):
        if not fname.endswith(".txt"):
            continue
        fpath = os.path.join(label_dir, fname)
        with open(fpath, "r") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            cls_id = int(line.split()[0])
            if cls_id != CLASS_TO_REMOVE:
                new_lines.append(line)

        # Si no quedó nada → BORRAMOS el archivo .txt entero (imagen negativa)
        if len(new_lines) == 0:
            os.remove(fpath)
        else:
            with open(fpath, "w") as f:
                f.writelines(new_lines)

for split in ["train", "valid", "test"]:
    label_dir = os.path.join(DATASET_PATH, split, "labels")
    limpiar_directorio(label_dir)

print("✔ Listo: todas las etiquetas de playera han sido eliminadas.")
