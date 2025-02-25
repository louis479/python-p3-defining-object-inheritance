from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"

from car import Car
c = Car(56, 4)
print(c.wheel_size)  # Should print 16
print(c.go())        # Should print "vrrrrrrrooom!"
print(c.fill_up_tank())  # Should print "filling up!"
