import cv2

carregaAlgoritimo = cv2.CascadeClassifier('Haarcascade\haarcascade_frontalface_default.xml')

imagem = cv2.imread('Fotos\imagem4.jpg')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = carregaAlgoritimo.detectMultiScale(imagemCinza)

print(faces)

for(x,y, l ,a) in faces:
    cv2.rectangle(imagem, (x, y,), (x + l, y + a), (0, 255, 0))

cv2.imshow("Faces", imagem)
cv2.waitKey()