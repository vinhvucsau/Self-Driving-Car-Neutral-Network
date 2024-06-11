import socket
import cv2
import numpy as np
import config

TCP_IP = config.TCP_IP_SERVER
TCP_PORT = config.PORT_SERVER
BUFFER_SIZE = 1024

def capture_image():
    start_time = time.time()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device.")
        return None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Error: Could not read frame.")
        return None

    end_time = time.time()
    print('Thoi gian chup anh', str(end_time - start_time))
    # Encode the frame in JPEG format

    start_time = time.time()
    _, encoded_image = cv2.imencode('.jpg', frame)
    end_time = time.time()

    print('Thoi gian encode: ', str(end_time - start_time))
    return encoded_image.tobytes()

def send_image(image_data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    # Send the size of the image first
    image_size = len(image_data)
    s.sendall(image_size.to_bytes(4, 'big'))

    # Send the image data
    s.sendall(image_data)

    # Receive the response from the server
    response = s.recv(BUFFER_SIZE)
    print("Received response:", response)

    s.close()

    return response


def main():
    while True:
        user_input = input("Press Enter to capture and send image, or type 'quit' to exit: ")
        if user_input.lower() == 'quit':
            break
        image_data = capture_image()
        if image_data is not None:
            send_image(image_data)

if __name__ == "__main__":
    main()
