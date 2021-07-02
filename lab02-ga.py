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
    binary_power = 0

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
            binary_number = gray[0]

        else:
            if gray[index] != binary_number[index - 1]:
                binary_number += "1"
            else:
                binary_number += "0"

    print("Binary number: " + binary_number)

    # convert to decimal
    for digit in binary_number[::-1]:
        if(digit == '1'):
            value = value + pow(2, binary_power)

        binary_power += 1

    return value


# Population Initialization:
# generates the first generation randomly based on the population size
# and the range of the value of each chromosome
def generatePopulation(pop_size, pop_min, pop_max):
    population = []

    # create a chromosome population of size pop_size with each value
    # between pop_min and pop_max
    for chromosome_index in range(pop_size):
        population.append(random.randrange(pop_min, pop_max + 1))

    return population


# Fitness Calculation
# calculates the fitness of a chromosome from the decimal value of the chromosome
def calculateFitness(value):
    # get number of squares that can be cut from paper with given square dimensions
    # assume 20cm x 15cm
    dim1 = 20
    dim2 = 15

    return (dim1 * dim2) // (value ** 2)    # just get integer value will do


# Parent Selection
def selectParents(chromosomes, pop_size):
    parent_pairs = []
    for iter in range(pop_size // 2):
        chromosome_pair = []
        first_chromosome_index = random.randrange(0, len(chromosomes))
        second_chromosome_index = first_chromosome_index
        while second_chromosome_index == first_chromosome_index:
            second_chromosome_index = random.randrange(0, len(chromosomes))

        chromosome_pair.append(chromosomes[first_chromosome_index])
        chromosome_pair.append(chromosomes[second_chromosome_index])

        # append new chromosome pair to parent_pair
        parent_pairs.append(chromosome_pair)

    return parent_pairs


# Crossover
# performs crossover on a parent pair to perform one-point crossover to produce
# a pair of offspring
def crossover(parents):
    offsprings = []

    return offsprings


if __name__ == "__main__":
    pop_size = 10
    pop_min = 1
    pop_max = 10
    curr_iter = 0
    max_iter = 100
    min_overalldistance = 0.5
    p_mutation = 0.05

    # initialize population
    population = generatePopulation(pop_size, pop_min, pop_max)
    print("Chromosome Population:", population)
