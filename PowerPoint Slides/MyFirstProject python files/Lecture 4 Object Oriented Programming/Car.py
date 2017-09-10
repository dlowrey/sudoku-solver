
class Car():

    # the constructor used to make a Car object
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def set_color(self, color):
        self.color = color

    # Get THIS Car's color
    def get_color(self):
        return self.color

    # Get THIS Car's model
    def get_model(self):
        return self.model

    # Get THIS Car's year
    def get_year(self):
        return self.year

    # Get THIS Car's make
    def get_make(self):
        return self.make

    def is_old(self):
        # If the Car was made in 2000,
        # we consider it old
        old = False
        if self.year < 2000:
            old = True
        return old

# First car object
my_car = Car('GMC', 'Yukon', 2005, 'White')

print('Car color {}'.format(my_car.get_color()))

my_car.set_color('Blue')

print('Car color {}'.format(my_car.get_color()))




# Another car object
your_car = Car('FORD', 'Mustang', 2016, 'Red')

print('My car is {}, your car is {}'.format(my_car.get_color(), your_car.color))
