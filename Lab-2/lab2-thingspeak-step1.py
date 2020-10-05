import time
import urllib.request
import gpiozero

WRITE_URL = "https://api.thingspeak.com/update?api_key="
WRITE_KEY = "ALSLSDLSDAODSO"

def getCpuTemperature():
    cpu = gpiozero.CPUTemperature();
    return cpu.temperature

def write_data_thingspeak():
    global WRITE_URL, WRITE_KEY
    # get cpu temperature then post that to thingspeak channel
    cpuTemperature = getCpuTemperature()
    temperatureHeader = "&field1={}".format(cpuTemperature)
    REQUEST_URL = WRITE_URL + WRITE_KEY + temperatureHeader
    print(REQUEST_URL)
    data = urllib.request.urlopen(REQUEST_URL)
    
if __name__ == "__main__":
    write_data_thingspeak()