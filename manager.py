import sys

from PyQt5.QtWidgets        import QApplication
from display.window_widget  import WindowWidget
from display.display_args   import DisplayArgs
from display.display_info   import DisplayInfo

class Manager:
    def __init__(self, displayArgs: DisplayArgs) -> None:
        self.__machines: list[DisplayInfo] = [
            DisplayInfo(id=3, name="벤치프레스", status=DisplayInfo.Status.USE),
            DisplayInfo(id=2, name="랫풀다운", status=DisplayInfo.Status.END),
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

    def showDisplay(self) -> None:
        if self.__display is not None:
            self.__display.showMaximized()
            sys.exit(self.__app.exec_())

    def createMachine(self, machine: DisplayInfo) -> None:
        # TODO: Exercise 객체 생성 루틴...
        self.__machines.append(machine)