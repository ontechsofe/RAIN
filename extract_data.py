from datetime import datetime, timedelta  
from time import mktime, sleep 
from collections import namedtuple  
from pandas import DataFrame  
import requests
from matplotlib.pyplot import *
from keys import *
from tqdm import tqdm

NUMBER_TO_EXPORT = 1
# KEY, LAT, LONG, TIME(UNIX)
BASE_URL = 'https://api.darksky.net/forecast'
# North Oshawa Latitude and Longitude
NORTH_OSHAWA = [43.897095, -78.865791]

def toUnixTime(dt) -> float:
    return int(mktime(dt.timetuple()))

def toReadableTime(ts) -> str:
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')

def request_weather_data(api_key, target_date, days):
    records = []
    for _ in tqdm(range(0, days)):
        request = f"{BASE_URL}/{api_key}/{NORTH_OSHAWA[0]},{NORTH_OSHAWA[1]},{target_date}?exclude=currently,flags"
        response = requests.get(request)
        valid_day = True
        if response.status_code == 200:
            hourly = response.json()['hourly']['data']
            daily = response.json()['daily']['data'][0]
            temperatures = list()
            humidities = list()
            dew_points = list()
            pressures = list()
            for x in hourly:
                # Checking that they all exist
                if all(feat in x for feat in ['temperature', 'humidity', 'dewPoint', 'pressure']):
                    temperatures.append(x['temperature'])
                    humidities.append(x['humidity'])
                    dew_points.append(x['dewPoint'])
                    pressures.append(x['pressure'])
                else:
                    valid_day = False
            if valid_day and all(feat in daily for feat in ['dewPoint', 'pressure', 'temperatureMax', 'temperatureMin', 'precipProbability', 'precipIntensity']):
                mean_temp = sum(temperatures)/float(len(temperatures))
                max_humidity = max(humidities)
                min_humidity = min(humidities)
                max_dewpt = max(dew_points)
                min_dewpt = min(dew_points)
                max_pressure = max(pressures)
                min_pressure = min(pressures)
                # All below are averages per day
                records.append(DailySummary(
                    date=toReadableTime(target_date),
                    mean_temp=mean_temp,
                    mean_dewpt=daily['dewPoint'],
                    mean_pressure=daily['pressure'],
                    max_temp=daily['temperatureMax'],
                    min_temp=daily['temperatureMin'],
                    max_humidity=max_humidity,
                    min_humidity=min_humidity,
                    max_dewpt=max_dewpt,
                    min_dewpt=min_dewpt,
                    max_pressure=max_pressure,
                    min_pressure=min_pressure,
                    precip_probability=daily['precipProbability'],
                    precip_intensity=daily['precipIntensity']
                ))            
        # Reduces one day on UNIX time
        target_date -= 86400
    return records

target_date = toUnixTime(datetime(2017, 12, 31))

features = ['date', 'mean_temp', 'mean_dewpt', 'mean_pressure', 
            'max_temp', 'min_temp', 'max_humidity', 'min_humidity',
            'max_dewpt', 'min_dewpt', 'max_pressure', 'min_pressure'
            ,'precip_probability', 'precip_intensity']
DailySummary = namedtuple("DailySummary", features)
records = request_weather_data(SAFE_KEY, target_date, NUMBER_TO_EXPORT)
df = DataFrame(records, columns=features).set_index('date')
df.to_csv('training_data.csv', sep=',')