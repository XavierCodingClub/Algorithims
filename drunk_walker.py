import random
import os
import time

print("hello world")

arr = [[0 for i in range(100)] for j in range(100)]

def print_array():
    for i in range(100):
      for j in range(100):
        if(arr[i][j] == 1):
          print(" ", end="")
        else:
          print("#", end="")
      print("")


# random.seed(time.time())
print_array()

steps_max = int(input("How many steps?"))
current_steps = int(0)

x_pos = int(50)
y_pos = int(50)

while(current_steps < steps_max):
  direction = random.randint(1, 4)
  if(direction == 1):
    y_pos -= 1
  if(direction == 2):
    x_pos += 1
  if(direction == 3):
    y_pos += 1
  if(direction == 4):
    x_pos -= 1

  arr[x_pos][y_pos] = 1
  
  if(x_pos > 98 or x_pos < 2):
    x_pos = 50
  if(y_pos > 98 or y_pos < 2):
    y_pos = 50
  current_steps += 1

  print_array()
  time.sleep(1)
  os.system("clear")
  

print_array()
