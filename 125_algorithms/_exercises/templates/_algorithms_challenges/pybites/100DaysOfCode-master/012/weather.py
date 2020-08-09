from datetime ______ datetime
______ os

______ pytz
______ requests

API_KEY = os.environ.get('WEATHER_API')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?q='

TIMEZONES = {
    'Sydney': 'Australia/Sydney',
    'Alicante': 'Europe/Madrid',
}

# API docs: http://openweathermap.org/current
URL = ('http://api.openweathermap.org/data/2.5/weather?'
       'q={}&mode=json&units=metric&appid={}')


___ get_weather(cities=TIMEZONES.keys()):
    fmt = 'In {} the weather is: {}, today sun rises at {} and sets at {}'

    output = []
    for city in cities:
        resp = requests.get(URL.format(city, API_KEY))
        info = resp.json()
        main = info["weather"][0]["main"]
        sunrise = get_local_tstamp(city, info["sys"]["sunrise"])
        sunset = get_local_tstamp(city, info["sys"]["sunset"])
        output.append(fmt.format(city, main, sunrise, sunset))

    r_ '\n'.join(output)


___ get_local_tstamp(city, utstamp
    __ city not in TIMEZONES:
        raise ValueError('Not a valid city, check what you call me with')
    tz = TIMEZONES[city]

    try:
        utstamp = int(utstamp)
    except ValueError:
        raise

    # http://stackoverflow.com/questions/12978391/localizing-epoch-time-with-pytz-in-python
    utc_dt = datetime.utcfromtimestamp(utstamp).replace(tzinfo=pytz.utc)
    loc_tz = pytz.timezone(tz)
    dt = utc_dt.astimezone(loc_tz)

    fmt = '%H:%M:%S %Z%z'
    r_ dt.strftime(fmt)


__ __name__ __ '__main__':
    print(get_weather())
