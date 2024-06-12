import DataCollectionModule as dcM
import MotorModule as mM
import WebcamModule as wM

import tty, sys, termios
import threading

filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)

x = 0

motor = mM.Motor(8, 7, 4, 2, 9, 3, 0.4, 0.5)

def read_input():
    while True:
        x = sys.stdin.read(1)
        if x == 'w':
            motor.forward()
        elif x == 's':
            motor.backward()
        elif x == 'a':
            motor.left()
        elif x == 'd':
            motor.right()
        elif x == ' ': 
            motor.stop()
        elif x == 27:
            break
        
        time.sleep(0.2)
        stop()
        time.sleep(1)
        img = wM.capImage()
        dcM.saveData(img)

read_input()

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)
wM.picam.close()