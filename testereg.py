from PIL import Image
from flask import Flask, jsonify, send_file
from flask_cors import CORS
import pytesseract
import cv2
import re


url = 'http://admin:root@1234@10.0.0.47:88/cgi-bin/guest/Video.cgi?media=JPEG'
pytesseract.pytesseract.tesseract_cmd =  r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#padrao = re.compile(r'^[A-Z]{3}-\d{4}$|^[A-Z]{3}\d[A-Z]\d{2}$')
padrao = re.compile(r'([a-z][a-z][a-z][0-9]([a-z]|[0-9])[0-9][0-9])|([a-z][a-z][a-z]\-[0-9][0-9][0-9][0-9])',re.IGNORECASE)

def binarizar(imagem):
    tamanho_corte = 250,250
    mistura = 110
    largura_original, altura_original = imagem.size
    binaryPic = imagem#.convert('L')
    binaryPic = imagem.point(lambda p: p>mistura and 255)
    binaryPic = binaryPic.convert('1', dither=Image.NONE)
    centro_x = largura_original // 2
    centro_y = altura_original // 2
    metade_largura_corte, metade_altura_corte = tamanho_corte[0] // 2, tamanho_corte[1] // 2
    x1 = centro_x - metade_largura_corte
    y1 = centro_y - metade_altura_corte
    x2 = centro_x + metade_largura_corte
    y2 = centro_y + metade_altura_corte
    binaryPic = binaryPic.crop((x1,y1,x2,y2)) #coordenadas do corte da imagem
    binaryPic = binaryPic.resize((300,300))
    binaryPic.save('binary.png')
    return binaryPic

def pegaPlaca():
    cap = cv2.VideoCapture(url)
    config = '--psm 11' 
    ret, frame = cap.read()
    cv2.imwrite('captura.png', frame)
    image = Image.open('captura.png')
    image_modificada = binarizar(image)
    text = pytesseract.image_to_string(image_modificada)
    print("Aguardando Captura")    
    texto = padrao.findall(text)
    if bool(texto) and texto[0] and texto[0][0]:
        print("Texto Capturado")
        print(texto[0][0])
        #image.show()
        return texto[0][0]


def retornar_imagem():
    return send_file('captura.png', mimetype='image/jpg')

        
app = Flask(__name__)
CORS(app, origins='*')

@app.route('/placa',methods=['GET'])
def procurar():
    while True:
        retorno = pegaPlaca()
        if bool(retorno):
            placa = {'placa':retorno}
            return jsonify(placa)

@app.route('/imagem_placa',methods=['GET'])
def retornar_imagem():
    return send_file('captura.png', mimetype='image/jpg')



if __name__ == '__main__':
    app.run(debug=True)