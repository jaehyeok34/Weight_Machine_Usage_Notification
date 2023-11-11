class Repository:
    def __init__(
            self,
            id          :   int     =   None,
            sensor      :   str     =   None,
            signal      :   bool    =   None,
            value       :   float   =   None,
            saveTime    :   str =   None,
    ) -> None:
        self.id         =   id
        self.sensor     =   sensor
        self.signal     =   signal 
        self.value      =   value
        self.saveTime   =   saveTime