from packages import *

# Cargar una imagen de prueba
image_path = r"..\..\data\output\divide_pages_test\pages_raw\Chapter01\page1_img.jpeg"
image = cv2.imread(image_path)

if image is None:
    print(f"No se pudo cargar la imagen: {image_path}")
else:
    # Guardar la imagen cargada
    output_path = r'..\..\data\output\divide_images_test\prueba.jpeg'
    cv2.imwrite(output_path, image)

    # Verificar si la imagen se guardó correctamente
    if os.path.exists(output_path):
        print(f"Imagen guardada correctamente en: {output_path}")
    else:
        print(f"No se pudo guardar la imagen en: {output_path}")