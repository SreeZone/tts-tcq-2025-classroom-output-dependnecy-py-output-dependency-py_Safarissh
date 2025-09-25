# weather tests
from weatherreport import report, sensorStub

def stub_high_rain_low_wind():
    return {
        'temperatureInC': 30,
        'precipitation': 80,  # high
        'humidity': 26,
        'windSpeedKMPH': 30   # low
    }

def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)

def testHighPrecip():
    # trying different conditions
    weather = report(stub_high_rain_low_wind)
    # this should be rainy but gets sunny day - bug?
    assert("rain" in weather.lower()), f"Got: {weather}"

if __name__ == '__main__':
    testRainy()
    testHighPrecip()
    print("done testing weather")
