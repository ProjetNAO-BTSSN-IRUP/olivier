
import sys
import time

# Python Image Library
from PIL import Image

import naoqi
from naoqi import ALProxy



class PeoplePerception(object):

    def __init__(self, IP, PORT):
        self.proxy = None

        print "PeoplePerception"
        print "**********************************"
        self.NewPpl(IP, PORT)
        print ""

        print "FaceDetection"
        print"***********************************"
        self.RecoPpl(IP, PORT)
        print ""

        print self.proxy.getSubscribersInfo()

    def NewPpl(self, IP, PORT):
        if not self.proxy:
            self.proxy = ALProxy("ALPeoplePerception", IP, PORT)
            self.proxy.subscribe("PeoplePerception", 500, 0.0)

        print self.proxy.isFaceDetectionEnabled()
        if self.proxy.PeopleDetected is True:
            print "Detected"
        else:
            print "nada"

        print self.proxy.PeopleList

        self.proxy.unsubscribe

    def RecoPpl(self, IP, PORT):
        self.proxy = ALProxy("ALFaceDetection", IP, PORT)
        self.proxy.subscribe("FaceDetection", 5000, 00)

        self.proxy.setRecognitionEnabled = True
        print self.proxy.isRecognitionEnabled()

        self.proxy.setTrackingEnabled = True
        print self.proxy.isTrackingEnabled()

        print self.proxy.getLearnedFacesList()
        print self.proxy.learnFace("Nicolas")

        print self.proxy.FaceDetected


PeoplePerception("192.168.0.115", 9559)