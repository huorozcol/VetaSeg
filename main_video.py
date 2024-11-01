import cv2
from simple_facerec import SimpleFacerec

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)
rojo = (0,0,255)
verde = (0,255,0)
blanco = (255,250,250)

while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)

    for face_loc, name in zip(face_locations, face_names):
        #print(face_loc)
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        if (name == 'Desconocido'):
            color = rojo
        else:
            color = verde
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 0.7, color=color)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 4)
    cv2.imshow("Reconocimiento facial VETA Seguridad ", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()