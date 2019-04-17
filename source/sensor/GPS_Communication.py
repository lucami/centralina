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

class GPS_Dummy_NMEA(GPS_Communication):
    def __init__(self):
        print ("DUMMY NMEA Generator built!")
        rmc_sentence = "$GPRMC,123519,A,4807.038,N,01131.000,E,022.4,084.4,230394,003.1,W*6A"
        gga_sentence"$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47"
        sentence=rmc_sentence
        pass

    def poll(self):
        if "RMC" in sentence:
            sentence = gga_sentence
        else
            sentence = rms_sentence
    
    def get(self):
        return nmea

class GPS_Dummy_JSON(GPS_Communication):
    def __init__(self):
        pass

    def poll(self):
        pass
    
    def get(self):
        pass
