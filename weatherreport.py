

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def highPrecipitationLowWindStub():
    """Stub to expose the bug in weather logic"""
    return {
        'temperatureInC': 30,  # > 25
        'precipitation': 80,   # > 60 (high precipitation)
        'humidity': 26,
        'windSpeedKMPH': 30    # < 50 (low wind speed)
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather
