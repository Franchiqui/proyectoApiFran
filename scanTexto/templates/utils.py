import skimage.io
import skimage.color
import skimage.filters
import pytesseract

def scanTexto_func(imagePath):
    """
    Extrae texto de una imagen y lo devuelve como cadena.

    Argumentos:
        imagePath (str): Ruta al archivo de imagen a escanear.

    Retorno:
        str: El texto extraído de la imagen.
    """

    # Cargar la imagen utilizando scikit-image
    img = skimage.io.imread(imagePath)

    # Convertir la imagen a escala de grises
    gray = skimage.color.rgb2gray(img)

    # Aplicar umbralización para convertir a una imagen binaria
    threshold_img = gray > skimage.filters.threshold_otsu(gray)

    # Establecer la ruta de Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'C:/Archivos de programa/Tesseract-OCR/tesseract.exe'

    # Establecer el idioma del texto
    text = pytesseract.image_to_string(img, config='--psm 10 lang=es')

    # Extraer texto usando pytesseract
    text = pytesseract.image_to_string(threshold_img)

    # Devolver el texto extraído
    return text
