import DataCollectionModule as dcM
import MotorModule as mM
#import WebcamModule as wM
import time

import tty, sys, termios
import threading
from picamera2 import Picamera2, Preview
import cv2
filedescriptors = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)


picam = Picamera2()

config = picam.create_preview_configuration()
picam.configure(config)
picam.start()

record = 0

motor = mM.Motor(8, 7, 4, 2, 3, 9, 0.45, 0.65, 0.3)


def capImage():
    img = picam.capture_array()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    size=[256, 128]
    img = cv2.resize(img,(size[0],size[1]))
    return img

def read_input():
    print('start')
    global record
    while True:
        x = sys.stdin.read(1)
        if x == 'w':
            motor.forward()
        if x == 's':
            motor.backward()
        if x == 'a':
            motor.left()
        if x == 'd':
            motor.right()
        if x == ' ': 
            motor.stop()
        
        if x == 'c':
            record = 1
        
        if x == 'x':
            record = 0
        
        if x == 'l':
            record = 2
            break
        
        
        time.sleep(0.05)
        motor.stop()
        time.sleep(1)
        img = capImage()
        dcM.saveData(img)

read_input()
#input_thread = threading.Thread(target=read_input)
#input_thread.daemon = True 
#input_thread.start()

#while True:
 #   if record == 1:
  #      img = capImage()
   #     dcM.saveData(img)
    #if record == 2:
     #   break

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, filedescriptors)
picam.close()
