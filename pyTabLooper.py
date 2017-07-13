import time
import webbrowser
import configparser
from pykeyboard import PyKeyboard

validador = 1
intervalos = 5
kInput = PyKeyboard()

config = configparser.ConfigParser()
config.read('config.ini')

dictURL = {}
for secciones in config.sections():
    dictURL[secciones] = {}
    for opcion in config.options(secciones):
        dictURL[secciones][opcion] = config.get(secciones,opcion)

# crear lista de urls
for k, v  in dictURL.items():
    dictLinks = list(dictURL[k].keys())

# Crear lista de minutos
for k, v in dictURL.items():
    listNum = list(map(float, dictURL[k].values()))

for contador in range(len(dictLinks)):
    urlOpen = dictLinks[contador]
    time.sleep(.05)
    webbrowser.open(urlOpen)

time.sleep(.3)
kInput.press_key(kInput.control_key)
kInput.tap_key('1')
kInput.release_key(kInput.control_key)
time.sleep(.3)
kInput.press_key(kInput.control_key)
kInput.tap_key('w')
kInput.release_key(kInput.control_key)
time.sleep(.1)

while validador == True:
    for i in range(len(listNum)):
        tiempo = listNum[i] * 60
        time.sleep(tiempo)
        kInput.press_key(kInput.control_key)
        kInput.tap_key(kInput.tab_key)
        kInput.release_key(kInput.control_key)
