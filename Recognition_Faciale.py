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


class PeoplePerception(object):

    def __init__(self, IP, PORT):
        self.proxy = None

        self.RecoVisage(IP, PORT)

    def RecoVisage(self, IP, PORT):

        faceproxy = ALProxy("ALFaceDetection", IP, PORT)
        faceproxy.subscribe("Test_Face", 500, 0.0)

        memoryFace = ALProxy("ALMemory", IP, PORT)
        memValue = "FaceDetected"


        for i in range(0, 20):
            time.sleep(0.5)
            face = memoryFace.getData(memValue)

            print ""
            print "*****"
            print ""

            # Verification lorsque que la donnee renvoyer est correcte
            if (face and isinstance(face, list) and len(face)) >= 2:

                # Visage detecte
                # Pour chaque visage, les valeurs de ce derniers sont recuperer

                # Premier champ = Valeur de temps
                timeStamp = face[0]

                # Deuxieme champ = Face Info.
                faceInfoArray = face[1]

                try:
                    # Pour recuperer chaque valeur de chaque visage rencontre
                    for j in range(2): #len(faceInfoArray) - 1):
                        faceInfo = faceInfoArray[j]

                        # Premier champ = info de forme
                        faceShapeInfo = faceInfo[0]

                        # Second champ = info bonus
                        faceExtraInfo = faceInfo[1]

                        # print faceInfo
                        # print "  Dist %.3f - Angle %.3f" % (faceShapeInfo[1], faceShapeInfo[2])  # Valeur de distane et d'angle de vue entre le robot et le visage
                        # print "  Largeur %.3f - Hauteur %.3f" % (faceShapeInfo[3], faceShapeInfo[4]) # Valeur de largeur et de hauteur du visage dectecte

                        if faceExtraInfo[2] != "":
                            nom_personne = faceExtraInfo[2]
                            print " Nom = %s" % (faceExtraInfo[2])
                            Verif = True
                            return faceShapeInfo, nom_personne, faceExtraInfo, str(Verif)
                        else:
                            print " Personne inconnu du systemes"
                            Verif = False
                            return str(Verif)

                except Exception, e:
                    print "Visage dectecte mais donnee invalide. ALValue ="
                    print face
                    print "Message d'erreur %s" % (str(e))
                    Verif = False
                    return str(Verif)
            else:
                print "Pas de visage detecte"
                Verif = False
                return str(Verif)