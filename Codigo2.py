import cv2

carregaFace = cv2.CascadeClassifier('Haarcascade\haarcascade_frontalface_default.xml')

carregailho = cv2.CascadeClassifier('Haarcascade\haarcascade_eye.xml')

imagem = cv2.imread('Fotos\imagem7.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaFace.detectMultiScale(imagemCinza, scaleFactor=1.05, minNeighbors=4, maxSize=(35, 35))

print(faces)

print(faces)

for(x,y, l ,a) in faces:
    imagem = cv2.rectangle(imagem, (x, y,), (x + l, y + a), (255, 0, 255), 2)
    localOlho = imagem[y:y + a, x:x, + 1]
    localOlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY) 
    detectado = carregailho.detectMultiScale(localOlho, scaleFactor=1.08)

    
    for(ox,oy, ol ,oa) in detectado:
        cv2.rectangle(localOlho, (ox, oy,), (ox + ol, oy + oa), (0, 0, 255), 2)    

cv2.imshow("Detecta faces e olhos", imagem)
cv2.waitKey()