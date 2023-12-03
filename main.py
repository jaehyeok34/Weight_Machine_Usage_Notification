import sys, os

from manager                import Manager
from display.display_args   import DisplayArgs
from display.display_info   import DisplayInfo

from threading import Thread

def tmpInputData(manager: Manager) -> None:
    while True:
        id, name, status = input("input id, name, status(0 ~ 2): ").split(" ")
        manager.createMachine(DisplayInfo(int(id), name, int(status)))

def main() -> None:
    sys.path.append(os.path.abspath(os.getcwd()))

    manager = Manager(
        displayArgs = DisplayArgs(
            winsize     =   (100, 100, 400, 400),
            title       =   "machine usage notification",
            winbackColor=   "black",
            updateTime  =   3000,
            text        =   "Hello",
            textColor   =   "white",
            fontSize    =   30,
            radius      =   30,
        )
    )
    inputThread = Thread(target=tmpInputData, args=(manager,))
    inputThread.start()

    manager.showDisplay()

if __name__ == "__main__":
    main()