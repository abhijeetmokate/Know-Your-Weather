class Weather:
    def __init__(self, name, wea, temp, pre, hum, country, wind_speed):
        self.city_name = name
        self.weather_condition = wea
        self.temperature = temp
        self.pressure = pre
        self.humidity = hum
        self.country = country
        self.wind_speed = wind_speed

    def get_city_name(self):
        return self.city_name

    def get_weather_condition(self):
        return self.weather_condition

    def get_temperature(self):
        return self.temperature

    def get_pressure(self):
        return self.pressure

    def get_humidity(self):
        return self.humidity

    def get_country(self):
        return self.country

    def get_wind_speed(self):
        return self.wind_speed
