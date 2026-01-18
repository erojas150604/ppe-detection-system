from ultralytics import YOLO
import torch

def main():
    print("CUDA:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))

    model = YOLO("yolo11m.pt")

    model.train(
        data=r"C:\Users\eduar\Documents\Universidad Anahuac Puebla\7mo Semestre\Sistemas de Visión Industrial\Códigos\Proyecto Final\prueba6\data.yaml",
        epochs=200,
        imgsz=640,
        batch=8,
        workers=0,
        device=0,
        lr0=0.0005,
        cls=2.0,
        pretrained=True,
        patience=50
    )

if __name__ == "__main__":
    main()
