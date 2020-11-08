import statistics

from Statistics.randomNum import getRandomNum


def varianceX(data):
    sample = getRandomNum(data)
    return statistics.variance(sample)