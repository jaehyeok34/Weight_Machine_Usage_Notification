class DisplayArgs:
    def __init__(
        self,
        # for window
        winsize: tuple, title: str, winbackColor: str, updateTime: int,

        # for text widget & text of status widget
        text: str, textColor: str, fontSize: int,

        # for status widget
        radius: int,
    ) -> None:
        self.winsize        = winsize
        self.title          = title
        self.winbackColor   = winbackColor
        self.updateTime     = updateTime
        self.text           = text
        self.textColor      = textColor
        self.fontSize       = fontSize
        self.radius         = radius