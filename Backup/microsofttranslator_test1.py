
from microsofttranslator import Translator
import socket
#socket.getaddrinfo( '127.0.0.1', 8080)

myClientID='9dd2a959-517e-45fb-94be-a60d6597d2d7'
#myClientSecretValue='DPm8Q~TynrF0z_EqI5JXEhhzmK9T~ivNqLFpOcJ.'

myClientSecretValue="DPm8Q~TynrF0z_EqI5JXEhhzmK9T~ivNqLFpOcJ"
translator = Translator(myClientID,myClientSecretValue)
print(translator.translate("Hello", "en"))