def Shieldupdate(self,dt,x,y,mute):
      """
      Updates the shield animation frames and plays sounds.

      Parameter x: the x coordinate of the shield.
      Precondition: x is a float >= 0

      Parameter y: the y coordinate of the shield.
      Precondition: y is a float >= 0

      Parameter dt: time value passed down.
      Precondition: dt is a number >= 0

      Parameter mute: determines whether the attack makes a sound.
      Precondition: mute is a bool
      """
      self.x = x
      self.y = y
      if self._active == True:
          if self.frame <= 3:
              self.frame = self._frames[self._count % 8]
              self._count += 1
          elif self.frame >= 17:
              if self._time >= 0.9:
                  self.frame = 0
                  self._time = 0
                  self._count = 0
              if self.frame == 18:
                  self.frame = 17
              elif self.frame == 17:
                  self.frame = 18
              self._time += dt
      else:
          if self.frame <= 3:
              self.frame = 4
              if mute == False:
                  self._fall.play()
          elif self.frame >= 4 and self.frame < 17:
              self.frame = (self.frame+1)%18
          self._time += dt
          if self._time >= 5:
              self._active = True
              self._time = 0
              if mute == False:
                  self._charge.play()