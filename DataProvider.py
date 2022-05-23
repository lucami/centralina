from source.zOld2 import SensorGPS
from source.zOld2 import SensorHTP
from source.zOld2 import SensorPM
from time import sleep

if __name__ == "__main__":
    gps = SensorGPS("GPS", 1)
    pm = SensorPM("pm", 1)
    htp = SensorHTP("htp", 1)
    sensor_array = []

    sensor_array.append(gps)
    sensor_array.append(pm)
    sensor_array.append(htp)

    while True:
        for i in range(2):
            print("{} pollable: {} -> {}".format(sensor_array[i].get_name(), sensor_array[i].is_pollable(),
                                                 sensor_array[i].take_data()))
        sleep(1)
