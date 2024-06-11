from picamera2 import Picamera2, Preview
import cv2
import MotorModule as mM
import client
import time


picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)
picam.start()

motor = mM.Motor(8, 7, 4, 2, 3, 9, 0.45, 0.65, 0.3)

def capImage():
    img = picam.capture_array()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    size=[256, 128]
    img = cv2.resize(img,(size[0],size[1]))
    _, encoded_image = cv2.imencode('.jpg', img)
    return encoded_image.tobytes()

if __name__ == "__main__":
    while True:
        img = capImage()
        resp = client.send_image(img)

        print(resp)
        # if resp == 'forward':
        #     motor.forward()
        #     time.sleep(config.time_sleep)
        
        # if resp == 'left':
        #     motor.left
        #     time.sleep(config.time_sleep)
        
        # if rasp == 'right':
        #     motor.right
        #     time.sleep(config.time_sleep)

        if rasp == 'stop':
            break

picam.close()