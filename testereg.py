from PIL import Image
import pytesseract
import cv2
import re

url = 'http://admin:root@1234@10.0.0.47:88/cgi-bin/guest/Video.cgi?media=JPEG'
cap = cv2.VideoCapture(url)
pytesseract.pytesseract.tesseract_cmd =  r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
padrao = re.compile(r'^[A-Z]{3}-\d{4}$|^[A-Z]{3}\d[A-Z]\d{2}$')

ret, frame = cap.read()
cv2.imwrite('captura.png', frame)
image = Image.open('captura.png')
#text = pytesseract.image_to_string(image)
image.show()

""" def pegaPlaca():
    ret, frame = cap.read()
    cv2.imwrite('captura.png', frame)
    image = Image.open('placa2.jpg')
    image_pb = image.convert('L')
    text = pytesseract.image_to_string(image_pb)
    print("Aguardando Captura")
    if padrao.match(text):
        print("Texto Capturado")
        print(text)
        image_pb.show()
        return text

while True:
    pegaPlaca()
     """

""" if padrao.match("ABC1334"):
    print("Válida")
else:
    print("Não válida")
 """
