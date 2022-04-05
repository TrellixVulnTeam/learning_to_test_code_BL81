# Notes and examples on how to use property decorator
# KZ 3-29-22

# property is like pythons way of getter/setter in other languages (Java, C++)

class Celsius:
    def __init__(self, temperature: int = 0):
        self.temperature = temperature

    def to_farenheight(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("getting value...")
        return self._temperature
    
    @temperature.setter
    def temperature(self, value: int):
        print("setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

    def __str__(self):
        return f'<Celsius>: {self.temperature}'


if __name__ == '__main__':
    c = Celsius()
    print(c)