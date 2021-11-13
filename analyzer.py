import random
from logger import our_logger

def analyze_sesor_data(sensor_data,tresholds):
    count = 0
    
    for sensor in sensor_data:
        measurement= sensor["measurement"]
        if measurement == "MHz":
            if tresholds["MHz"]["min"] > sensor["value"]:
                count+= 1
                our_logger.error(str(sensor["value"]) + " " +measurement)
                our_logger.error("Error in " + sensor["sensor_name"] + ". The value is lower than expected")
            if tresholds["MHz"]["max"] < sensor["value"]:
                count+= 1
                our_logger.error(str(sensor["value"]) + " " +measurement)
                our_logger.error("Error in " + sensor["sensor_name"] + ". The value is higher than expected")
        elif measurement == "Watt":
            if tresholds["Watt"]["min"] > sensor["value"]:
                count+= 1
                our_logger.error(str(sensor["value"]) + " " +measurement)
                our_logger.error("Error in " + sensor["sensor_name"] + ". The value is lower than expected")
            if tresholds["Watt"]["max"] < sensor["value"]:
                count+= 1
                our_logger.error(str(sensor["value"]) + " " +measurement)
                our_logger.error("Error in " + sensor["sensor_name"] + ". The value is higher than expected")  
        elif measurement == "Ohm":
            if tresholds["Ohm"]["min"] > sensor["value"]:
                count+= 1
                our_logger.error(str(sensor["value"]) + " " +measurement)
                our_logger.error("Error in " + sensor["sensor_name"] + ". The value is lower than expected")
            if tresholds["Ohm"]["max"] < sensor["value"]:
                count+= 1
                our_logger.error(str(sensor["value"]) + " " +measurement)
                our_logger.error("Error in " + sensor["sensor_name"] + ". The value is higher than expected")
    
    deep_learning_ai(count)
        
def deep_learning_ai(errors):
    if random.random()*errors > 2:
        raise Exception("Possible error")