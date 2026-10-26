import cv2
import math
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Configuração do Hand Landmarker para detetar ATÉ 2 MÃOS
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2,  # <--- Alterado para 2 mãos
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5
)
detector = vision.HandLandmarker.create_from_options(options)

# Inicializa a captura de vídeo da webcam
cap = cv2.VideoCapture(0)

print("Pressione 'q' na janela do vídeo para sair.")

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Não foi possível ler o frame da câmera.")
        break

    # Espelha a imagem horizontalmente (modo espelho)
    image = cv2.flip(image, 1)
    height, width, _ = image.shape

    # Converte para RGB e cria o objeto do MediaPipe
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)

    # Processa a detecção
    detection_result = detector.detect(mp_image)

    status_texto = "Mostre as duas maos..."

    # Se detetar 2 mãos em simultâneo
    if detection_result.hand_landmarks and len(detection_result.hand_landmarks) == 2:
        mao1 = detection_result.hand_landmarks[0]
        mao2 = detection_result.hand_landmarks[1]

        status_texto = "Duas maos interligadas! 💖"

        # Pontos principais para interligar entre as duas mãos (Ex: Pontas dos Polegares [4] e Indicadores [8])
        pontos_para_ligar = [4, 8, 12, 16, 20]

        for idx in pontos_para_ligar:
            p1 = mao1[idx]
            p2 = mao2[idx]

            x1, y1 = int(p1.x * width), int(p1.y * height)
            x2, y2 = int(p2.x * width), int(p2.y * height)

            # Desenha uma linha cor de rosa a interligar os dedos correspondentes das duas mãos
            cv2.line(image, (x1, y1), (x2, y2), (203, 192, 255), 2)
            
            # Círculos cor de rosa nas pontas
            cv2.circle(image, (x1, y1), 6, (203, 192, 255), -1)
            cv2.circle(image, (x2, y2), 6, (203, 192, 255), -1)

        # Desenha os pontos de ambas as mãos discretamente
        for hand_landmarks in detection_result.hand_landmarks:
            for landmark in hand_landmarks:
                x = int(landmark.x * width)
                y = int(landmark.y * height)
                cv2.circle(image, (x, y), 2, (150, 150, 200), -1)

    elif detection_result.hand_landmarks and len(detection_result.hand_landmarks) == 1:
        status_texto = "Mostre a segunda mao..."

    # Cria painel superior com borda e tema rosa
    cv2.rectangle(image, (20, 20), (450, 90), (50, 20, 50), -1)
    cv2.rectangle(image, (20, 20), (450, 90), (203, 192, 255), 2)

    # Escreve o estado no ecrã
    cv2.putText(image, status_texto, (35, 70), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (203, 192, 255), 2)

    # Mostra a imagem resultante
    cv2.imshow('Interligando Duas Maos', image)

    # Sai do loop ao pressionar a tecla 'q'
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()