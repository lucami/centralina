import sys
import argparse

def test_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--gps_log')
    parser.add_argument('-i', '--input')
    parser.add_argument('-v', dest='verbose', action='store_true')
    parser.add_argument('-s', '--suca')
    args = parser.parse_args()

    arg_dic=vars(args)
    print (arg_dic.get('verbose'))


class parser():
    def __init__(self):
    
        parser = argparse.ArgumentParser()
        parser.add_argument('-gps', '--gps')
        parser.add_argument('-v', dest='verbose', action='store_true')
        args = parser.parse_args()
        arg_dic=vars(args)
        self.nmea_arg=arg_dic.get('gps')
    def get_gps_arg(self):
        return self.nmea_arg

def test_gps_parser():
    p = parser()
    print(p.get_gps_arg())

#test_gps_parser()
