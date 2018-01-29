import requests
from lxml import etree

ICAO_CODE = 'LKTB'
WEATHER_SOURCE = 'https://aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&stationString={}&hoursBeforeNow=1'.format(ICAO_CODE)

def get_current_weather():
    response = requests.get(WEATHER_SOURCE)
    tree = etree.fromstring(response.content)
    for element in tree.findall('.//data/METAR'):
        time = element.find('./observation_time').text
        temperature = element.find('./temp_c').text
        print('{0}- {1}'.format(time, temperature))

if __name__ == '__main__':
    get_current_weather()