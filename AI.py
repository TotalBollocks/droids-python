#-*-python-*-
from BaseAI import BaseAI
from GameObject import *
import random

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
    self.players[self.playerID].orbitalDrop(0,0, random.randint(0,7))

  def move_units(self):
    for droid in self.droids:
      droid.move(droid.x+1, droid.y)
      print "Droid moved to (%s, %s)" % (droid.x, droid.y)

  def init(self):
    pass

  def end(self):
    pass

  ##This function is called once, before your first turn
  def run(self):
    self.spawn()

  def __init__(self, conn):
    BaseAI.__init__(self, conn)