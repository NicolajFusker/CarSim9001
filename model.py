from random import randint

class Car(object):
    pass

class Wheel(object):
    def __init__(self):
        self.oriantation = randint(0, 359)

    def rotate(self, revolutions):
        degreesOfRotation = 360 * revolutions
        self.oriantation = (degreesOfRotation + self.oriantation) % 360


class Engine(object):
    pass

class Gearbox(object):
    pass

class Tank(object):
    pass
