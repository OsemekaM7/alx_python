def convert_to_celsius(fahrenheit):
    celcius = ((fahrenheit-32)*(5/9))
    if celcius < -273.15:
        return -273.15
    elif celcius > 273.15:
        return 273.15
    else:
        return celcius
