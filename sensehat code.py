import math
import time
from sense_hat import SenseHat

sense = SenseHat()

def get_data():

    h = []
        t = []
            d = []
    start = time.time()
        while time.time() - start < .8:
                hum = sense.get_humidity()
                        temp = sense.get_temperature()
                                h.append(hum)
                                        t.append(temp)
                                                d.append(243.04 * (math.log(round(hum,1) / 100) + ((17.625 * round(temp, 1)) / (243.04 + round(temp, 1)))) / (17.625 - math.log(round(hum, 1) / 100)- (17.625 * round(temp, 1)) / (243.04 + round(temp, 1))))
    sensor_vals = [h, t, d]
        avg_list = [round(sum(each)/len(each),1) for each in sensor_vals]
            return avg_list
