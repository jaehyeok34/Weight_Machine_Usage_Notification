class DisplayInfo:
    class Status:
        USE     =   0
        PAUSE   =   1
        END     =   2
    
    def __init__(
        self,
         id: int, name: str, status: "DisplayInfo.Status"
    ) -> None:
        self.id     = id
        self.name   = name
        self.status = status