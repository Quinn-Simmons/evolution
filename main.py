import random
import time
import os

#global vars


class Environment:
  def __init__(self,h,w, numAnimals):
    self.h = h
    self.w = w
    self.time = 0 
    self.grid = self.createGrid(h,w)
    self.animals = []
    self.foods = []
    
    for i in range (numAnimals):  
      an1 = Animal("@", [0,0])
      self.animals.append(an1)
      
    self.foodPerDay = int((self.h * self.w) / 50)
    for i in range(self.foodPerDay):
      food1 = Food("#", [random.randint(0, self.h -1 ), random.randint(0, self.w - 1)])
      self.grid[food1.location[0]][food1.location[1]] = food1.char
      
      self.foods.append(food1)   
      
       
  
      

  def update(self):
    for animal in self.animals:


      if(type(self.grid[animal.location[0]][animal.location[1]]) == "Food"):
        

      
      self.grid[animal.location[0]][animal.location[1]] = ","
      #this is where the code for the animals eating food will go


      #remove the food we run over from the food array 



      for x in range(animal.location[0] - 1, animal.location[0] + 1):
        for y in range (animal.location[1] - 1, animal.location[1] + 1):
          if type(self.grid[x][y]) == "Food":
            if self.grid[x][y].objType == "food":
              print("found food")










      animal.update()
      self.grid[animal.location[0]][animal.location[1]] = animal.char
    self.displayEnv()

  def createGrid(self,h,w):
    grid = []
    for i in range(h):
      row = []
      for j in range(w):
        row. append(",")
      grid.append(row)
    return grid
  def displayEnv(self):
    for i in range(self.h):
      for j in range(self.w):
        print(self.grid[i][j], end = " ")
      print("")

class Animal:
  def __init__(self, char, location):
    self.char = char
    self.location = location
    self.eaten = 0
    self.objType = "animal"

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
  time.sleep(0.1)
 
  os.system('clear')
  simTime-=1

