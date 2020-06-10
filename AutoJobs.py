import ctypes
import time

SendInput = ctypes.windll.user32.SendInput


W = 0x11
A = 0x1E
S = 0x1F
D = 0x20

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

if __name__ == '__main__':
    PressKey(0x11)
    time.sleep(1)
    ReleaseKey(0x11)
    time.sleep(1)


import pyautogui,time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True           # 启用自动防故障功能
print(pyautogui.size())
width,height = pyautogui.size()     # 屏幕的宽度和高度
pyautogui.position()
index = 0
round = 0
try:
    while True:

        location_GS = pyautogui.locateCenterOnScreen('GS.png')

        if str(location_GS) == 'None':
            #print(location_GS)
            location_replay = pyautogui.locateCenterOnScreen('replay1.png')
            if str(location_replay) == 'None':
                location_replay = pyautogui.locateCenterOnScreen('rm1.png')
            if str(location_replay) == 'None':
                location_replay = pyautogui.locateCenterOnScreen('rm.png')
            if str(location_replay) == 'None':
                location_replay = pyautogui.locateCenterOnScreen('r3.png')
            if str(location_replay) == 'None':
                location_replay = pyautogui.locateCenterOnScreen('r4.png')

            if str(location_replay) != 'None':
                print("location_replay:" + str(location_replay))
                # pyautogui.moveTo(location)
                # pyautogui.click()
                pyautogui.click(location_replay)
                #time.sleep(0.33)
                pyautogui.drag(-29, 0, 0.17, button='left')
                pyautogui.drag(21, 0, 0.23, button='left')

        location = pyautogui.locateCenterOnScreen('c.png')
        #print(location)
        if str(location) == 'None':
            location = pyautogui.locateCenterOnScreen('cm1.png')
            #print(location)
        if str(location) == 'None':
            location = pyautogui.locateCenterOnScreen('c2.png')
            #print(location)
        if str(location) != 'None':
            print("location:" + str(location))
            #pyautogui.moveTo(location)
            #pyautogui.click()
            pyautogui.click(location)
            #time.sleep(0.33)
            pyautogui.drag(40, 0, 0.2, button='left')
            pyautogui.drag(-37, 0, 0.3, button='left')

        location_s = pyautogui.locateCenterOnScreen('s.png')
        if str(location_s) == 'None':
            location_s = pyautogui.locateCenterOnScreen('sm1.png')

        if str(location_s) != 'None':
            print("location_s:" + str(location_s))
            pyautogui.click(location_s)
            pyautogui.drag(20, 0, 0.29, button='left')
            pyautogui.drag(-17, 0, 0.21, button='left')
            time.sleep(0.9)
            #print("0x1C")
            PressKey(0x1C)
            time.sleep(0.31)
            ReleaseKey(0x1C)
            print("ReleaseKey into the job")
            round = round +1


        #time.sleep(0.1)
        PressKey(0x3A)
        time.sleep(0.13)
        ReleaseKey(0x3A)
        print("Index:" + str(index) + "    Round:" + str(round))
        #pyautogui.drag(1, 0, 0.2, button='left')
        #pyautogui.click()
        #time.sleep(0.5)
        #ReleaseKey(0x13)
        index = index + 1

except KeyboardInterrupt:                              # 处理 Ctrl-C 按键
    print('\nDone.')
