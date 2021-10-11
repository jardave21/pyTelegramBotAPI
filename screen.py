import pyscreenshot
from time import sleep
sleep(2)
im = pyscreenshot.grab()
sleep(2)
im.save("screenshot.png")