from GPS_Factory import *

sys.path.insert(0,'../')
from kick import *

class GPS_Facade(kicker):

	def __init__(self, gps_type):

		self.g=GPSFactory(gps_type)

		self.gps_device = self.g.build_gps()
		self.parser,self.rmc_parser, self.gga_parser=self.g.build_parser()
		self.latitude = self.g.build_latitude()
		self.longitude = self.g.build_longitude()   
		self.time = self.g.build_time()
		self.date = self.g.build_date()
		self.q = self.g.build_quality()

		self.gps_device.register(self.parser, self.parser.parse)

		self.parser.register(self.rmc_parser, self.rmc_parser.parse_rmc)
		self.parser.register(self.gga_parser, self.gga_parser.parse_gga)

		self.rmc_parser.register(self.latitude, self.latitude.set)
		self.rmc_parser.register(self.longitude, self.longitude.set)
		self.rmc_parser.register(self.time, self.time.set)
		self.rmc_parser.register(self.date, self.date.set)
		self.rmc_parser.register(self.q, self.q.set)

	def kick(self):
		self.gps_device.execute()

	def get_position(self):
		return self.latitude.get() + ";" + self.longitude.get()
	def get_time_date(self):
		return self.time.get()+ ";" + self.date.get()
	def get_validity(self):
		return self.q.get()
