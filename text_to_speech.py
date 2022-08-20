# Program : text to speech
# Description : input a text output the speech
# Date : 20/08/22
# Author : Christophe Lagaillarde
# Version : 1.0
from sys import argv
import pyttsx3


def text_to_speech(*args):

    text: str = ''
    i: int = 0
    convert_to_speech: pyttsx3.engine.Engine = pyttsx3.init()
    convert_to_speech.setProperty('rate', 100)
    if len(args[0]) == 1:
        while True:
            text = str(input('Text: '))
            if text == 'stop':
                break
            convert_to_speech.say(text)
            convert_to_speech.runAndWait()

    else:
        for i in range(len(args[i])):
            if i != 0:
                text += ' ' + str(args[0][i])
        convert_to_speech.say(text)
        convert_to_speech.runAndWait()


if __name__ == '__main__':
    text_to_speech(argv)
