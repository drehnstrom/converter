class Converter:

    def __init__(self):
        self.temp_to_convert = -40.0
        self.converted_temp = -40.0


    def setTemp(self, temp):
        self.temp_to_convert = temp


    def toCelsius(self):
        self.converted_temp = (self.temp_to_convert - 32.0) * 5.0 / 9.0


    def toFahrenheit(self):
        self.converted_temp = self.temp_to_convert * 9.0 / 5.0 + 32.0