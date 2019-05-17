# Initialisation des librairies/modules
from naoqi import ALProxy
# # # # # # # # #Definition du code


class LearnFace(object):

    def __init__(self, ip, port):
        self.peopleproxy = ALProxy("ALFaceDetection", ip, port)

    def SetPpl(self, nompersonne):

        self.peopleproxy.subscribe("FaceDetection", 500, 00)

        self.peopleproxy.setRecognitionEnabled = True
        self.peopleproxy.setTrackingEnabled = True

        print self.peopleproxy.learnFace(nompersonne)
        print self.peopleproxy.getLearnedFacesList()

        self.peopleproxy.unsubscribe

    def getData(self, ip, port):

        self.memproxy = ALProxy("ALFaceDetection", ip, port)


LearnFace("192.168.0.115", 9559).SetPpl("Benjamin")