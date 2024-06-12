import pyfirmata

board = pyfirmata.Arduino("/dev/ttyACM0")

class Motor:
    def __init__(self, motor1 = 8 , motor2 = 7, motor3 =4 , motor4=2, enLeft  =9, enRight = 3, speed =0.3, hight_speed = 0.5, low_speed = 0.2):
        self.motor1 = board.digital[motor1]
        self.motor2 = board.digital[motor2]
        self.motor3 = board.digital[motor3]
        self.motor4 = board.digital[motor4]
        self.pinLeft = board.get_pin(f'd:{enLeft}:p')
        self.pinRight = board.get_pin(f'd:{enRight}:p')
        self.speed = speed
        self.hight_speed = hight_speed
        self.low_speed = low_speed
    
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
        self.pinLeft.write(self.low_speed)
        self.pinRight.write(self.hight_speed)
        #self.motor1.write(0)
        #self.motor2.write(1)
        #self.motor3.write(0)
        #self.motor4.write(1)
        self.motor1.write(1)
        self.motor2.write(0)
        self.motor3.write(0)
        self.motor4.write(1)
        print('Rẻ trái')

    def right(self):
        self.pinLeft.write(self.hight_speed)
        self.pinRight.write(self.low_speed)
        self.motor1.write(1)
        self.motor2.write(0)
        self.motor3.write(0)
        self.motor4.write(1)
        print('Rẻ phải')

    def stop(self):
        speed = 0
        self.pinLeft.write(speed)
        self.pinRight.write(speed)
        print('Dừng')
