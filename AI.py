#-*-python-*-
from BaseAI import BaseAI
from GameObject import *
import random
from cache import cache

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
      y = random.randint(0, self.mapHeight-1)
      variant = random.randint(0,7)
      self.players[self.playerID].orbitalDrop(x,y,variant)
    elif self.playerID == 1:
      x = self.mapWidth-1
      y = random.randint(0, self.mapHeight-1)
      variant = random.randint(0,7)
      self.players[self.playerID].orbitalDrop(x,y,variant)  
    return

  def move_units(self):
    kill_this = self.find_enemy_hangar()

    for droid in self.droids:
      if droid.owner == self.playerID:
        self.move_to(droid, droid.x, droid.y)


  def move_right(self, droid):
    droid.move(droid.x + 1, droid.y)

  def move_left(self, droid):
    droid.move(droid.x -1, droid.y)

  def move_up(self, droid):
    droid.move(droid.x, droid.y -1)

  def move_down(self, droid):
    droid.move(droid.x, droid.y +1)

  def move_to(self, droid, x, y):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for _ in range(droid.maxMovement):
      if droid.x < x:
        move_right(droid)
      elif droid.x > x:
        move_left(droid)
      elif droid.y < y:
        move_down(droid)
      elif droid.y > y:
        move_up(droid)
      else:
        droid.operate(x, y)


    movement = random.choice(directions)
    new_x, new_y = droid.x + movement[0], droid.y + movement[1]

    for _ in range(droids.maxMovement):
      droid.move(droid.x + movement[0], droid.y + movement[1])
      if self.Cache.my_droids[new_x][new_y] == None:
        if self.Cache.enemy_droids[new_x][new_y] == None:
          # Move

  def find_enemy_hangar(self):
    for droid in self.droids:
      if droid.playerID != self.playerID^1 and droid.variant == self.HANGAR:
        return droid
  return None


  ##This function is called once, before your first turn
  def init(self):
    self.Cache = cache
    pass

  ##This function is called once, after your last turn
  def end(self):
    pass

  ##This function is called each time it is your turn
  ##Return true to end your turn, return false to ask the server for updated information
  def run(self):
    self.spawn_units()

    self.move_units()

    return 1

  def __init__(self, conn):
    BaseAI.__init__(self, conn)