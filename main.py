import sys, os
import RPi.GPIO as GPIO

from manager                import Manager
from display.display_args   import DisplayArgs
from display.display_info   import DisplayInfo
from machine                import Machine

def main() -> None:
    sys.path.append(os.path.abspath(os.getcwd()))
    IR_SENSOR_PIN = 5;  TRIG_PIN = 21
    ECHO_PIN = 20;      LED_PIN = 6
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
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)  # 경고 비활성화

    manager = Manager(
        displayArgs = DisplayArgs(
            winsize     =   (100, 100, 400, 400),
            title       =   "machine usage notification",
            winbackColor=   "black",
            updateTime  =   3000,
            text        =   "Hello",
            textColor   =   "white",
            fontSize    =   80,
            radius      =   30,
        )
    )
    thread = manager.appendMachine(
        Machine(
            name = "벤치프레스", id = 0,
            ir_sensor_pin   =   IR_SENSOR_PIN,
            trig_pin        =   TRIG_PIN,
            echo_pin        =   ECHO_PIN,
            led_pin         =   LED_PIN,
            switch_pin      =   SWITCH_PIN,
            segments        =   SEGMENTS,
            digits          =   DIGITS
        )
    )
    threads = []
    threads.append(thread)

    manager.showDisplay(True)
    GPIO.cleanup()


if __name__ == "__main__":
    main()