
class machine_class:
    def __init__(self,name,sensors):
        self.name = name
        self._sensors = sensors
        
    def __call__(self):
        return self.check_state()

    def check_state(self):
        collected_data = []
        for sensor in self._sensors:
            collected_data.append(sensor())
        
        return collected_data