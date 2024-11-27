from time import sleep
from trace import Trace
import cv2
from numpy.ma.core import shape
#import open_door
#import open_door
from crud import *
from simple_facerec import SimpleFacerec
import time
import numpy as np

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

rojo = (0,0,255)
verde = ( 0, 140, 13 )
blanco = (255,250,250)

def zoomframe(frame, scale):

    width = int(frame.shape[1]*scale)
    heigth = int(frame.shape[0] * scale)
    dimensions = (width,heigth)

    return cv2.resize(frame,dimensions, interpolation=cv2.INTER_AREA)


def comparar_faces(scale, *args):

    cam_n = 1
    for frame in args:


        if frame is not None:
            frame = zoomframe(frame, scale)
            face_locations, face_names = sfr.detect_known_faces(frame)
            for face_loc, name in zip(face_locations, face_names):
                name = name[:40]

                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
                if name == 'Desconocido':
                    print(f"Visitante en camara {cam_n}, ============== no se abre la puerta. ======================")
                    color = rojo
                else:
                    tUltimaApertura = ult_apertura(name)
                    if tUltimaApertura > 20:
                        print(f"Bienvenido: {name},  en camara {cam_n} @@@@@@@@@@@@@ Se abre la puerta @@@@@@@@@@@@@@")
                        insert_face(name, cam_n)
                        #descomentar para que funcione, yo no la puedo descomentar porque no tengo el dispositvo usb y me va a tirar error
                        #open_door.on_relay(1)
                        sleep(1)
                        # open_door.oFF_relay(1)
                        sleep(1)
                    else:
                        print(f"Bienvenido: {name},  en camara {cam_n}.")

                key = cv2.waitKey(1)
                if key == 27:
                    break

        print(cam_n)
        cam_n += 1




