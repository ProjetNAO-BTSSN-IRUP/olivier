
import sys
import time

from PIL import Image
from naoqi import ALProxy


class PeoplePerception(object):

    def __init__(self, IP, PORT):
        self.proxy = None

        print "FaceDetection"
        print"***********************************"
        self.SetPpl(IP, PORT)
        print ""

        print "PeoplePerception"
        print "**********************************"
        self.NewPpl(IP, PORT)
        print ""

    def NewPpl(self, IP, PORT):
        self.faceproxy = ALProxy("ALPeoplePerception", IP, PORT)
        self.faceproxy.subscribe("PeoplePerception", 500, 0.0)

        print self.faceproxy.isFaceDetectionEnabled()
        for i in range(10):
            print i
            if self.faceproxy.PeopleDetected:
                print "Detected"
                print
            else:
                print "nada"
            i = i + 1

        print self.faceproxy.PeopleList

        self.faceproxy.unsubscribe

    def SetPpl(self, IP, PORT):
        self.peopleproxy = ALProxy("ALFaceDetection", IP, PORT)
        self.peopleproxy.subscribe("FaceDetection", 500, 00)

        self.peopleproxy.setRecognitionEnabled = True
        print self.peopleproxy.isRecognitionEnabled()

        if not self.peopleproxy.isTrackingEnabled() :
            self.peopleproxy.setTrackingEnabled = True

        print self.peopleproxy.isTrackingEnabled()

        print self.peopleproxy.getLearnedFacesList()
        print self.peopleproxy.learnFace("Olivier")

        self.peopleproxy.unsubscribe

    def getData(self, IP, PORT):

        self.memproxy = ALProxy("ALFaceDetection", IP, PORT)


PeoplePerception("192.168.0.115", 9559)