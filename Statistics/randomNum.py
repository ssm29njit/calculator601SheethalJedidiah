from random import random


def getRandomNum(data,sample_size):
    random_values = random.sample(data, k=sample_size-1)
    return random_values

#def getSample(data, sample_size):
 #   random_values = random.sample(data, k=sample_size)
 #   return random_values