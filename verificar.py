import os

DATASET_PATH = r"C:\Users\eduar\Documents\Universidad Anahuac Puebla\7mo Semestre\Sistemas de Visión Industrial\Códigos\Proyecto Final\prueba6"
PLAYERA = 6
encontradas = []

for split in ["train", "valid", "test"]:
    labels = os.path.join(DATASET_PATH, split, "labels")
    
    for fname in os.listdir(labels):
        if not fname.endswith(".txt"):
            continue
        with open(os.path.join(labels, fname), "r") as f:
            for line in f:
                cls_id = int(line.split()[0])
                if cls_id == PLAYERA:
                    encontradas.append(os.path.join(split, "labels", fname))

if encontradas:
    print("❌ Todavía existen etiquetas de playera:")
    for path in encontradas:
        print(path)
else:
    print("✔ No existe ni una sola etiqueta de playera (clase 6). Todo limpio.")
