# Initialisation des librairies/modules
import sys
import time

import Recognition_Faciale
import Recognition_QRCode
import Connexion_Sql
import audio_response

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser
# # # # # # # # #Definition du code


class HumanGreeterModule(ALModule):
    """
    Un module qui reagit lorsqu'un visage est detecte
    """
    def __init__(self, name):
        ALModule.__init__(self, name)
        # IP non necessaire car le module ALBroker est utilise ici

        self.tts = ALProxy("ALTextToSpeech")

        # Subscribe FaceDetected event:
        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("FaceDetected", "HumanGreeter", "onFaceDetected")

    def onFaceDetected(self, *_args):
        """
        Cette event est appele a chaque fois qu'un visage est detecte
        """

        # Unsubcribe pour eviter les repetitions
        memory.unsubscribeToEvent("FaceDetected", "HumanGreeter")

        # Le processus qui sera appeler a chaque visage detecte*

        faceshapeinfo, nom_personne, faceextrainfo, verif = Recognition_Faciale.PeoplePerception(ip_bts, port).RecoVisage(ip_bts, port)

        if faceshapeinfo != "":
            faceshapeinfo[1] = round(faceshapeinfo[1], 3)
            print faceshapeinfo[1]
            faceshapeinfo[2] = round(faceshapeinfo[2], 3)
            print faceshapeinfo[2]
            faceshapeinfo[3] = round(faceshapeinfo[3], 3)
            print faceshapeinfo[3]
            faceshapeinfo[4] = round(faceshapeinfo[4], 3)
            print faceshapeinfo[4]

        print verif
        print''
        if verif:
            valreq = Connexion_Sql.Conn("192.168.0.19",nom_personne, faceshapeinfo[3], faceshapeinfo[4], "").RecupVal(2)

            if valreq != "":
                print valreq
                audio_response.Response(ip_bts, port)
            else:
                essaie += essaie

        elif essaie == 2:
            Recognition_QRCode.QRCode().qr_code_recognition(ip_bts, port)

        time.sleep(10)

        # Subscribe pour recommencer
        memory.subscribeToEvent("FaceDetected", "HumanGreeter", "onFaceDetected")


def main():
    """
    Main entry point
    """
    # Variables Globale
    global port
    global ip_bts
    global ip_home
    global HumanGreeter
    global essaie

    HumanGreeter = None
    # faceInfo = None
    # faceShapeInfo = None
    # faceExtraInfo = None
    # nom_personne = None
    # timeStamp = None
    # global ValReq

    ip_home = "192.168.1.43"
    ip_bts = "192.168.0.115"
    port = 9559

    parser = OptionParser()
    parser.add_option("--pip",
                      help=ip_bts,
                      dest="pip")
    parser.add_option("--pport",
                      help=port,
                      dest="pport",
                      type="int")
    parser.set_defaults(
        pip=ip_bts,
        pport=port)

    (opts, args_) = parser.parse_args()
    pip = opts.pip
    pport = opts.pport

    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
                        "0.0.0.0",  # listen to anyone
                        0,  # find a free port and use it
                        pip,  # parent broker IP
                        pport)  # parent broker port

    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable

    HumanGreeter = HumanGreeterModule("HumanGreeter")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)


if __name__ == "__main__":
    main()