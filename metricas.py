from ultralytics import YOLO 

def main():
    modelo = YOLO(r"runs\detect\train5\weights\best.pt")

    metricas = modelo.val()
    print(metricas)
    

if __name__ == "__main__":
    main()



