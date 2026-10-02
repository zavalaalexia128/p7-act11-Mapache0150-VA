# Ejemplo1: Conversacion entre BGR, RGB y escala de grises
# Zavala Medina NC = 0150

import cv2
import matplotlib.pyplot as plt

# 1. Cargar imagen desde disco (OpenCV la lee en formato BGR)
img_bgr = cv2.imread('Mapache.jpg')

# 2. Conversión BGR -> RGB (para visualizar correctamente con Matplotlib)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# 3. Conversión BGR -> Escala de grises (1 solo canal)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# 4. Mostrar los resultados comparativos
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(img_bgr)
axes[0].set_title("Original en OpenCV (BGR incorrecto)")

axes[1].imshow(img_rgb)
axes[1].set_title("Convertido a RGB")

axes[2].imshow(img_gray, cmap='gray')
axes[2].set_title("Escala de Grises")

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()

print("Zavala Medina NC = 0150")
