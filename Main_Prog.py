# Initialisation des librairies/modules

import socket
import MySQLdb
import time
import os
import sys
import vision_definitions
from naoqi import ALProxy
from Connexion import Conn

# Definition du code


class Nao:
    def __init__(self):

        print "Bonjour"
        print "cc"

    def test(self):
        hptxt = Conn.get_one("photo")
        return hptxt


Nao().test()