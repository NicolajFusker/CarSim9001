from random import randint # Import random libary

class Car(object): # Create car module
    def __init__(self): # start engine
        self.theEngine = Engine()

    def updateModel(self, dt): # Update the engine
        self.theEngine.updateModel(dt)

class Wheel(object): # Create an recipie for the wheel
    def __init__(self): # Give the wheel a random orientation
        self.orientation = randint(0, 359)

    def rotate(self, revolutions): # Make the wheel able to turn
        degreesOfRotation = 360 * revolutions
        self.orientation = (degreesOfRotation + self.orientation) % 360

class Engine(object): # Create the engine
    def __init__(self): # Define variables for the engine
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()

    def updateModel(self, dt):# Start the engine
        if self.theTank.contents > 0:
            self.currentRpm = self.throttlePosition * self.maxRpm
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            self.theGearbox.rotate(self.currentRpm * (dt/60))
        else:
            self.currentRpm = 0

class Gearbox(object): # Create a gearbox
    def __init__(self): # Create four wheels
        self.wheels = {}
        for newWheel in ['frontLeft', 'frontRight', 'rearLeft', 'rearRight']:
            self.wheels[newWheel] = Wheel()

        self.currentGear = 0
        self.clutchEngaged = False
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]

    def shiftUp(self): # Shift up
        if self.currentGear < len(self.gears) - 1 and not self.clutchEngaged:
            self.currentGear += 1

    def shiftDown(self): # shift down
        if self.currentGear > 0 and not self.clutchEngaged:
            self.currentGear -= 1

    def rotate(self, revolutions): # Turn the Wheels
        if self.clutchEngaged:
            newRevs = revolutions * self.gears[self.currentGear]
            for wheel in self.wheels:
                self.wheels[wheel].rotate(newRevs)


class Tank(object): # Create a tank
    def __init__(self): # Define variables for the tank, and fill the tank
        self.capacity = 100
        self.contents = 100

    def remove(self,amount): # Remove fuel from the tank
        self.contents -= amount
        if self.contents < 0:
            self.contents = 0

    def refuel(self): # Refuel the tank
        self.contents = self.capacity

