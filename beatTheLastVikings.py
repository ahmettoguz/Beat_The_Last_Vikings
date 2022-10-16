import pyautogui
import keyboard
import time
pyautogui.PAUSE = 0


# def clickLevelNode():
#     pyautogui.mouseDown(185, 150, button='left')
#     pyautogui.moveTo(185, 900, 0.5)
#     pyautogui.mouseUp(185, 900, button='left')
#     pyautogui.moveTo(1350, 500, 1)
#     pyautogui.click()

def clickLevelNode():
    # pyautogui.moveTo(1500, 450, 0.5)
    pyautogui.moveTo(400, 400, 0.5)
    pyautogui.click()


def isClockPast():
    # detect if hour is 20 so that we cannot increase time we will increase day
    sc = pyautogui.screenshot()

    # print(sc.getpixel((851, 780))[0])
    # print(sc.getpixel((878, 765))[0])

    # check for 2
    if sc.getpixel((851, 780))[0] <= 75 and sc.getpixel((851, 780))[0] >= 70:
        return True
    return False


def haveEnergy():
    sc = pyautogui.screenshot()
    # print(sc.getpixel((446, 926))[0])
    # if sc.getpixel((446, 926))[0] <= 231 and sc.getpixel((446, 926))[0] >= 227:
    if sc.getpixel((446, 926))[0] >= 60:
        return False
    return True


def startProgramWithKey():
    print("Press F8 to start program")
    keyboard.wait('F8')
    time.sleep(1)


def moveToApplicaiton():
    # click application
    pyautogui.moveTo(900, 10, 0.5)
    pyautogui.click()


def openRaidPage():
    # click raid
    pyautogui.moveTo(1686, 935, 0.5, pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.moveTo(1800, 200, 0.5, pyautogui.easeInOutQuad)
    pyautogui.click()


def startAdventure():
    global j, serverError

    # click solo adventure
    time.sleep(1)
    pyautogui.moveTo(1000, 200, 0.5, pyautogui.easeInOutQuad)
    pyautogui.click()

    # click level node
    time.sleep(1)
    clickLevelNode()

    # check for energy
    time.sleep(1.5)
    if haveEnergy():
        print("Game number:", j)
        j += 1
        serverError = 0

        # click start button
        pyautogui.moveTo(600, 900, 0.5, pyautogui.easeInOutQuad)
        pyautogui.click()

        # click place
        pyautogui.moveTo(1150, 300, 1.2, pyautogui.easeInOutQuad)
        pyautogui.click()

        # after battle start collect reward
        pyautogui.moveTo(1686, 935, 5, pyautogui.easeInOutQuad)
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(0.3)
        pyautogui.click()

        # return main page
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()

        # click boat
        pyautogui.moveTo(1504, 939, 0.5, pyautogui.easeInOutQuad)
        pyautogui.click()

        # click space to skip conversation
        pyautogui.moveTo(1504, 200, 0.5, pyautogui.easeInOutQuad)
        pyautogui.click()
    else:
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(0.5)
        pyautogui.click(button='right')
        time.sleep(0.5)
        print("do not have energy. Will go to date settings")
        serverError += 1

        # check server error
        if serverError == 3:
            print("Server Error !")
            print("Program terminated.")
            exit()

        # go home
        pyautogui.click(button='middle')
        time.sleep(2)

        # open settings
        pyautogui.moveTo(985, 50, 0.2)
        time.sleep(0.5)
        pyautogui.mouseDown(985, 50, button="left")
        time.sleep(0.5)
        pyautogui.moveTo(985, 600, 0.5, pyautogui.easeInOutQuad)
        pyautogui.mouseUp(985, 600, button="left")
        pyautogui.moveTo(1170, 550, 0.2, pyautogui.easeInOutQuad)
        pyautogui.moveTo(1170, 50, 0.5, pyautogui.easeInOutQuad)
        pyautogui.click()

        # open date settings
        time.sleep(2)
        pyautogui.moveTo(1170, 1000, 0.2)
        pyautogui.mouseDown(1170, 1000, button="left")
        pyautogui.moveTo(1170, 100, 0.5, pyautogui.easeInOutQuad)
        pyautogui.mouseUp(1170, 100, button="left")
        pyautogui.moveTo(1170, 550, 0.5, pyautogui.easeInOutQuad)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(1170, 300, 0.5, pyautogui.easeInOutQuad)
        pyautogui.click()

        # check if date is auto
        time.sleep(1)
        if pyautogui.pixel(1175, 240)[0] == 249:
            print("Switching to manuel date.")
            pyautogui.moveTo(1175, 240, 0.5)
            pyautogui.click()

        # click hour
        pyautogui.moveTo(1175, 500, 0.5)
        pyautogui.click()

        # check hour
        time.sleep(2.5)
        if isClockPast():
            # take hour to 00.00

            # click hour
            pyautogui.moveTo(870, 770, 1, pyautogui.easeInOutQuad)
            pyautogui.click()

            # click 0 and ok
            pyautogui.moveTo(960, 950, 1.5, pyautogui.easeInOutQuad)
            pyautogui.click()

            pyautogui.moveTo(1130, 955, 0.5, pyautogui.easeInOutQuad)
            pyautogui.click()

            # click 0 and ok
            pyautogui.moveTo(960, 950, 0.5, pyautogui.easeInOutQuad)
            pyautogui.click()
            pyautogui.moveTo(1130, 955, 0.5, pyautogui.easeInOutQuad)
            pyautogui.click()

            # ok again
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(2)

            # click date
            pyautogui.moveTo(1175, 370, 1.5, pyautogui.easeInOutQuad)
            pyautogui.click()
            pyautogui.moveTo(950, 530, 1.5, pyautogui.easeInOutQuad)
            pyautogui.click()

            # increment day bay 1
            pyautogui.moveTo(775, 740, 0.5, pyautogui.easeInOutQuad)
            pyautogui.mouseDown(775, 740, button="left")
            pyautogui.moveTo(775, 660, 0.4)
            pyautogui.mouseUp(775, 660, button="left")

            # click ok
            pyautogui.moveTo(1150, 965, 2, pyautogui.easeInOutQuad)
            pyautogui.click()
            time.sleep(2)

        else:
            # change hour by 3 max is 4
            hourChange = 3
            pyautogui.moveTo(870, 770, 0.5)
            pyautogui.mouseDown(870, 770, button="left")
            pyautogui.moveTo(870, 770 - hourChange * 60,
                             0.5, pyautogui.easeInOutQuad)
            pyautogui.mouseUp(870, 770 - hourChange * 60, button="left")

            # click ok
            time.sleep(1)
            pyautogui.moveTo(1150, 965, 0.5, pyautogui.easeInOutQuad)
            pyautogui.click()

        # # return game
        time.sleep(0.5)
        pyautogui.click(button='middle')
        time.sleep(1)
        pyautogui.moveTo(1230, 500, 0.2, pyautogui.easeInOutQuad)
        time.sleep(0.3)
        pyautogui.mouseDown(1230, 500, button="left")
        time.sleep(0.5)
        pyautogui.moveTo(700, 500, 0.5)
        pyautogui.mouseUp(700, 500, button="left")
        pyautogui.moveTo(1160, 300, 0.5)
        pyautogui.click()


# main
startProgramWithKey()
moveToApplicaiton()
# openRaidPage()

serverError = 0
j = 1
# main loop
while True:
    startAdventure()


print("Stopped")
