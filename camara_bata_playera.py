from ultralytics import YOLO

model = YOLO(r"C:\Users\eduar\Documents\Universidad Anahuac Puebla\7mo Semestre\Sistemas de Visión Industrial\Códigos\Proyecto Final\runs\detect\train11\weights\best.pt")  # tu modelo entrenado solo con bata/playera

# Imagen donde SABES que es playera, bien clara
img_path = r"C:\Users\eduar\Documents\Universidad Anahuac Puebla\7mo Semestre\Sistemas de Visión Industrial\Códigos\Proyecto Final\Playeras\cloth_dataset\tshirt\113.jpg"

results = model(img_path, conf=0.1)  # conf baja para ver todo

for r in results:
    print("------- FRAME -------")
    for box in r.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        print(f"cls: {cls_id}, conf: {conf}")
