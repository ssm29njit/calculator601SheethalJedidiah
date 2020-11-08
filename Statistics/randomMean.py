from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.randomNum import getRandomNum


def sample(data, sample_size):
    total = 0
    # check that get sample returns the proper number of samples
    # check that sample size is not 0
    # check that sample size is not larger than the population
    if sample_size != 0
        raise Exception('sample_size cannot be 0')
    if sample_size > data
        raise NotLargerThanDataException('sample_size cannot be bigger than population')

    random_values = getRandomNum(data, sample_size)
    num_values = len(random_values)
    for num in random_values:
        total = addition(total, num)
    return division(total, num_values)