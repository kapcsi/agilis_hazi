import random

class sensor_class:
    def __init__(self,name,measurement):
        self._name = name
        self._measurement = measurement
    
    def __call__(self):
        return self.read_data()

    def read_data(self):
        if self._measurement == "MHz":
            return dict(measurement=self._measurement ,value = random.random()*100, sensor_name = self._name)
        elif self._measurement == "Watt":
            return dict(measurement=self._measurement ,value = random.random()*10,sensor_name = self._name)
        elif self._measurement == "Ohm":
            return dict(measurement=self._measurement ,value = random.random()*1000,sensor_name = self._name)
