from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.randomMean import random_mean


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def random_mean(self, data):
        self.result = random_mean(data)
        return self.result