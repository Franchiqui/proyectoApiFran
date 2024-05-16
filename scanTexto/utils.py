import cv2
import pytesseract

def scanTexto_func():
    """
    Extrae texto de una imagen y lo devuelve como cadena.
    Retorno:
        str: El texto extraído de la imagen.
    """
    # Ruta de la imagen predefinida
    imagePath = "ruta/a/la/imagen.jpg"
    
    # Cargar la imagen
    img = cv2.imread(imagePath)
    
    # Comprobar si la imagen se leyó correctamente
    if img is None:
        raise Exception("Error loading image: {}".format(imagePath))
    
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplicar umbrales para convertir a una imagen binaria
    threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    
    # Establecer la ruta de Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:/Archivos de programa/Tesseract-OCR/tesseract.exe'
    
    # Extraer texto usando pytesseract
    text = pytesseract.image_to_string(threshold_img)
    
    # Devolver el texto extraído
    return text
