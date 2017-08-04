import time
import webbrowser
import ConfigParser
import yaml
import sys
from pykeyboard import PyKeyboard

validador = 1
intervalos = 5
kInput = PyKeyboard()

preConfig = open('links.yaml')
config = yaml.load(preConfig)
preConfig.close()

dictURL = {}
dictLinks = []
for k, v  in config.iteritems():
    dictLinks = config[k].keys()
time.sleep(.3)

# Crear lista de minutos
listNum = []
for k, v in config.iteritems():
    listNum = list(map(float, config[k].values()))

'''
for contador in range(len(dictLinks)):
    time.sleep(.05)
    urlOpen = dictLinks[contador]
    prefixx = "http://"
    urlFixed = prefixx+urlOpen
    time.sleep(.08)
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
'''

while validador == True:
    for i in range(len(listNum)):
        tiempo = listNum[i] * 60
        time.sleep(tiempo)
        kInput.press_key(kInput.control_key)
        kInput.tap_key(kInput.tab_key)
        kInput.release_key(kInput.control_key)