# Initialisation des librairies/modules
import sys
import time
import MySQLdb
import socket
import Connexion

from PIL import Image
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

# # # # # # # # #Definition du code


class Response:

    def __init__(self, IP, PORT):
        print ">>>{0}".format(IP)
        self.tts = ALProxy("ALTextToSpeech", IP, PORT)

        db = MySQLdb.connect(host="SRV-NAO",  # your host
                             user="benjamin",  # username
                             passwd="benjamin",  # password
                             db="benjamin",  # name of the database
                             charset="utf8")

        # Create a Cursor object to execute queries.
        self.cur = db.cursor()
        # Select data from table using SQL query.
        self.cur.execute("SELECT Reponse FROM audio")
        self.prenom = "Frederic"
        self.nom = "Chopin"
        self.retard = 40

    def get_response_in_database(self):
        n = 0
        for row in self.cur.fetchall():
            if n == 0:  # Dire que la premiere ligne
                response = row[0].encode("utf-8")
                print type(response), response
                # response = response.format(self.prenom, self.nom, self.retard)
                self.tts.say(response)
                # n += 1

    def response_from_facial_recognition(self):
        is_recognized = False

        if is_recognized:
            print "Face reconnue"
            self.get_response_in_database()

        else:
            print "Aucune reconnaissance"

    def response_from_qr_code_recognition(self):
        is_recognized = True

        if is_recognized:

            self.get_response_in_database()

        else:
            print "Aucune reconnaissance"

# Response().response_from_qr_code_recognition()
