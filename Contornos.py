import cv2
import numpy as np

video_path = "C:/Users/chent/Documents/Video_Carro.mp4"
capture = cv2.VideoCapture(video_path)

kernel_size = (5, 5)
low_threshold = 50
high_threshold = 150

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Procesamiento
    blur = cv2.GaussianBlur(frame, kernel_size, 1)
    gray_image = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray_image, low_threshold, high_threshold)

    kernel = np.ones((5, 5), np.uint8)
    dilated = cv2.dilate(canny, kernel, iterations=1)

    # Mostrar resultados intermedios
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Blurred Frame', blur)
    cv2.imshow('Gray Frame', gray_image)
    cv2.imshow('Canny Edges', canny)
    cv2.imshow('Dilated Image', dilated)

    # Espera para salir
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
