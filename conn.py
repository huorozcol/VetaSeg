import mysql.connector
cnx = None
def conn_op():
    cnx = mysql.connector.connect(
        host="localhost",
        user="facerecogn",
        passwd="F4c3R3c06n",
        database="face_recog",
    )
    return cnx

def conn_cl():
    cnx.close()


