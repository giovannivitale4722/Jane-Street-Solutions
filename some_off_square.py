import numpy as np
import random
import math

num_of_simulations = 100000
outside = 0 

for i in range(num_of_simulations):
        
        x1 = random.random()
        y1 = random.random()
        x2 = random.random()
        y2 = random.random()

        midpoint_x = (x1 + x2) / 2

        midpoint_y = (y1 + y2) / 2

        diameter = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        radius = diameter / 2

        if radius + midpoint_x > 1:
                        outside += 1
        elif midpoint_x - radius < 0:
                        outside += 1
        elif radius + midpoint_y > 1:
                        outside += 1
        elif midpoint_y - radius < 0:
                        outside += 1


        probability = float(outside/num_of_simulations)
        
print(probability)


