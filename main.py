import pyautogui
from PIL import ImageGrab, ImageOps
from time import sleep
import numpy

sleep(2)

def StartGame():
    # Get the Dino moving
    pyautogui.press('space')
    sleep(0.10)
    # sleep(4)
    #
    # # Take a screenshot of the board
    # screenshot = pyautogui.screenshot('screenshot.png')

def GetSpaceInfrontOfDino():
    dinoposition = (311, 1157)
    # bottomlet, top y, far x, bottom y
    box = (
        310, 1106, 865, 1283
    )

    image = ImageGrab.grab(box)

    greyImage = ImageOps.grayscale(image)

    a = numpy.array(greyImage.getcolors())
    print(a.sum())
    return a.sum()

StartGame()
while True:
    if (GetSpaceInfrontOfDino()!=98490):
        # print('im here')
        pyautogui.press('space')
        sleep(0.1)
    # print('over here')




