#!/usr/bin/env python

import socket
import cv2
import numpy as np
import time
import predict as predict
# from WebcamModule import capImage
import utils_car
import cv2
import numpy as np 
import threading
from object_detection import object_detect, face_detect

mode_face_detect = False

TCP_IP = '192.168.1.12'
TCP_PORT = 5010
BUFFER_SIZE = 1024

semaphore = threading.Semaphore(0)
angle = None
area_object_detect = None

tang_toc = False
def pred_angle(img):
    global angle
    img_pred = predict.get_output(imgs= [[img, img]])
    img_arr_pred = np.array(img_pred)
    #angle = utils_car.detect_lane_direction(img_arr_pred)
    angle = utils_car.get_decision(img_arr_pred)
    semaphore.release()

def pred_object(img):
    global area_object_detect
    area_object_detect = object_detect(img)
    semaphore.release()


def receive_image(conn):
    global angle
    global area_object_detect

    image_size = int.from_bytes(conn.recv(4), 'big')

    received_data = b''
    while len(received_data) < image_size:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        received_data += data

    nparr = np.frombuffer(received_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    thread1 = threading.Thread(target=pred_angle, args=(img,))
    thread2 = threading.Thread(target=pred_object, args=(img,))

    thread1.start()
    thread2.start()

    semaphore.acquire()
    semaphore.acquire()

    if area_object_detect is not None:
        print('object detect:', area_object_detect)
        if area_object_detect[0] == 'stop' and area_object_detect[1] >= 0.4:
            conn.send(b'stop')
            return
        if area_object_detect[0] == 'parking' and area_object_detect[1] >= 1.2:
            conn.send(b'parking')
            return
        if area_object_detect[0] == 'speed40' and area_object_detect[1] >= 0.4:
            conn.send(b'speed40')

        if area_object_detect[0] == 'speed60' and area_object_detect[1] >= 0.4:
            conn.send(b'speed60')


    if angle is None:
        conn.send(b'keep-cap')
        return

    if(angle >= -10 and angle <= 10):
        angle = 0
    

    angle_bytes = str(angle).encode('utf-8')

    msg = angle_bytes
    # Send a response back to the client
    conn.send(msg)

def receive_face_image(conn):
    print('Nhan')
    # Receive the size of the image first
    image_size = int.from_bytes(conn.recv(4), 'big')

    # Receive the image data
    received_data = b''
    while len(received_data) < image_size:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        received_data += data

    nparr = np.frombuffer(received_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    angle = face_detect(img)
    if angle is None:
        conn.send(b'keep-cap')
        return

    if(angle >= -10 and angle <= 10):
        angle = 0

    angle_bytes = str(angle).encode('utf-8')

    msg = angle_bytes
    # Send a response back to the client
    conn.send(msg)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set the SO_REUSEADDR option to reuse the port if it's in TIME_WAIT state
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((TCP_IP, TCP_PORT))
    s.listen(5)

    print("Server listening on {}:{}".format(TCP_IP, TCP_PORT))

    if not mode_face_detect:
        while True:
            conn, addr = s.accept()
            print('Connection address:', addr)
            receive_image(conn)
            conn.close()
    else:
        while True:
            conn, addr = s.accept()
            print('Connection address:', addr)
            receive_face_image(conn)
            conn.close()

if __name__ == "__main__":
    main()
