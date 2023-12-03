from PyQt5.QtGui            import QColor

class Palette:
    GRAY    =   QColor(128, 128, 128)
    RED     =   QColor(255, 0, 0)
    GREEN   =   QColor(0, 255, 0)
    BLUE    =   QColor(0, 0, 255)
    WHITE   =   QColor(255, 255, 255)
    BLACK   =   QColor(0, 0, 0)

    def getColor(color: str):
        return QColor(color)