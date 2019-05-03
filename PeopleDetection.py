
import sys
import time

from PIL import Image
from naoqi import ALProxy


class PeoplePerception(object):

    def __init__(self, IP, PORT):
        self.proxy = None

        print "FaceDetection"
        print"***********************************"
        # self.SetPpl(IP, PORT)
        print ""

        print "PeoplePerception"
        print "**********************************"
        self.NewPpl(IP, PORT)
        print ""

    def NewPpl(self, IP, PORT):
        # faceproxy = ALProxy("ALPeoplePerception", IP, PORT)

        faceproxy = ALProxy("ALFaceDetection", IP, PORT)
        faceproxy.subscribe("Test_Face", 500, 0.0)

        memory = ALProxy("ALMemory", IP, PORT)
        memValue = "FaceDetected"


        for i in range(0, 20):
            time.sleep(0.5)
            face = memory.getData(memValue)

            print ""
            print "*****"
            print ""

            # Check whether we got a valid output.
            if face and isinstance(face, list) and len(face) >= 2:

                # We detected faces !
                # For each face, we can read its shape info and ID.

                # First Field = TimeStamp.
                timeStamp = face[0]
                if timeStamp:
                    print time

                # Second Field = array of face_Info's.
                faceInfoArray = face[1]

                try:
                    # Browse the faceInfoArray to get info on each detected face.
                    for j in range(len(faceInfoArray) - 1):
                        faceInfo = faceInfoArray[j]


                        # First Field = Shape info.
                        faceShapeInfo = faceInfo[0]

                        # Second Field = Extra info (empty for now).
                        faceExtraInfo = faceInfo[1]

                        print faceInfo
                        print "  alpha %.3f - beta %.3f" % (faceShapeInfo[1], faceShapeInfo[2])
                        print "  width %.3f - height %.3f" % (faceShapeInfo[3], faceShapeInfo[4])

                except Exception, e:
                    print "faces detected, but it seems getData is invalid. ALValue ="
                    print face
                    print "Error msg %s" % (str(e))
            else:
                print "No face detected"


PeoplePerception("192.168.0.115", 9559)