from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Variance import varianceX
from Statistics.mode import mmode
from Statistics.randomMean import randomMean


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def random_mean(self, data):
        self.result = randoMean(data, 9)
        return self.result

    def mode(self,data):
        self.result = mmode(data)
        return self.result

    def variance(self, data):
        self.result = varianceX(data)
        return self.result
