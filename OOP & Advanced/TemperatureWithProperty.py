from xml.dom.minidom import ProcessingInstruction

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        print("Getting Fahrenheit")
        return (self._celsius * 9 / 5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        print("Setting Fahrenheit")
        self._celsius = (value - 32) * 5 / 9

    @fahrenheit.deleter
    def fahrenheit(self):
        print("Fahrenheit deleting")
        self._celsius = None


t = Temperature(0)
print(f"Initial Celsius: {t._celsius}")
print(f"Initial Fahrenheit {t.fahrenheit}")

t.fahrenheit = 321
print(f"Updated Clesius: {t._celsius}")
print(f"Updated Celsius: {t.fahrenheit}")

del t.fahrenheit

print(t._celsius)
