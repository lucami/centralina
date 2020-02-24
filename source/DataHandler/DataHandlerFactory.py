import os
from DataHandler.DataHandler import *

class DataHandler_Factory():
    def __init__(self):
        self.data_handler = Data_Handler()

    def get_data_handler(self):
        return self.data_handler
