from ultralytics import YOLO
import cv2

model = YOLO(r"C:\Users\eduar\Documents\Universidad Anahuac Puebla\7mo Semestre\Sistemas de Visión Industrial\Códigos\Proyecto Final\runs\detect\train12\weights\best.pt")   # Cambia la ruta si es necesario

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

print("Cámara detectada. Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer el frame.")
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("Detección con best.pt", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()