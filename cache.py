class cache:
  enemy_hangars = []
  enemy_droids = []
  my_droids = []

  ai = None

  def __init__(self, ai):
    self.ai = ai

    self.clean_droids()
    
  def clean_droids(self):
    grid = []
    for i in self.ai.mapWidth:
      grid.push([])
      for x in grid[i]:
        x.push([])
    self.my_droids = grid
    self.enemy_droids = grid
    self.enemy_hangars = grid


  def update_droids(self):
    self.clean_droids()

    for droid in self.ai.droids:
      if droid.owner == self.ai.playerID:
        self.my_droids[droid.x][droid.y] = droid

      elif droid.owner == self.ai.playerID^1:
        self.enemy_droids[droid.x][droid.y] = droid

        if droid.variant == self.ai.HANGAR:
          self.enemy_hangars[droid.x][droid.y] = droid


      else:
        print("THIS IS WRONG.")


