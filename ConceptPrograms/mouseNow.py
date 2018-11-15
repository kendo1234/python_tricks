#! python3

# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui

print('Press Ctrl-C to quit.')

try:
    while True:
        x, y = pyautogui.position() #gets starting position of mouse cursor
        # prints mouse movement in real time
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # prints colour under cursor in real time
        pixelColor = pyautogui.screenshot().getpixel((x, y))
        positionStr += ' RGB: (' + str(pixelColor[0]).rjust(3)
        positionStr += ', ' + str(pixelColor[1]).rjust(3)
        positionStr += ', ' + str(pixelColor[2]).rjust(3) + ')'
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone')

