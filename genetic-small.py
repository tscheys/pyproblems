from random import randint
from math import floor
# implement mini genetic algorithm 

# create a sample population 
# first arg: size of population 
# second arg: number of features
def population(size, featureCount):
  population = []
  for individual in range(0, size - 1):
    population.append([])
    for feature in range(0, featureCount - 1):
      population[individual].append(randint(0, 10))
  return population

# have function accept population
def genetic(population, threshold):
  fittest = []
# check the fitness of every individual
  def helper(population):
    # check threshold
    for individual in population:
      if sum(individual) >= threshold:
        return

    # crossover (copy over features from one and vice versa)
    # sort population on fitness 
    population.sort(key = sum)
    # select 2 fit individuals
    percentage = floor(len(population) / 3)
    elite = population[-percentage:]
    newElite = []
    while elite:
      # select 2 randon individuals
      # select a crossover point 
      # extract both slices 
      # append/ prepend to other individual
      # append them to new elite
      # delete them out of old elite  
    
    # add new elite to population 
    
    # mutate
      # loop through the new population 
        # change between 0 and half of the features to a random number 

    # call helper function with this new generation  
  
