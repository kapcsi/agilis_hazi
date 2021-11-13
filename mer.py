
from sensor import sensor_class
from machine import machine_class
from analyzer import analyze_sesor_data


def run(machines,tresholds):
    for machine in machines:
        data_to_analyze =  machine()
        try:
            analyze_sesor_data(data_to_analyze,tresholds)
        except Exception as error:
            print(error)
            print("Problem with " + machine.name+ ", except failure! Check log data"  )

if __name__ == '__main__':
    tresholds= dict(MHz= dict(max=75,min=25),Ohm= dict(max=750,min=250),Watt= dict(max=7.5,min=2.5))
    current_machines = []
    sensor_cluster1 = []
    sensor1 = sensor_class("Arm 1","MHz")
    sensor2 = sensor_class("Arm 2","MHz")
    sensor3 = sensor_class("Board1","Ohm")
    sensor4 = sensor_class("Board2","Ohm")
    sensor5 = sensor_class("PowerSupply1","Watt")
    sensor6 = sensor_class("PowerSupply2","Watt")

    sensor_cluster1.append(sensor1)
    sensor_cluster1.append(sensor2)
    sensor_cluster1.append(sensor3)
    sensor_cluster1.append(sensor4)
    sensor_cluster1.append(sensor5)
    sensor_cluster1.append(sensor6)

    current_machines.append(machine_class("robot1",sensor_cluster1))
    current_machines.append(machine_class("robot2",sensor_cluster1))
    current_machines.append(machine_class("robot3",sensor_cluster1))
    
    for i in range(0,1):
       run(current_machines,tresholds)