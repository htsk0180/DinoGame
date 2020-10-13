import pyautogui
from PIL import Image, ImageGrab
import time


# anlık olarak bilgisayar ekran görüntüsünü alıyoruz.
def screenshot():
    img = ImageGrab.grab().convert('L')
    return img


pyautogui.alert(text='Google DinoGame, oyunu otomatik olarak oynayacaktır.', title='www.google.com', button="HADİ BAŞLAYALIM");


def press(key):
    pyautogui.keyDown(key)
    return


def detect(data):
    for i in range(485, 525):
        for j in range(220, 260):
            if data[i, j] < 100:
                press('up')
                return


press('up')
time.sleep(2)
while True:
    img = screenshot()
    data = img.load()
    detect(data)