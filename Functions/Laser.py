def laserattack(self,dt):
        """
        FIRES THE LASER (starts the ship laser animation and creates a beam
        object from the nose of the boss ship.)

        The laser charges for 2.5 seconds and then fires for 1.5 seconds.

        Paremeter dt: time value passed from invaders.
        Precondition: dt is a number >= 0
        """
        if self._laser == True:
            if self._beamtime >=4:
                for bolt in self._bolts:
                    if bolt.getType() == 'b':
                        self._bolts.remove(bolt)
                self._laser = False
                self._beamtime = 0
                self._aliens.restore()
            elif self._beamtime >= 2.5:
                x = False
                beam = None
                for bolt in self._bolts:
                    if bolt.getType() == 'b':
                        x = True
                        beam = bolt
                if x == True:
                    beam.beamupdate(self._aliens)
                else:
                    self._bolts.append(Beam(self._aliens))
                    if self._mutesound == False:
                        self._aliens.blaah()
                self._beamtime += dt
            else:
                self._beamtime += dt
         
        
-----------------------------------------------------------------------------------------   
=========================================================================================
-----------------------------------------------------------------------------------------                
                
                
def update(self,laser):
        """
        Update method for the boss to animate its laser firing animation.

        Parameter laser: determines whether to animate or not.
        Precondition: laser is a bool
        """
        if laser == True:
            if self.frame == 0:
                self._frames = self.lasercharge()
                self.frame = self._frames[self._count%16]
                self._count += 1
            elif self.frame <= 14 and self._count < 16:
                if self._frames != None:
                    self.frame = self._frames[self._count%16]
                    self._count += 1
                    if self._count >= 16:
                        self.frame = 15
                        self._frames = self.laserhold()
                        self._count = 0
            elif self.frame > 14:
                if self._frames != None:
                    self._count += 1
                    self.frame = self._frames[self._count%4]                
