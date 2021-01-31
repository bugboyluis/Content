class Missile(GImage):
    """
    A class for the boss' Missile attack.
    Has only two hit points (from and back) instead of 4 corners.
    Is designed to track the ship's movement up until a certain y value (300)
    Speed of missile = BOLT_SPEED//4

    Attributes:
    radangle: angle of rotation in radians
    _type: the projectile type (ONLY 'm')
    _radangle: the angle of rotation in radians (number)
    """
    def getY(self):
        """
        Returns the y coordinate of the missile
        """
        return self.y

    def getType(self):
        """
        Returns the projectile type.
        """
        return self._type

    def __init__(self,x,y,ship):
        """
        Initializer for the missile bolt.

        Parameter x: the x coordinate of the missile.
        Precondition: x is a float >= 0

        Parameter y: the y coordinate of the missile.
        Precondition: y is a float >= 0

        Parameter ship: the ship object that the missile follows.
        Precondition: ship is a valid ship object.
        """
        super().__init__(x=x,y=y,width=15,height=30,source='Missile.png')
        self._type = 'm'
        self._radangle = self.relativeangle(ship)
        self.angle = -1 * self.relativeangle(ship) * 180/math.pi

    def missileupdate(self,ship):
        """
        Updates the missiles angle of rotation accordingly and moves the missile.

        Paremeter ship: A ship object to get x and y coordinates from.
        Precondition: ship is a valid ship object.
        """
        if ship != None:
            if self.y > 250:
                self._radangle = self.relativeangle(ship)
                self.angle = -1 * self._radangle * 180/math.pi
                self.y -= math.cos(self._radangle) * BOLT_SPEED/4
                self.x -= math.sin(self._radangle) * BOLT_SPEED/4
            else:
                self.y -= math.cos(self._radangle) * BOLT_SPEED/4
                self.x -= math.sin(self._radangle) * BOLT_SPEED/4

    def relativeangle(self,ship):
        """
        Returns the angle of rotation needed for the missile to follow the ship

        Paremeter ship: A ship object to get x and y coordinates from.
        Precondition: ship is a valid ship object.
        """
        x = self.x - ship.x
        y = self.y - ship.y
        return math.atan(x/y)

    def ends(self):
        """
        Returns the coordinates of the ends of the missile as a list of ints or floats.
        """
        end = []
        back = [self.x-(15*math.sin(self._radangle)),\
        self.y-(15*math.cos(self._radangle))]
        front = [self.x+(15*math.sin(self._radangle)),\
        self.y+(15*math.cos(self._radangle))]
        end.append(back)
        end.append(front)
        return end
