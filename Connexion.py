# -*- coding: utf-8 -*

import socket
from naoqi import ALProxy
import MySQLdb


class Conn:
    def __init__(self):

        # ip_nao = "192.168.0.115"

        # print ">>>{0}".format(ip_nao)

        # self.tts = ALProxy("ALTextToSpeech", ip_nao, 9559)

        db = MySQLdb.connect(host="127.0.0.1",  # your host
                             user="olivier",  # username
                             passwd="olivier",  # password
                             db="olivier")  # name of the database

        # Create a Cursor object to execute queries.
        self.cur = db.cursor()

        # Select data from table using SQL query.
        self.cur.execute("SELECT * FROM faciale")

    def get_all(self):
        i = 0
        rc = self.cur.rowcount
        for row in self.cur.fetchall():
            # response = self.tts.say(row[0])

            while i < rc:

                print "***************"
                print ""
                print row[i]
                print ""
                print "***************"
                i += 1

    def get_one(self, nom_col):
        id_faciale = 0
        photo = 1
        id_app = 2
        id_int = 3
        col = 0

        if nom_col == "id_faciale":
            col = id_faciale
        elif nom_col == "photo":
            col = photo
        elif nom_col == "id_app":
            col = id_app
        elif nom_col == "id_int":
            col = id_int

        for row in self.cur.fetchall():

            print "***************"
            print ""
            print row[col]
            print ""
            print "***************"

            return row[col]


Conn().get_one("id_app")