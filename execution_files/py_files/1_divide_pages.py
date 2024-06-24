from packages import *

#Función para dividir las páginas del pdf

def extract_images_from_pdf(pdf_path, output_folder):
    document = fitz.open(pdf_path)
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_path = f"{output_folder}/page{page_num+1}_img.{image_ext}"
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
    print(f"Images extracted and saved to {output_folder}")

#Función para crear un archivo con todas las rutas de las páginas separadas anteriormente

def create_image_list(input_folder, output_csv):
    #Crear y Escribir el archivo
    with open(output_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        for img_name in os.listdir(input_folder):
            img_path = os.path.join(input_folder, img_name)
            writer.writerow([img_path])

input_directory = r'.\data\input\Comic_test'
output_directory = r'.\data\output\divide_pages_test\pages_raw'
output_directory_csv = r'.\data\output\divide_pages_test\pages_routes\images_routes.csv'

#Primero borrar el archivo de lista csv si existe
if os.path.exists(output_directory_csv):
    os.remove(output_directory_csv)
    print(f"Archivo '{output_directory_csv}' eliminado correctamente.")
else:
    print(f"El archivo '{output_directory_csv}' no existe, se va a crear.")

#Eliminar subestructura creada de una ejecución anterior
def eliminar_subdirectorios(directorio):
    if os.path.exists(directorio) and os.path.isdir(directorio):
        elementos = os.listdir(directorio)
        if elementos:
            for elemento in elementos:
                ruta_elemento = os.path.join(directorio, elemento)
                if os.path.isdir(ruta_elemento):
                    shutil.rmtree(ruta_elemento)
                    print(f"Se ha eliminado el subdirectorio: {ruta_elemento}")
                else:
                    print(f"'{ruta_elemento}' no es un directorio, no se eliminará.")
        else:
            print(f"El directorio {directorio} está vacío.")
    else:
        os.mkdir(output_directory)
        print(f"El directorio {directorio} no existe o no es un directorio.")

# Definir la ruta
output_directory = r'.\data\output\divide_pages_test\pages_raw'

# Eliminar solo los subdirectorios dentro de output_directory
eliminar_subdirectorios(output_directory)

# Recorrer el directorio de forma recursiva
for raiz, subcarpetas, archivos in os.walk(input_directory):
    # Procesar subcarpetas
    for subcarpeta in subcarpetas:
        print(f"Subcarpeta: {subcarpeta}")
        ruta_carpeta_salida = f"{output_directory}\\{subcarpeta}"
        # verificamos si el directorio que vamos a crear, de salida, existe
        os.mkdir(ruta_carpeta_salida)
        print("Directorio %s creado!" % ruta_carpeta_salida)
        # Procesar archivos
        directorio_procesado = f"{input_directory}\\{subcarpeta}"
        procesado_archivos = os.listdir(f"{input_directory}\\{subcarpeta}")
        # Procesar cada nombre de archivo
        for nombre_archivo in procesado_archivos:
            print(f"Procesando carpeta: {directorio_procesado}")
            print(f"Archivo: {nombre_archivo}")
            print(f"Ruta de la carpeta de salida: {ruta_carpeta_salida}")
            # verificamos si el archivo que vamos a crear, de salida, existe
            extract_images_from_pdf(f"{directorio_procesado}\\{nombre_archivo}", ruta_carpeta_salida)
            create_image_list(ruta_carpeta_salida, output_directory_csv)
            print(f"Fichero de rutas creado en {output_directory_csv} !")