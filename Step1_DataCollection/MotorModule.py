import pyfirmata

board = pyfirmata.Arduino("/dev/ttyACM0")

class Motor:
    def __init__(self, motor1, motor2, motor3, motor4, enLeft, enRight, speed, speed_left_right):
        self.motor1 = board.digital[motor1]
        self.motor2 = board.digital[motor2]
        self.motor3 = board.digital[motor3]
        self.motor4 = board.digital[motor4]
        self.pinLeft = board.get_pin(f'd:{enLeft}:p')
        self.pinRight = board.get_pin(f'd:{enRight}:p')
        self.speed = speed
        self.speed_left_right = speed_left_right
    
    def forward(self):
        speed = self.speed
        self.pinLeft.write(speed)
        self.pinRight.write(speed)
        self.motor1.write(1)
        self.motor2.write(0)
        self.motor3.write(0)
        self.motor4.write(1)
        print('Chạy thẳng')

    def backward(self):
        speed = self.speed
        self.pinLeft.write(speed)
        self.pinRight.write(speed)
        self.motor1.write(0)
        self.motor2.write(1)
        self.motor3.write(1)
        self.motor4.write(0)
        print('Chạy lùi')

    def left(self):
        speed_left_right = self.speed_left_right
        self.pinLeft.write(speed_left_right)
        self.pinRight.write(speed_left_right)
        self.motor1.write(0)
        self.motor2.write(1)
        self.motor3.write(0)
        self.motor4.write(1)
        print('Rẻ trái')

    def right():
        speed_left_right = self.speed_left_right
        self.pinLeft.write(speed_left_right)
        self.pinRight.write(speed_left_right)
        self.motor1.write(1)
        self.motor2.write(0)
        self.motor3.write(1)
        self.motor4.write(0)
        print('Rẻ phải')

    def stop():
        self.motor1.write(0)
        self.motor2.write(0)
        self.motor3.write(0)
        self.motor4.write(0)
        print('Dừng')
