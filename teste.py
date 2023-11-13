from PIL import Image
import pytesseract
import cv2

cap = cv2.VideoCapture(0)
pytesseract.pytesseract.tesseract_cmd =  r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def pegaPlaca():
    ret, frame = cap.read()
    cv2.imwrite('captura.png', frame)
    image = Image.open('captura.png')
    image_pb = image.convert('L')
    text = pytesseract.image_to_string(image_pb)
    print("Aguardando Captura")
    if  text != "":
        print("Texto Capturado")
        print(text)
        image_pb.show()
    return text


buffer = ''
while buffer == "":
    buffer = pegaPlaca()




