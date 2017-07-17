import time
import webbrowser
import ConfigParser
import sys
from pykeyboard import PyKeyboard

validador = 1
intervalos = 5
kInput = PyKeyboard()

config = ConfigParser.RawConfigParser()
config.read('config.ini')

dictURL = {}
for secciones in config.sections():
    dictURL[secciones] = {}
    for opcion in config.options(secciones):
        dictURL[secciones][opcion] = config.get(secciones,opcion)

# crear lista de urls
dictLinks = []
for k, v  in dictURL.iteritems():
    dictLinks = list(dictURL[k].keys())

# Crear lista de minutos
listNum = []
for k, v in dictURL.iteritems():
    listNum = list(map(float, dictURL[k].values()))

for contador in range(len(dictLinks)):
    urlOpen = dictLinks[contador]
    prefixx = "http://"
    urlFixed = prefixx+urlOpen
    time.sleep(.05)
    webbrowser.open_new(urlFixed)

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
