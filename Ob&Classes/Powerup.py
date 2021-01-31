class Powerup(object):
    """
    A collection of GRectangles and a GLabel to represent a powerup that releases
    8 ship bolts in a spread pattern when fully charged.
    _chargemeter: a list of GRectangles representing the charge bars.
    _chargeaccumulation: the total amount of charge accumulated (int range 0..CHARGE)
    _chargep: a GLabel to display the total amount stored as a percentage.
    _blast: a list of 'p' bolts that are then transfered to the wave.
    _blam: A valid sound object that plays when the power up is fired.
    """
    def getChargepercent(self):
        """
        Returns the _charep attribute.
        """
        return self._chargep

    def getChargeBar(self):
        """
        Returns the _chargemeter attribute.
        """
        return self._chargemeter

    def getBlast(self):
        """
        Returns the _blast attribute.
        """
        return self._blast

    def __init__(self):
        """
        Initializer for the powerup object. Creates CHARGE number of
        Grey GRectangles and a GLabel with a percentage representing the
        total amount of charge.
        """
        self._chargemeter = []
        self._chargeaccumulation = 0
        self._blast = []
        self._blam = Sound('PowerUp.wav')
        for c in range(CHARGE):
            self._chargemeter.append(GRectangle(x=GAME_WIDTH/20 + 50/CHARGE +\
            c*100/CHARGE,y=GAME_HEIGHT*7/8,width=100/CHARGE,\
            height=20,fillcolor='grey'))
        self._chargep = GLabel(x=GAME_WIDTH/20 + 50,y=GAME_HEIGHT*7/8,\
        font_name='RetroGame',font_size = 20,linecolor='black',\
        text=str(self._chargeaccumulation*100/CHARGE)+'%')

    def PowerUpdate(self,input,ship,mute):
        """
        Update method for the powerup class.
        Changes the colors of the rectangles appropriately and checks whether
        the activation key is pressed.

        Parameter input: checks whether the appropriate key is pressed.
        Precondition: input is a valid input

        Parameter ship: the ship that fires the special attack.
        Precondition: ship is a valid ship object or None

        Parameter mute: determines whether the attack makes a sound.
        Precondition: mute is a bool
        """
        if self._chargeaccumulation > 0:
            for c in range(self._chargeaccumulation):
                self._chargemeter[c].fillcolor = 'purple'
        self._chargep.text = str(round(self._chargeaccumulation*100/CHARGE))+'%'
        if ship != None:
            if self._chargeaccumulation == CHARGE and input.is_key_down('w'):
                self.FIRE(ship)
                if mute == False:
                    self._blam.play()
                self._chargeaccumulation = 0
                for c in range(CHARGE):
                    self._chargemeter[c].fillcolor = 'grey'

    def PowerIncrease(self):
        """
        Increases the _chargeaccumulation by 1. Does not let this value go over
        the constant CHARGE.
        """
        if not self._chargeaccumulation >= CHARGE:
            self._chargeaccumulation += 1

    def FIRE(self,ship):
        """
        Fires a set of POWER bolts in an arc.
        Parameter ship: the ship that fires the special attack.
        Precondition: ship is a valid ship object
        """
        for a in range(POWER):
            self._blast.append(Bolt(ship.getX(),ship.getY()+SHIP_HEIGHT,type='p',\
            angle=(a+0.5)*ANGLE/POWER - ANGLE/2))