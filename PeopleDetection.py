
import sys
import time

# Python Image Library
from PIL import Image

import naoqi
from naoqi import ALProxy


class PeoplePerception(object):

    def __init__(self, IP, PORT):
        self.proxy = None
        self.NewPpl(IP, PORT)

    def NewPpl(self, IP, PORT):
        if not self.proxy:
            self.proxy = ALProxy("ALPeoplePerception", IP, PORT)
        if self.proxy.isFaceDetectionEnabled():
            print ""


PeoplePerception("192.168.0.115", 9559)