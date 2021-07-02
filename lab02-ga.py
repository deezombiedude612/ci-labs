import random


# converts decimal value to gray code equivalent
def value2gray(value):
    """
    Reference: https://youtu.be/cbmh1DPPQyI
    First digit in gray code is equal to binary number's first digit.
    Subsequent gray code digits are determined based on comparing every 
    consequent pair of binary digits.

    If binary digit in position (i) and position (i - 1) are
    -> similar, next gray code digit is 0.
    -> different, next binary digit is 1.
    """
    return str(bin(value ^ (value >> 1)))[2:]


# convert gray code to decimal equivalent
def gray2value(gray):
    value = 0
    binaryPower = 0

    """
    Reference: https://youtu.be/cbmh1DPPQyI
    First digit in binary number is equal to gray code's first digit.
    
    Subsequent binary digits are determined based on comparing the 
    digit in gray code at position (i) and digit in binary number at 
    position (i - 1).
    -> If similar, next binary digit is 0.
    -> If different, next binary digit is 1.
    """

    # obtain binary number
    for index in range(len(gray)):
        if(index == 0):
            binaryNumber = gray[0]

        else:
            if gray[index] != binaryNumber[index - 1]:
                binaryNumber += "1"
            else:
                binaryNumber += "0"

    print("Binary number: " + binaryNumber)

    # convert to decimal
    for digit in binaryNumber[::-1]:
        if(digit == '1'):
            value = value + pow(2, binaryPower)

        binaryPower += 1

    return value


# Population Initialization
# this function generates the first generation randomly based on the population size and the range of the value of each chromosome
def generatePopulation(pop_size, pop_min, pop_max):
    population = []

    # create a chromosome population of size pop_size with each value between pop_min and pop_max
    for chromosomeIndex in range(pop_size):
        population.append(random.randrange(pop_min, pop_max + 1))

    return population


# Fitness Calculation
# this function calculates the fitness of a chromosome from the decimal value of the chromosome
def calculateFitness(value):
    # get number of squares that can be cut from paper with given square dimensions?

    return fitness


if __name__ == "__main__":
    # print(value2gray(10))      # 1111
    # print(gray2value("1001"))  # 14

    pop_size = 10
    pop_min = 1
    pop_max = 10
    curr_iter = 0
    max_iter = 100
    min_overalldistance = 0.5
    p_mutation = 0.05

    # initialize population
    # print(generatePopulation(8, 0, 10))
    population = generatePopulation(pop_size, pop_min, pop_max)
    print("Chromosome Population:", population)
