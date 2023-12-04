import RPi.GPIO as GPIO
import time
from threading import Thread
from multiprocessing import Process, Value
from numpy import mean

A = 0; B = 1; C = 2; D = 3
E = 4; F = 5; G = 6
D1 = 0; D2 = 1; D3 = 2; D4 = 3

NUMBERS = {
    0: (A, B, C, D, E, F),
    1: (B, C),   
    2: (A, B, D, E, G),
    3: (A, B, C, D, G),
    4: (B, C, F, G), 
    5: (A, C, D, F, G),
    6: (A, C, D, E, F, G),
    7: (A, B, C, F), 
    8: (A, B, C, D, E, F, G),
    9: (A, B, C, D, F, G)   
}

# 클래스로 기구를 정의
class Machine:
    class __STATUS:
        USE     =   0
        PAUSE   =   1
        END     =   2

    def __init__(
        self, 
        
        # for object
        name: str, id: int,
        
        # for pin
        ir_sensor_pin,  trig_pin,   echo_pin,   
        led_pin,        switch_pin, segments, 
        digits,
    ) -> None:
        # 객체 식별 변수 초기화
        self.name   =   name
        self.id     =   id

        # pin 변수 초기화
        self.ir_sensor_pin  =   ir_sensor_pin
        self.trig_pin       =   trig_pin
        self.echo_pin       =   echo_pin
        self.led_pin        =   led_pin
        self.switch_pin     =   switch_pin
        self.segments       =   segments
        self.digits         =   digits

        self.__status   =   Value("i", Machine.__STATUS.END)

        # Thread 객체 생성
        self.__switch   =   Process(target = self.switch_interrupt)
        self.__segment  =   Process(target = self.startSegment, args = (self.__status, )) 

        # pin 설정

        if self.ir_sensor_pin != 0:
            self.initPins()
            self.initSegment()

    def initPins(self):
        GPIO.setup(self.ir_sensor_pin, GPIO.IN)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.setup(self.switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.output(self.led_pin, False)

    def initSegment(self, mode: int = 0):
        for segment in self.segments:
            if mode == 0:
                GPIO.setup(segment, GPIO.OUT)
            GPIO.output(segment, False)

        for digit in self.digits:
            if mode == 0:
                GPIO.setup(digit, GPIO.OUT)
            GPIO.output(digit, True)

    def check_infrared_sensor(self) -> bool:
        return GPIO.input(self.ir_sensor_pin) == GPIO.HIGH
    
    def get_pulse_duration(self):
        START, END = 0, 1
        def getTime(pin: int, mode: int, timeout: int = 0):
            start = int(time.time())
            while GPIO.input(pin) == mode:
                if (int(time.time()) - start) > timeout:
                    return 0
                
            return time.time()

        pulse_start, pulse_end = 0, 0
        while True:
            GPIO.output(self.trig_pin, False)
            time.sleep(0.5)
            GPIO.output(self.trig_pin, True)
            time.sleep(0.00001)
            GPIO.output(self.trig_pin, False)

            pulse_start = getTime(self.echo_pin, START)
            pulse_end = getTime(self.echo_pin, END)

            if (pulse_start != 0) and (pulse_end != 0):
                break

        return pulse_end - pulse_start

    def getDistance(self):
        return self.get_pulse_duration() * 34300 / 2

    def switch_interrupt(self):
        while True:
            if (self.__status.value != Machine.__STATUS.END) and \
                (GPIO.input(self.switch_pin) == 0):
                print("Switch - Reset")
                self.__endRoutine()

    def printNumber(self, number):
        delay = 0.00001  # 1ms
        values = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]

        for i, digit in enumerate(values):
            for j in range(len(self.digits)):
                if j == i:
                    GPIO.output(self.digits[j], False)
                else:
                    GPIO.output(self.digits[j], True)

            for pin in range(len(self.segments)):
                if pin in NUMBERS[digit]:
                    GPIO.output(self.segments[pin], True)
                else:
                    GPIO.output(self.segments[pin], False)

            time.sleep(delay)

    def startSegment(self, status: Value):
        sec = 0
        def inclineSec():
            nonlocal sec
            while True:
                sec += 1
                time.sleep(1)
        
        thread = Thread(target=inclineSec)
        while True:
            if status.value != Machine.__STATUS.END:
                if not thread.is_alive():
                    thread.start()

                self.printNumber(sec)

    def __keep(self, startTime: int, keepTime: int, pivot: int):
        flag = True
        count = 0
        while (int(time.time()) - startTime) < keepTime:
            distance = self.getDistance()
            print(distance, "cm")

            if distance < pivot:
                count += 1

            if count > 5:
                flag = False
                break

        return flag
    
    def __endRoutine(self):
        GPIO.output(self.led_pin, False)
        self.initSegment(1)
        self.__status.value = Machine.__STATUS.END

    def __pauseRoutine(self):
        GPIO.output(self.led_pin, True)
        self.__status.value = Machine.__STATUS.PAUSE

    def __useRoutine(self):
        GPIO.output(self.led_pin, False)
        self.__status.value = Machine.__STATUS.USE


    def __useStatusRoutine(self, keepTime: int, pivot: int):
        if self.__keep(int(time.time()), keepTime, pivot):
            print("pause!!")
            self.__pauseRoutine()

    def __pauseStatusRoutine(self, keepTime:int, pivot: int):
        if self.__keep(int(time.time()), keepTime, pivot):
            print("end!!")
            self.__endRoutine()

        else:
            print("use!!")
            self.__useRoutine()

    def __endStatusRoutine(self, keepTime: int, pivot: int):
        distances = []
        if self.check_infrared_sensor():
            print("infrared detected")
            ulStart = int(time.time())

            while (int(time.time()) - ulStart) < keepTime:
                distance = self.getDistance()
                print(distance, "cm")
                distances.append(distance)
            
            if mean(distances) <= pivot:
                self.__useRoutine()

    def getStatus(self):
        return self.__status.value 

    def run(self):
        try:
            self.__switch.start()
            self.__segment.start()

            while True:
                if self.__status.value == Machine.__STATUS.USE:
                    print("use")
                    self.__useStatusRoutine(5, 8)

                elif self.__status.value == Machine.__STATUS.PAUSE:
                    print("pause")
                    self.__pauseStatusRoutine(7, 8)

                else:
                    self.__endStatusRoutine(3, 10)


        except KeyboardInterrupt:
            print("KeyboardInterrupt - Exiting")

            self.__switch.join()
            self.__segment.join()
            GPIO.cleanup()
