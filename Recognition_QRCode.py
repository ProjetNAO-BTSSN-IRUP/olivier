# Initialisation des librairies/modules
import time

from naoqi import ALProxy

# # # # # # # # #Definition du code


class QRCode:
    def __init__(self):
        self.proxy = None

    def qr_code_recognition(self, ip, port):
        barcode = ALProxy("ALBarcodeReader", ip, port)
        barcode.subscribe("test_barcode")

        memory = ALProxy("ALMemory", ip, port)

        for i in range(20):
            data = memory.getData("BarcodeReader/BarcodeDetected")
            if data:
                is_recognized = True
                data = data[0][0].split(",")
                print type(int(data[0])), data[0]
                time.sleep(1)
                return is_recognized, data