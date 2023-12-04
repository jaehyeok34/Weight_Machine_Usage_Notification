import sys
import RPi.GPIO as GPIO

from PyQt5.QtWidgets        import QApplication
from display.window_widget  import WindowWidget
from display.display_args   import DisplayArgs

from machine                import Machine
from threading              import Thread

class Manager:
    def __init__(self, displayArgs: DisplayArgs) -> None:
        self.__machines: list[Machine] = [
            Machine("랫풀다운", 1, 0, 0, 0, 0, 0, 0, 0),
            Machine("스미스머신", 2, 0, 0, 0, 0, 0, 0, 0)
        ]
        self.__app          = None
        self.__display      = None

        self.__initDisplay(displayArgs)

    def __initDisplay(self, displayArgs: DisplayArgs):
        self.__app      = QApplication([])
        self.__display  = WindowWidget(
            machines    = self.__machines,
            args        = displayArgs,
        )

    def showDisplay(self, fullScreen: bool = False) -> None:
        if self.__display is not None:
            if fullScreen:
                self.__display.showFullScreen()
            else:
                self.__display.showMaximized()
            sys.exit(self.__app.exec_())

    def appendMachine(self, machine: Machine) -> Thread:

        self.__machines.append(machine)
        thread = Thread(target  =   machine.run)
        thread.start()

        return thread
        