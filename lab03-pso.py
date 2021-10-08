class Particle:
    def __init__(self, position=0, velocity=0):
        self.position = position
        self.velocity = velocity
        self.best_position = position


def fit_fcn(position):
    fitness = (100 + position) * (50 + position) * position * \
        (position - 20) * (position - 60) * (position - 100)

    return fitness


def initialize_particles(n_ptc, position_limits):
    # position_limits is a list of two values. The first value is the lower boundary and the second value is the upper boundary.


if __name__ == "__main__":
    alpha = [0.1, 0.1]
    n_particle = 10
