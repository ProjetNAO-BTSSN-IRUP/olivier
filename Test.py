from naoqi import ALProxy
tts = ALProxy("ALTextToSpeech", "192.168.1.43", 9559)
tts.say("Bonjour")