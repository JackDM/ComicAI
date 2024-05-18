import cv2
import numpy as np

# Cargar la imagen del cómic
image = cv2.imread('comic.jpg')

# Convertir a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización
_, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

# Detectar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtrar contornos pequeños (opcional)
min_area = 1000
contours = [c for c in contours if cv2.contourArea(c) > min_area]

# Crear una lista para almacenar las viñetas
panels = []

for contour in contours:
    # Obtener el rectángulo delimitador de cada contorno
    x, y, w, h = cv2.boundingRect(contour)
    
    # Extraer la viñeta usando el rectángulo delimitador
    panel = image[y:y+h, x:x+w]
    panels.append(panel)
    
    # (Opcional) Dibujar rectángulos alrededor de las viñetas en la imagen original
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar la imagen con los rectángulos dibujados
cv2.imshow('Viñetas detectadas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar cada viñeta como una imagen separada
for i, panel in enumerate(panels):
    cv2.imwrite(f'panel_{i}.jpg', panel)
