from zOLD.Bosh.Bosh_Data import *
from zOLD.Bosh.Bosh_Facade import *
from zOLD.Bosh.Bosh_Parser import *


class BoshFactory:
    def __init__(self):
        self.parser = None
        self.fac = None
        self.bosh_queue()

    def get_parser(self):
        return self.parser

    def get_facade(self):
        return self.fac

    def bosh_queue(self):
        bosh_parser = Bosh_Parser()
        self.parser = bosh_parser

        bosh_adapter = Bosh_Data()
        bosh_parser.register(bosh_adapter, bosh_adapter.bosh_update)

        self.fac = Bosh_Facade()
        bosh_adapter.register(self.fac, self.fac.data_update)
