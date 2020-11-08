import statistics
from Statistics.randomNum import getRandomNum


def stdev(data, sample_size):
    sample = getRandomNum(data, sample_size)
    return statistics.stdev(sample)