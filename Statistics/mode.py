import statistics
from Statistics.randomNum import getRandomNum

   def mmode(data):
        sample = getRandomNum(data)
        return statistics.mode(sample)