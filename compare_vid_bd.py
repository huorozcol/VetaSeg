from time import sleep

import cv2
from numpy.ma.core import shape


#import open_door
from crud import *
from simple_facerec import SimpleFacerec
import time


# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")


rojo = (0,0,255)
verde = ( 0, 140, 13 )
blanco = (255,250,250)


def comparar_faces(*args):

    cam_n = 1
    #print(f'frames enviados {len(args)}')
    for frame in args:
        if frame is not None:
            face_locations, face_names = sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                name = name
                # print(face_loc)
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                if name == 'Visitante':
                    color = rojo
                else:
                    color = verde
                    #descomentar para que funcione, yo no la puedo descomentar porque no tengo el dispositvo usb y me va a tirar error
                    #open_door.on_relay(1)

                cv2.putText(frame, 'Bienvenido' + name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 0.7, color=color)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 4)
                insert_face(name, cam_n)

                key = cv2.waitKey(1)
                if key == 27:
                    break

            if cam_n == 1:
                # cv2.imshow("Reconocimiento facial ITM - Prueba - ", frame)
                # cv2.waitKey(1)
                cont_frame = +1
            else:
                continue

