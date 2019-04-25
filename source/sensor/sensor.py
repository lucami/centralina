class Abstract_Sensor():
    def __init__(self):
        raise NotImplementedError

    def kick(self):
        raise NotImplementedError

class GPS_Sensor(Abstract_Sensor):
	def __init__(self)