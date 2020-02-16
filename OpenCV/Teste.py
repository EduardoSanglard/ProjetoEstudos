import cv2
import numpy as np
import matplotlib.pyplot as plt

branco = (255,255,255)
img = cv2.imread("Fotos\\bolinhas.jpg")
fonte = cv2.FONT_HERSHEY_SIMPLEX


#
def redim(img, largura):
    alt = int(img.shape[0]/img.shape[1]+largura)
    img = cv2.resize(img, (largura, alt), interpolation=cv2.INTER_AREA)
    return img

df = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

camera = cv2.VideoCapture(0)

while True:
    (sucesso, frame) = camera.read()
    if not sucesso:
        break

    frame = redim(frame, 320)
    frame_pb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = df.detectMultiScale(frame_pb, scaleFactor=1.1, minNeighbors=3, minSize=(20,20))
    frame_tmp = frame.copy()

    for (x,y,lar,alt) in faces:
        cv2.rectangle(frame_tmp, (x,y),(x+lar,y+alt), (0,255,255), 2)

    cv2.imshow("Janela", redim(frame_tmp, 640))

    if cv2.waitKey(1) & 0xFF == ord("s"):
        break

camera.release()
cv2.destroyAllWindows()

#Rastreando objeto azul
# azulEscuro = np.array([100,67,0], dtype="uint8")
# azulClaro = np.array([255,128,50], dtype="uint8")
#
# camera = cv2.VideoCapture(0)
#
# while True:
#     (sucesso, frame) = camera.read()
#     if not sucesso:
#         break
#
#     obj = cv2.inRange(frame, azulEscuro, azulClaro)
#
#     (cnts, _) = cv2.findContours(obj.copy(),cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
#     if len(cnts) > 0:
#         cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
#         rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
#         cv2.drawContours(frame, [rect], -1, (0,255,255),2)
#
#
#     cv2.imshow("Janela", frame)
#     cv2.imshow("Janela1", obj)
#
#     if cv2.waitKey(1) & 0xFF == ord("s"):
#         break
#
# camera.release()
# cv2.destroyAllWindows()

#Suavizar pela média/mediana
# for i in range(0, img.shape[0],15):
#     for j in range(0, img.shape[1],15):
#         img[i:i+3, j:j+3] = (255,255,255)
#
# suave = cv2.medianBlur(img,11)
# suave = cv2.Blur(img,(11,11))

#Histograma

# listaB = []
# listaR = []
# listaG = []
# listaCopiaB = []
# listaCopiaG = []
# listaCopiaR = []
#
# for i in range(0, img.shape[0]):
#     for j in range(0, img.shape[1]):
#         listaB.append(img[i][j][0])
#         listaG.append(img[i][j][1])
#         listaR.append(img[i][j][2])
#
# listaSemB = sorted(set(listaB))
# listaSemG = sorted(set(listaG))
# listaSemR = sorted(set(listaR))
#
# for i in range(0, len(listaSemB)):
#     somatoria = 0
#     for j in range(0, len(listaB)):
#         if listaSemB[i] == listaB[j]:
#             somatoria += j
#     listaCopiaB.append(somatoria)
#
# for i in range(0, len(listaSemG)):
#     somatoria = 0
#     for j in range(0, len(listaG)):
#         if listaSemG[i] == listaG[j]:
#             somatoria += j
#     listaCopiaG.append(somatoria)
#
# for i in range(0, len(listaSemR)):
#     somatoria = 0
#     for j in range(0, len(listaR)):
#         if listaSemR[i] == listaR[j]:
#             somatoria += j
#     listaCopiaR.append(somatoria)
#
# plt.plot(listaCopiaR, color='red')
# plt.plot(listaCopiaG, color='green')
# plt.plot(listaCopiaB, color='blue')
# plt.show()

#Torna a imagem preta
#for i in range(0, img.shape[0]):
#    for j in range(0, img.shape[1]):
#        img[i][j] = (0,0,0)

#Coloca textos
#cv2.putText(img,'255',(15,65), fonte,2,(255,255,255),2)
#cv2.putText(img,'70',(125,65), fonte,2,(70,70,70),2)
#cv2.putText(img,'gaaaaay',(255,65), fonte,2,(100,100,100),2)
#cv2.putText(img,'1',(405,65), fonte,2,(1,1,1),2)

#Descrove textos
#for i in range(0, img.shape[0]):
#    for j in range(0, img.shape[1]):
#        if img[i][j][0] != 1:
#            img[i][j] = (255,255,255)
#        else:
#            img[i][j] = (0,0,0)

#Rotacionar imagem
#imagemRotacionada = img[::-1,::-1]

#Redimensiona sem perder proporcao
#largura = img.shape[1]
#altura = img.shape[0]
#proporcao = float(altura/largura)
#larguraNova = 150
#alturaNova = int(larguraNova*proporcao)
#img = cv2.resize(img, (larguraNova, alturaNova))

#Crop
#imgRecorta = img[100:600, 100:600]

#Coloca texto
#cv2.putText(img,"Caio",(200,200),fonte,2,branco,2, cv2.LINE_AA)

#Mostra Valor por valor
#for i in range(0, img.shape[0]):
#    for j in range(0, img.shape[1]):
#        if img[i][j][0] == (255) and img[i][j][1] == (255) and img[i][j][3] == (255):
#            img[i][j] = (0,0,0)

#Mostar Imagem
#Separando canais de cores
#(b,g,r) = cv2.split(img)


#Histograma


#cv2.imshow("Gatos", img)
#cv2.waitKey(0)



#cv2.imshow("bolinhas", img)
#cv2.waitKey()

