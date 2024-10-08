#==========================================================
# CS 330-01 Programming Assignment 1
# Dynamic Movement Newton-Euler 1 Movement Update Algorithm
# Eric Delgado
# 09/29/2024 
#==========================================================

import math
import copy

class Character:
    def __init__(self, time, id, positionX, positionZ, velocityX, velocityZ, 
                 linearAccX, linearAccZ, orientation, steeringCode, 
                 collisionStatus, maxVelocity, maxAcceleration,
                 arrivalRadius, slowingRadius, timeToTarget):
        
        self.time = time                        # simulation time
        self.id = id                            # character id (numeric)
        self.positionX = positionX              # position x (meters)
        self.positionZ = positionZ              # position z (meters)
        self.velocityX = velocityX              # velocity x (meters)
        self.velocityZ = velocityZ              # velocity y (meters)
        self.linearAccX = linearAccX            # linear acceleration x (meters per second per second)
        self.linearAccZ = linearAccZ            # linear acceleration z (meters per second per second)
        self.orientation = orientation          # character orientation (radians)
        self.steeringCode = steeringCode        # steering hevaior code (1=continueCharacter, 6=seek, 7=flee, 8=arrive)
        self.collisionStatus = collisionStatus  # always false in this implementation
        self.maxVelocity = maxVelocity          # velocity cap used for regulating character speed
        self.maxAcceleration = maxAcceleration  # acceleration cap used for regulating character acceleration
        self.arrivalRadius = arrivalRadius      # distance to target where character stops
        self.slowingRadius = slowingRadius      # distance to target where character slow down occurs
        self.timeToTarget = timeToTarget 

    def seek(self, source, target):

        # Get the direction to the target.
        directionVector = [(target.positionX - source.positionX), 
                           (target.positionZ - source.positionZ)]
    
        # Acccelerate at the maximum rate.
        posVector = self.__normalize(directionVector[0], directionVector[1], self.maxAcceleration)

        self.__update(posVector) 

    def flee(self, source, target):

        # Get the direction to the target.
        directionVector = [(source.positionX - target.positionX), 
                           (source.positionZ - target.positionZ)]
    
        # Accelerate at maximum rate.
        posVector = self.__normalize(directionVector[0], directionVector[1], self.maxAcceleration)

        self.__update(posVector) 

    def arrive(self, source, target):

        # The desired speed used to reach the target.
        targetSpeed = 0 

        # Get direction to the target.
        directionVector = [(target.positionX - source.positionX), 
                           (target.positionZ - source.positionZ)]
    
        # Calculate the length of directionVector.
        length = self.__lengthOf(directionVector[0], directionVector[1])

        # Test for arrival.
        # If the distance is within the target radius, do nothing.
        if length < self.arrivalRadius:
            pass

        # If character is outside of target and arrival radius
        # set the desired speed to the max speed.
        elif length > self.slowingRadius:
            targetSpeed = self.maxVelocity
        
        # If the character is between target and arrival radius
        # slow down the desired speed while approaching target.
        else:
            targetSpeed = self.maxVelocity * length / self.slowingRadius
        
        # Velocity vector for the desired velocity (speed and direction).
        velocityVector = self.__normalize(directionVector[0], directionVector[1], targetSpeed)

        # Accelerate to the target velocity.
        linearAccVector =[((velocityVector[0] - source.velocityX) / self.timeToTarget),
                          ((velocityVector[1] - source.velocityZ) / self.timeToTarget)]

        length = self.__lengthOf(linearAccVector[0], linearAccVector[1])

        # If the current acceleration is faster than max acceleration
        # then normalize the acceleration vector.
        if length > self.maxAcceleration:

            linearAccVector = self.__normalize(linearAccVector[0], linearAccVector[1], self.maxAcceleration)

            self.linearAccX = linearAccVector[0]
            self.linearAccZ = linearAccVector[1]

        # Update acceleration if current acceleration is slower
        # than its max acceleration.
        else:
            self.linearAccX = linearAccVector[0]
            self.linearAccZ = linearAccVector[1]

        self.__update(linearAccVector) 

    def continueCharacter(self, source):
        
        linearVector = [source.linearAccX, source.linearAccZ]
        angularVector = [source.orientation]

        result = [linearVector, angularVector]
        
        return result

    def __update(self, vector):

        self.time += 0.5    # increase total time by 0.5 sec
        deltaTime = 0.5     # timestep used in calculations

        # Compute the length of linear acceleration vector.
        length = self.__lengthOf(self.linearAccX, self.linearAccZ)

        # Prevents character's acceleration from exceeding maxAcceleration.
        # Acceleration vector is normalized and acceleration values are updated.
        if length > self.maxAcceleration:
            self.linearAccX = (self.linearAccX / length) * self.maxAcceleration
            self.linearAccZ = (self.linearAccZ / length) * self.maxAcceleration
        
        else:
            self.linearAccX = vector[0]
            self.linearAccZ = vector[1]

        # Update the position of the character.
        self.positionX += (self.velocityX * deltaTime)
        self.positionZ += (self.velocityZ * deltaTime)

        # Update the velocity of the chracter.
        self.velocityX += (vector[0] * deltaTime)
        self.velocityZ += (vector[1] * deltaTime)

        # Compute the length of velocity vector.
        length = self.__lengthOf(self.velocityX, self.velocityZ)

        # Prevents character's speed from exceeding maxVelocity.
        # Speed vector is normalized and velocity values are updated.
        if length > self.maxVelocity:
            self.velocityX = (self.velocityX / length) * self.maxVelocity
            self.velocityZ = (self.velocityZ / length) * self.maxVelocity
    
    def __lengthOf(self, x, z):

        return math.sqrt(math.pow(x, 2) + math.pow(z, 2))

    def __normalize(self, x, z, vectorQuantity):

        vector = []

        length = self.__lengthOf(x, z)

        vector.append((x / length) * vectorQuantity)
        vector.append((z / length) * vectorQuantity)

        return vector

trajectoryList = []
time = 0 

# Instantiate characters with base values.
character1 = Character(0, 2601, 0, 0, 0, 0, 0, 0, 0, 1, 
                       False, 0, 0, 0, 0, 0)                                # continue character
character2 = Character(0, 2602, -30, -50, 2, 7, 0, 0, math.pi / 4, 7, 
                       False, 8, 1.5, 0, 0, 0)                              # flee character
character3 = Character(0, 2603, -50, 40, 0, 8, 0, 0, 3 * math.pi / 2, 6, 
                       False, 8, 2, 0, 0, 0)                                # seek character
character4 = Character(0, 2604, 50, 75, -9, 4, 0, 0, math.pi, 8, 
                       False, 10, 2, 4, 32, 1)                              # arrive character

# Populate trajectoryList and invoke character functions at each timestep.
while time <= 50:

    trajectoryList.append(copy.copy(character1))
    trajectoryList.append(copy.copy(character2))
    trajectoryList.append(copy.copy(character3))
    trajectoryList.append(copy.copy(character4))
    character1.continueCharacter(character1)
    character2.flee(character2, character1)
    character3.seek(character3, character1)
    character4.arrive(character4, character1)

    time += 0.5

file = open('results.txt', 'w')

# Iterate through each element in trajectoryList and write each line to file.
for Character in trajectoryList:

    file.write(str(Character.time)
               + "," + str(Character.id)
               + "," + str(Character.positionX)
               + "," + str(Character.positionZ)
               + "," + str(Character.velocityX)
               + "," + str(Character.velocityZ)
               + "," + str(Character.linearAccX)
               + "," + str(Character.linearAccZ)
               + "," + str(Character.orientation)
               + "," + str(Character.steeringCode)
               + "," + str(Character.collisionStatus)
               + "\n")

file.close