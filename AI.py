#-*-python-*-
from BaseAI import BaseAI
from GameObject import *
from random  import *

class AI(BaseAI):
  """The class implementing gameplay logic."""
  @staticmethod
  def username():
    return "Shell AI"

  @staticmethod
  def password():
    return "password"

  CLAW, ARCHER, REPAIRER, HACKER, TURRET, WALL, TERMINATOR, HANGAR = range(8)

  def spawn_units(self):
    if self.playerID == 0:
	  x = 0
	  y = randint(0, self.mapHeight-1)
    else:
	  x = self.mapWidth-1
	  y = randint(0, self.mapHeight-1)
	  
    self.players[self.playerID].orbitalDrop(x,y, randint(0,7))

  def move_units(self):
    if self.playerID == 0:
      for droid in self.droids:
        droid.move(droid.x+1, droid.y)
        print "Droid moved to (%s, %s)" % (droid.x, droid.y)
  	  
    elif self.playerID == 1:
      for droid in self.droids:
        droid.move(droid.x+1, droid.y)
        print "Droid moved to (%s, %s)" % (droid.x, droid.y)
	  

  def init(self):
    pass

  def end(self):
    pass

  ##This function is called once, before your first turn
  def run(self):
    self.spawn_units()
    self.move_units()
    return 1

  def __init__(self, conn):
    BaseAI.__init__(self, conn)