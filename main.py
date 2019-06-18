import random
import time
import os

#global vars

#Sets up and manages the animals, foods, grid, and overall game.
class Environment:
  def __init__(self,h,w, numAnimals):
    self.h = h
    self.w = w
    self.time = 0 
    self.grid = self.createGrid(h,w)
    self.animals = []
    self.foods = []
    
    #initilization
    for i in range (numAnimals):  
      an1 = Animal("@", [4,4])
      self.animals.append(an1)
      
    self.foodPerDay = int((self.h * self.w) / 50)
    for i in range(self.foodPerDay):
      food1 = Food("#", [random.randint(0, self.h -1 ), random.randint(0, self.w - 1)])
      self.grid[food1.location[0]][food1.location[1]].append(food1)
      self.foods.append(food1)   
      
       
  def update(self):
    for animal in self.animals:
      #we dont know where the animal was after it updates

      #take the animal at its old location and pop it out of the tile 
      #this is the tile that the animal is in 
      self.grid[animal.location[0]][animal.location[1]].pop(-1)
     
      animal.update()
      #at the new tile, append the animal
      self.grid[animal.location[0]][animal.location[1]].append(animal)
    self.displayEnv()

  def createGrid(self,h,w):
    grid = []
    for i in range(h):
      row = []
      for j in range(w):
        tile = []
        #create a terrain object at i and j, and then place it into tile 
        ter1 = Terrain(i, j, ",")
        tile.append(ter1)
        row.append(tile)
      grid.append(row)
    return grid

  def displayEnv(self):
    for i in range(self.h):
      for j in range(self.w):
        #printing the string rn 
        
        print(self.grid[i][j][-1].char, end = " ")
      print("")


class Terrain:
  def __init__(self, x, y, char):
    self.x = x
    self.y = y
    self.char = char

class Animal:
  def __init__(self, char, location):
    self.char = char
    self.location = location
    self.eaten = 0
    self.objType = "animal"
  #changes an instance var of animal, not its actual position
  def move(self):
    self.location[0] += random.randint(-1, 1)
    self.location[1] += random.randint(-1, 1)
    return self.location  
  def update(self):
    self.move()  

class Food:
  def __init__(self, char, location):
    self.char = char
    self.location = location
    self.nutrition = random.randint(1,2)
    self.growing = True
    self.objType = "food"
  def update(self):
    if self.growing == True:
      self.nutition += 1
    if self.growing == False:
      self.nutrition -= 1
    if self.nutrition >= 10:
      self.growing = False
    
    if self.nutrition <= 0:
      del self

env1 = Environment(20,20,6)
simTime = 120

while(simTime > 0):
  env1.update()
  time.sleep(1)
 
  os.system('clear')
  simTime-=1

