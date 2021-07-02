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
    gray = str(bin(value ^ (value >> 1)))[2:]
    while(len(gray) < 4):
        gray = "0" + gray

    return gray


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

    # print("Binary number: " + binary_number)

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

        first_chromosome_index = random.randrange(len(chromosomes))

        # Chromosome pair should not be asexual (i.e., not the same chromosome in pair)
        second_chromosome_index = first_chromosome_index
        while second_chromosome_index == first_chromosome_index:
            second_chromosome_index = random.randrange(len(chromosomes))

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

    # Assume we are only dealing with values less than 16 (only 4-digit gray codes)
    for iter1 in range(2):
        child = ""
        for iter2 in range(4):
            child += value2gray(parents[random.randrange(len(parents))])[iter2]

        offsprings.append(gray2value(child))

    return offsprings


# Mutation
# mutates each gene of a chromosome based on the mutation probability
def mutate(chromosome, p_mutation):
    chromosome_gray = value2gray(chromosome)
    mutated = ""

    for iter in range(4):
        if p_mutation > random.uniform(0, 1):  # uniform distribution used
            if chromosome_gray[iter] == "0":
                mutated += "1"
            else:
                mutated += "0"

        else:
            mutated += chromosome_gray[iter]

    return gray2value(mutated)


# takes the input of the current population and returns the overall distance among
# fitnesses of all chromosomes
def findOverallDistance(chromosomes):
    total = 0

    for iter in range(len(chromosomes)):
        total += chromosomes[iter]

    return total / len(chromosomes)


if __name__ == "__main__":
    pop_size = 10
    pop_min = 1   # 1 cm
    pop_max = 10  # 10 cm
    curr_iter = 0
    max_iter = 100
    min_overalldistance = 0.5
    p_mutation = 0.05

    # initialize population
    population = []
    population.append(generatePopulation(pop_size, pop_min, pop_max))
    print("Chromosome Population:", population)

    while (curr_iter < max_iter and findOverallDistance(population[-1]) > min_overalldistance):
        curr_iter += 1

        # select parent pairs
        parents = selectParents(population[-1], len(population[-1]))

        # perform crossover
        offsprings = []
        for p in parents:
            new_offsprings = crossover(p)
            for o in new_offsprings:
                offsprings.append(o)

        # perform mutation
        mutated = [mutate(offspring, p_mutation) for offspring in offsprings]

        # update current population
        population.append(mutated)
