import urllib
import requests

def read_data_thingspeak():
    URL = 'https://api.thingspeak.com/channels/1151557/fields/1.json?api_key='
    KEY = 'BFSHI8WP49X27LW1'
    HEADER = '&results=2'
    NEW_URL = URL+KEY+HEADER
    print(NEW_URL)

    get_data = requests.get(NEW_URL).json()
    #print(get_data)
    channel_id = get_data['channel']['id']

    field_1 = get_data['feeds']
    #print(field_1)

    t = []
    for x in field_1:
        print(x['field1'])
        t.append(x['field1'])

read_data_thingspeak()