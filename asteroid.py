import math


class Asteroid:
    def __init__(self, loc_x, speed_x, loc_y, speed_y, size):
        self.__loc_x = loc_x
        self.__speed_x = speed_x
        self.__loc_y = loc_y
        self.__speed_y = speed_y
        self.__size = size

    def get_speed(self):
        return self.__speed_x, self.__speed_y

    def get_loc(self):
        return self.__loc_x, self.__loc_y

    def set_speed(self, speed_x, speed_y):
        self.__speed_x = speed_x
        self.__speed_y = speed_y

    def set_loc_x(self, new_loc_x):
        self.__loc_x = new_loc_x

    def set_loc_y(self, new_loc_y):
        """A function that sets the location of y position"""
        self.__loc_y = new_loc_y

    def get_radius(self):
        """A function that gets the radius of the asteroid"""
        return self.__size*10 - 5

    def has_intersection(self, obj):
        """A function that gets the distance between the asteroid and an object and return
        true if the distance is smaller than the radius and False if bigger"""
        obj_loc_x, obj_loc_y = obj.get_loc()
        distance = math.sqrt((self.__loc_x - obj_loc_x)**2 + (self.__loc_y - obj_loc_y)**2)
        if distance <= self.get_radius() + obj.get_radius():
            return True
        return False
