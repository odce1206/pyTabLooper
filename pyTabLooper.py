import time
import webbrowser
import ConfigParser
from pykeyboard import PyKeyboard

validador = 1
intervalos = 5
kInput = PyKeyboard()

while validador == True:
	# Link 1
	webbrowser.open("www.google.com")
	time.sleep(1)
	kInput.press_key(kInput.control_key)
	kInput.tap_key(kInput.tab_key)
	kInput.release_key(kInput.control_key)
	time.sleep(.1)
	kInput.press_key(kInput.control_key)
	kInput.tap_key('w')
	kInput.release_key(kInput.control_key)
	time.sleep(5)
	# Link 2
	webbrowser.open("www.reddit.com")
	time.sleep(1)
	kInput.press_key(kInput.control_key)
	kInput.tap_key(kInput.tab_key)
	kInput.release_key(kInput.control_key)
	time.sleep(.1)
	kInput.press_key(kInput.control_key)
	kInput.tap_key('w')
	kInput.release_key(kInput.control_key)
	time.sleep(5)
	# Link 3
	webbrowser.open("www.yahoo.com")
	time.sleep(1)
	kInput.press_key(kInput.control_key)
	kInput.tap_key(kInput.tab_key)
	kInput.release_key(kInput.control_key)
	time.sleep(.1)
	kInput.press_key(kInput.control_key)
	kInput.tap_key('w')
	kInput.release_key(kInput.control_key)
	time.sleep(5)
