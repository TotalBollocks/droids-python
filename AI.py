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

  def spawn(self):
    self.players[self.playerID].orbitalDrop(0,0, random.randint(0,7))

  def init(self):
    pass

  def end(self):
    pass

  ##This function is called once, before your first turn
  def run(self):
    self.spawn()

  def __init__(self, conn):
    BaseAI.__init__(self, conn)