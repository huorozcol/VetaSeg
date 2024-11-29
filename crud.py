import csv
import os

from conn import conn_op, conn_cl
import time

def insert_face(nombre, cam_n):
    fecha = time.strftime("%Y-%m-%d %H:%M:%S")
    my_con = conn_op()
    my_cursor = my_con.cursor()
    sql = "INSERT INTO registro (nombre, fecha, camara) VALUES(%s, %s, %s)"
    vals = (nombre, fecha, cam_n)
    my_cursor.execute(sql, vals)
    my_con.commit()
    my_con.close()

def ult_registros():

    fecha = time.strftime("%Y-%m-%d-%H-%M-%S")
    my_con = conn_op()
    my_cursor = my_con.cursor()
    path_desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    sql = "SELECT * FROM face_recog.registro order by fecha desc"
    my_cursor.execute(sql)
    #result = my_cursor.fetchall()
    # fp = open(f'./reporte{fecha}.csv', 'w')
    # myFile = csv.writer(fp)
    # myFile.writerow(result)
    # fp.close()
    with open(f'{path_desktop}\\reporte-{fecha}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([i[0] for i in my_cursor.description])
        writer.writerows(my_cursor.fetchall())


def ult_apertura(nombre):
    nombre = nombre
    my_con = conn_op()
    my_cursor = my_con.cursor()
    sql = "select   TIMESTAMPDIFF(SECOND,fecha ,NOW()) as minutes from face_recog.registro where  nombre = %s  order by fecha desc limit 1"
    pl = (nombre,)
    my_cursor.execute(sql,pl)
    result = my_cursor.fetchall()
    if (len(result)) == 0:
        insert_face(nombre,1)
        return 1
    #print(len(result))
    return result[0][0]

#ult_apertura("Hugo")


