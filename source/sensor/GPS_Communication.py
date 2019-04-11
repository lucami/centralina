class GPS_Communication():
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def poll(self):
        pass
    
    @abstractmethod
    def get(self):
        pass

class GPS_SPI(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass

class GPS_Serial(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass

class GPS_Daemon(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass

class GPS_Dummy(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass
