# á é í ó ú ñ
import cv2
import tkinter as tk
from threading import Thread
from tkinter import Entry, Scale, Checkbutton, IntVar, Button
import csv
from compare_vid_bd import comparar_faces
from config import create_direct
from PIL import ImageTk, Image
import simple_facerec
import crud
import time

class GUI:
    def __init__(self, winroot):
        self.frame2 = None
        self.frame1 = None
        self.selection_cb = None
        print('Instanciada la clase GUI')
        self.img2_path = 'dbfaces/hugo1.jpeg'
        self.is_running=None
        self.flag_video_capture = False
        self.ret1 = None
        self.ret2 = None
        self.cap1 = None
        self.cap2 = None
        self.count_fr = 0
        self.var_cb_showcv2 = IntVar()
        self.winroot = winroot
        self.winroot.title("VETA Seguridad - Acceso Facial -")
        self.fr_data_camara = tk.Frame(self.winroot, width=600, height=200, borderwidth=2, relief='groove').place(x=10,y=10)
        self.ip_label = tk.Label(self.winroot, text='Ingrese la dirección de la cámara:').place(x=15,y=15)

        self.txb_ip_camara1 = Entry(self.winroot, width=70)
        self.txb_ip_camara1.insert(0,"rtsp://192.168.1.172:554")
        self.txb_ip_camara1.place(x=15,y=35)

        self.txb_ip_camara2 = Entry(self.winroot, width=70)
        self.txb_ip_camara2.insert(0, "rtsp://admin:admin@192.168.1.201:1935")
        self.txb_ip_camara2.place(x=15, y=55)

        self.bt_connect_camara = (tk.Button(self.winroot, text='Conectar', command=self.get_camara_ip))
        self.bt_connect_camara.place(x=350,y=105)
        self.bt_unplug_camara = (tk.Button(self.winroot, text='Desconectar', command=self.unplug_camara))
        self.bt_unplug_camara.config(state='disabled')
        self.bt_unplug_camara.place(x=475,y=105)
        self.lb_framerate = tk.Label(self.winroot, text='Frames Skip ')
        self.lb_framerate.place(x=17,y=130)
        self.sc_framerate = Scale(self.winroot, from_=1, to=30, orient=tk.HORIZONTAL)
        self.sc_framerate.set(10)
        self.sc_framerate.place(x=152, y=105)
        # self.chb_show_cv2 = tk.Checkbutton(self.winroot, state='normal', onvalue=1, offvalue=0, text='Ver Video', variable=self.var_cb_showcv2)
        # self.chb_show_cv2.select()
        # self.chb_show_cv2.place(x=290,y=130)
        self.lb_framerate = tk.Label(self.winroot, text='Tiempo apertura ')
        self.lb_framerate.place(x=17, y=159)
        self.sc_timer_door = Scale(self.winroot, from_=1, to=5, orient=tk.HORIZONTAL)
        self.sc_timer_door.set(3)
        self.sc_timer_door.place(x=152, y=145)

        self.lb_stat_camara = tk.Label(self.winroot, text='')
        self.lb_stat_camara.place(x=15,y=185)
        self.fr_data_personal = tk.Frame(self.winroot, width=600, height=200, borderwidth=2, relief='groove')
        self.fr_data_personal.place(x=10,y=270)
        self.lb_status_detect_face = tk.Label(self.fr_data_personal, text='')
        self.bt_downl_reg = (tk.Button(self.fr_data_personal, text='Descargar Reporte', command=self.unplug_camara))
        self.bt_downl_reg.place(x=20,y=10)
        self.lb_status_detect_face.place(x=15,y=15)
        self.ph_image_detected = tk.PhotoImage(file='')
        self.lb_image_detected = tk.Label(self.fr_data_personal, image=self.downl_reporte())
        self.lb_image_detected.place(x=200,y=10)

    def downl_reporte(self):

        rows = crud.ult_registros()





    def close_gui(self):
        print("Cerrando la ventana")
        self.winroot.destroy()

    def get_camara_ip(self):
        #print('Intentando conexion camara 1')
        ip_camara1 = self.txb_ip_camara1.get()
        ip_camara1.replace(" ","")

        ip_camara2 = self.txb_ip_camara2.get()
        ip_camara2.replace(" ", "")

        if len(ip_camara1) == 0:
            ip_camara1 = None

        if len(ip_camara2) == 0:
            ip_camara2 = None

        self.plug_camera(ip_camara1,ip_camara2)


    def plug_camera(self, ip_camara1, ip_camara2):
        self.lb_status_detect_face.config(text="")
        self.lb_stat_camara.config(text="")
        if not self.flag_video_capture:
            print('Inicia capture videos')
            #aqui es donde esta quemado el codigo.
            if  ip_camara1 is not None: self.cap1 = cv2.VideoCapture(ip_camara1)
            if  ip_camara2 is not None: self.cap2 = cv2.VideoCapture(ip_camara2)
            self.flag_video_capture = True


        # self.cap2 = cv2.VideoCapture(ip_camara2)
##################### cam 1 ############3
        if self.cap1 is  None or not self.cap1.isOpened():
            self.txb_ip_camara1.delete(0, 200)
            self.txb_ip_camara1.insert(0,"Error conectando la camara 1")
        else:

            self.lb_stat_camara.config(text="Camara conectada", fg='green')
            self.txb_ip_camara1.config(state='disabled')
            self.bt_unplug_camara.config(state='active')
            self.bt_connect_camara.config(state='disabled')
            self.is_running = True
            self.show_frames()
            ##############################
##################### cam2 ##############

        if self.cap2 is None or not self.cap2.isOpened():
            self.txb_ip_camara2.delete(0,200)
            self.txb_ip_camara2.insert(0,"Error conectando la camara 2")

        else:
            self.lb_stat_camara.config(text="Camara conectada", fg='green')
            self.txb_ip_camara2.config(state='disabled')
            self.bt_unplug_camara.config(state='active')
            self.bt_connect_camara.config(state='disabled')
            self.is_running = True

            self.show_frames()
            #################################

    def show_frames(self):
        if self.is_running and self.flag_video_capture:
            self.count_fr += 1
            if self.cap1 is not None:
                self.ret1, self.frame1 = self.cap1.read()
            if self.cap2 is not None:
                self.ret2, self.frame2 = self.cap2.read()

            if self.ret1:
                self.frame1 = cv2.resize(self.frame1,(640,480))

            if self.ret2:
                self.frame2 = cv2.resize(self.frame2, (640, 480))


            if self.count_fr % self.sc_framerate.get() == 0 and self.ret1:
                th_showcv2 = Thread(target=comparar_faces, args=(self.frame1,self.frame2,))
                th_showcv2.run()
                if self.var_cb_showcv2.get() == 1:
                    pass
            self.ult_registros()
            self.lb_stat_camara.after(1, self.show_frames)
        else:
            self.unplug_camara()

    def show_cv2(self, frame):

        cv2.imshow('Camara Reconocimiento Facial - ITM -', self.frame1)
        cv2.waitKey(1)

    def unplug_camara(self):
        self.lb_status_detect_face.config(text="")
        self.lb_stat_camara.config(text="")
        self.cap = None
        self.is_running =False
        self.bt_connect_camara.config(state='active')
        self.bt_unplug_camara.config(state='disabled')
        self.txb_ip_camara1.config(state='normal')
        self.txb_ip_camara2.config(state='normal')

    def get_time_open(self):
        return self.sc_timer_door.get()

    def ult_registros(self):
        results = crud.ult_registros()

        for result in results:
            print(result)



if __name__ == '__main__':
    winroot = tk.Tk()
def startAll():
    print('funcion start all')
    app = GUI(winroot)
    winroot.geometry('640x480')
    winroot.protocol("WM_DELETE_WINDOW", app.close_gui)
th_startAll = Thread(target=startAll, args=(), daemon=True)
th_startAll.run()
create_direct()
winroot.mainloop()