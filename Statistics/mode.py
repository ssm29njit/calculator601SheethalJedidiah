import statistics
from Statistics.randomNum import getRandomNum

def mmode(data, sample_size):
     sample = getRandomNum(data, sample_size)
     return statistics.mode(sample)