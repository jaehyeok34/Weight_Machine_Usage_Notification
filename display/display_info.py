class DisplayInfo:
    class Status:
        USE     =   0
        PAUSE   =   1
        END     =   2
    
    def __init__(
        self,
        machineName: str,
        status: "DisplayInfo.Status",
    ) -> None:
        self.machineName    =   machineName
        self.status         =   status