# -*- encoding: UTF-8 -*-
# Get an image from NAO. Display it and save it using PIL.

import sys
import time

# Python Image Library
from PIL import Image

from naoqi import ALProxy


def showNaoImage(IP, PORT):
    """
    First get an image from Nao, then show it on the screen with PIL.
    """

    camProxy = ALProxy("ALVideoDevice", IP, PORT)
    resolution = 2    # VGA
    colorSpace = 11   # RGB

    videoClient = camProxy.subscribe("python_client", resolution, colorSpace, 5)

    t0 = time.time()

    # Recupère l'image depuis la cam du Robot NAO
    # image[6] contient les caractères ASCII d
    naoImage = camProxy.getImageRemote(videoClient)

    t1 = time.time()

    # temps d'acquisition pour l'image
    print "acquisition delay ", t1 - t0

    camProxy.unsubscribe(videoClient)

    # Now we work with the image returned and save it as a PNG  using ImageDraw
    # package.

    # Get the image size and pixel array.
    imageWidth = naoImage[0]
    imageHeight = naoImage[1]
    array = naoImage[6]

    # Create a PIL Image from our pixel array.
    image = Image.frombytes("RGB", (imageWidth, imageHeight), array)

    # Save the image.
    image.save("C:\Users\OBayon\PycharmProjects\NAO\Photos_Reco\camImage.png", "PNG")
    image.show()


if __name__ == '__main__':
    IP = "192.168.0.115"  # Replace here with your NaoQi's IP address.
    PORT = 9559
    naoImage = showNaoImage(IP, PORT)

    # Read IP address from first argument if any.
    #if len(sys.argv) > 1:
        #IP = sys.argv[1]

        #naoImage = showNaoImage(IP, PORT)