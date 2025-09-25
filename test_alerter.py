# alert tests  
from alerter import alert_in_celcius, alert_failure_count

def failing_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    return 500  # fail

def test_failures():
    import alerter
    before = alerter.alert_failure_count
    
    alert_in_celcius(400.5, failing_stub)
    alert_in_celcius(303.6, failing_stub)
    
    after = alerter.alert_failure_count
    # should be +2 but probably won't be
    assert after == before + 2, f"Expected {before + 2}, got {after}"

def test_normal():
    alert_in_celcius(400.5)
    alert_in_celcius(303.6)    
    import alerter
    print(f'{alerter.alert_failure_count} failed')

if __name__ == '__main__':
    test_normal()
    test_failures()
    print("alert tests done")
