from picamera2 import Picamera2, Preview
import cv2

picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)
picam.start()

def capImage():
    img = picam.capture_array()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    size=[256, 128]
    img = cv2.resize(img,(size[0],size[1]))
    return img
