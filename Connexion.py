# -*- coding: utf-8 -*

import socket
from naoqi import ALProxy
import MySQLdb


class Conn:
    def __init__(self):

        db = MySQLdb.connect(host="SRV-NAO",  # your host
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

            while i < rc:

                print "***************"
                print rc
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


print "/*/*/*/*/*/*/*/*/*/"
print ("TABLE FACIALE")
Conn().get_all()
print "/*/*/*/*/*/*/*/*/*/"
print "/*/*/*/*/*/*/*/*/*/"
print ("COLONNE PHOTO")
Conn().get_one("photo")
print "/*/*/*/*/*/*/*/*/*/"