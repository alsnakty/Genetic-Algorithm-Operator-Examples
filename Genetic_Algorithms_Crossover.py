
import random

#Genetic Algorithms Crossover

def single_point_crossover(chromosome1, chromosome2):
     point = random.randint(1, len(chromosome1)-1)
     offspring = chromosome1[:point] + chromosome2[point:]
     return offspring

def two_point_crossover(chromosome1, chromosome2):
     size  = len(chromosome1)
     start = random.randint(1,int(size/2))
     end = random.randint(int(size/2), size-2)
     offspring = chromosome1[:]
     for i in range(start,end):
          offspring[i] = chromosome2[i] 
     return offspring

def uniform_point_crossover(chromosome1, chromosome2, pointsNum=5):
     offspring = chromosome1[:]
     for i in range(pointsNum):
          selectedPoint = random.randint(0, len(chromosome1)-1)
          offspring[selectedPoint] = chromosome2[selectedPoint]
     return offspring
     
     
 

parents1 = [0,0,0,0,0,0,0,0,0,0]
parents2 = [1,1,1,1,1,1,1,1,1,1]

print("Single Point Crossover")
print(single_point_crossover(parents1,parents2))
print("Two Point Crossover")
print(two_point_crossover(parents1,parents2))
print("Uniform Point Crossover")
print(uniform_point_crossover(parents1,parents2))
