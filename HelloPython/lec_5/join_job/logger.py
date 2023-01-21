from datetime import datetime as dt

def temperature_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};temperature;{}'
                   .format(time))


def pressure_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};pressure;{}'
                   .format(time))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};wind_speed;{}'
                   .format(time))

