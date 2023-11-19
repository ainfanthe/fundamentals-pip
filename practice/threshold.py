import cv2
imagen = cv2.imread('bookpage.jpg',
                    cv2.IMREAD_GRAYSCALE)

_, threhold_img = cv2.threshold(imagen, 
                                14,
                                255,
                                cv2.THRESH_BINARY)

cv2.imshow('Imagen original', imagen)
cv2.imshow('Imagen umbralizada', threhold_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Los umbrales permiten segmentar una imagen en regiones distintas

