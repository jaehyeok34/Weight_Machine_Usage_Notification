import RPi.GPIO as GPIO
import time
from threading import Thread

# 클래스로 기구를 정의
class ExerciseEquipment:
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

        # Thread 객체 생성
        self.__switch   =   Thread(target = self.switch_interrupt)
        self.__segment  =   Thread(target = self.start_segment) 

        self.isRun      =   True    # 전체 프로그램이 실행 중인지 확인
        self.isUse      =   False   # 기구 사용 중인지 확인
        self.start_time =   None

        # pin 설정
        self.initialize_pins()


    def initialize_pins(self):
        GPIO.setup(self.ir_sensor_pin, GPIO.IN)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.setup(self.switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.output(self.led_pin, False)

        for segment in self.segments:
            GPIO.setup(segment, GPIO.OUT)
            GPIO.output(segment, False)

        for digit in self.digits:
            GPIO.setup(digit, GPIO.OUT)
            GPIO.output(digit, True)
    
    def initialize_segments(self):
        for segment in self.segments:
            GPIO.setup(segment, GPIO.OUT)
            GPIO.output(segment, False)

    def stop_sensor(self):
        self.isRun = False
        GPIO.output(self.led_pin, False)
        print("Exercise Equipment: Sensor stopped")


    def get_pulse_duration(self):
        pulse_start = 0
        pulse_end = 0

        GPIO.output(self.trig_pin, False)
        time.sleep(0.5)
        GPIO.output(self.trig_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, False)

        while GPIO.input(self.echo_pin) == 0:
            pulse_start = time.time()

        while GPIO.input(self.echo_pin) == 1:
            pulse_end = time.time()

        return pulse_end - pulse_start

    def switch_interrupt(self):
        while self.isRun:
            if GPIO.input(self.switch_pin) == 0:
                print("스위치 눌림 - 초기화")
                self.stop_sensor()  # 센서 정지
                self.initialize_segments()  # 세그먼트 초기화
                self.initialize_pins()  # 핀 초기화

    def print_number(self, number):
        delay = 0.00001  # 1ms
        values = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]

        # digit 설정
        for i, digit in enumerate(values):
            for j in range(len(DIGITS)):
                if j == i:
                    GPIO.output(self.digits[j], False)
                else:
                    GPIO.output(self.digits[j], True)

            # segment 설정
            for pin in range(len(self.segments)):
                if pin in NUMBERS[digit]:
                    GPIO.output(self.segments[pin], True)
                else:
                     GPIO.output(self.segments[pin], False)

            time.sleep(delay)

    def start_segment(self):
        sec = 1
        while self.isUse:
            self.print_number(sec)
            sec += 1
            time.sleep(1)

    def run(self):
        self.__switch.start()       # switch_interrupt
        self.__segment.start()      # start_segment

        while self.isRun:
            # TODO: 적외선 센싱 추가
            infrared = True     # 적외선 센싱이 완료됐다 가정하는 변수(적외선 센싱 추가 하면 변경 지우셈)
            
            if infrared:
                start_sensing = time.time()
                keep_time = 3
                ul_sensor = True

                # n초 동안 센서가 유지 됐는지 확인
                while (time.time() - start_sensing) < keep_time:
                    pulse_duration = self.get_pulse_duration()
                    distance = pulse_duration * 34300 / 2

                    # n초가 지나기 전에, 멀어지면(거리 값 일정치 이상보다 증가) 센싱 실패
                    if distance > 30:       
                        ul_sensor = False
                        break

                    time.sleep(0.1)

                # 초음파 센싱 성공(기구에 사람이 있음)
                if ul_sensor:
                    self.start_time = time.time()
                    self.isUse = True               # segment 활성화
                    # TODO: 기구 사용 중이면 해야 할것들(LED 키기 등) 추가


            # TODO: 기구 사용 종료를 판단하고, 그에따른 종료 루틴 수행
            time.sleep(0.5)


if __name__ == "__main__":
    # GPIO 핀 설정
    IR_SENSOR_PIN = 5
    TRIG_PIN = 21
    ECHO_PIN = 20
    LED_PIN = 6
    SWITCH_PIN = 17

    SEGMENTS = (23, 16, 13, 22, 27, 24, 19)
    DIGITS = (18, 25, 12, 26)

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

    # GPIO 초기화 및 기구 초기화
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)  # 경고 비활성화

    # 객체 생성
    exercise_equipment = ExerciseEquipment(
        # info
        "bench", 0,

        # pin
        IR_SENSOR_PIN, TRIG_PIN, ECHO_PIN, LED_PIN, SWITCH_PIN, SEGMENTS, DIGITS
    )

    exercise_equipment.run()

    # GPIO 정리
    GPIO.cleanup()


