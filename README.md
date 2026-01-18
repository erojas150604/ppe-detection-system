# PPE Detection System using YOLOv8

Sistema de visión artificial desarrollado para detectar automáticamente el uso de Equipo de Protección Personal (EPP) en laboratorios de ingeniería, utilizando modelos de detección entrenados con YOLOv8.

Este proyecto implementa un pipeline completo de Machine Learning orientado a monitoreo de seguridad en entornos técnicos e industriales.

---

## Objetivo
Detectar en tiempo real si una persona porta correctamente equipo de protección (bata y playera como clases principales) mediante visión computacional y modelos entrenados.

---

## Enfoque del sistema
El flujo del proyecto fue:

1. Recolección y etiquetado del dataset (Roboflow)  
2. Organización de imágenes en carpetas `train`, `valid` y `test`  
3. Definición de clases mediante `data.yaml`  
4. Entrenamiento del modelo YOLOv8 con Ultralytics  
5. Evaluación de métricas (precision, recall, F1, matriz de confusión)  
6. Pruebas en cámara en tiempo real con el modelo entrenado  

---

## Tecnologías utilizadas
- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- PyTorch  
- Roboflow  
- Numpy  

---

## Estructura real del proyecto
```
Proyecto Final/
├── train/
├── valid/
├── test/
├── data.yaml
├── final_training.py
├── camara.py
├── camara_bata_playera.py
├── metricas.py
├── verificar.py
├── limpiar_playeras.py
├── runs/detect/train12/
│ ├── weights/best.pt
│ ├── confusion_matrix.png
│ ├── BoxPR_curve.png
│ ├── results.png
│ └── results.csv
└── modelos base YOLO (yolo11m.pt, yolo8m.pt)
```

---

## Ejecución del sistema

Para ejecutar la detección en tiempo real con cámara:

```
bash
python camara.py
```

Modelo entrenado disponible aquí: https://github.com/erojas150604/ppe-detection-system/releases/tag/v1.0-model


---

## Resultados del modelo final

El entrenamiento final se encuentra en:
runs/detect/train12/

Archivos relevantes generados automáticamente por YOLOv8:

- best.pt → pesos del modelo con mejor desempeño
- confusion_matrix.png → matriz de confusión
- BoxPR_curve.png → curva Precision-Recall
- results.png → métricas generales de entrenamiento
- results.csv → historial de entrenamiento por época

Estas métricas permiten evaluar el desempeño del modelo en detección de bata y playera como elementos de protección.

---

## Aplicación en entornos industriales

Este tipo de sistema puede implementarse en:

- Monitoreo automático de cumplimiento de EPP
- Supervisión de seguridad en plantas o laboratorios
- Sistemas de alerta cuando no se detecta equipo obligatorio
- Integración con sistemas de control de acceso

Proyecto desarrollado como práctica académica con enfoque directo a aplicaciones reales de visión artificial para seguridad.

---
