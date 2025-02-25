class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        return "vroom! vroom! vroom!"
    
    def fill_up_tank(self):
        return "filling up!"

from vehicle import Vehicle

v = Vehicle(18, 4)
print(v.wheel_size)  # Should print 18
print(v.go())        # Should print "vrrrrrrrooom!"
print(v.fill_up_tank())  # Should print "filling up!"

