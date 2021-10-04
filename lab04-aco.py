# Coordinates of each town
location_list = [
    [75, 125, 'Arad'],
    [100, 75, 'Zerind'],
    [125, 25, 'Oradea'],
    [265, 175, 'Sibiu'],
    [425, 175, 'Fagaras'],
    [320, 230, 'Rimnicu Vilcea'],
    [475, 310, 'Pitesti'],
    [350, 465, 'Craiova'],
    [185, 450, 'Drobeta'],
    [190, 390, 'Mehadia'],
    [185, 335, 'Lugoj'],
    [85, 280, 'Timisoara'],
    [640, 390, 'Bucharest'],
    [575, 485, 'Giurgiu'],
    [745, 340, 'Urziceni'],
    [875, 340, 'Hirsova'],
    [935, 440, 'Eforie'],
    [850, 225, 'Vaslui'],
    [760, 120, 'Iasi'],
    [625, 60, 'Neamt']
]

# Travel cost between cities
step_cost = [
    ['Arad', 'Zerind', 75],
    ['Zerind', 'Oradea', 71],
    ['Oradea', 'Sibiu', 151],
    ['Sibiu', 'Arad', 140],
    ['Sibiu', 'Fagaras', 99],
    ['Sibiu', 'Rimnicu Vilcea', 80],
    ['Fagaras', 'Bucharest', 211],
    ['Bucharest', 'Giurgiu', 90],
    ['Bucharest', 'Pitesti', 101],
    ['Pitesti', 'Rimnicu Vilcea', 97],
    ['Rimnicu Vilcea', 'Craiova', 146],
    ['Craiova', 'Pitesti', 138],
    ['Craiova', 'Drobeta', 120],
    ['Drobeta', 'Mehadia', 75],
    ['Mehadia', 'Lugoj', 70],
    ['Lugoj', 'Timisoara', 111],
    ['Arad', 'Timisoara', 118],
    ['Bucharest', 'Urziceni', 85],
    ['Urziceni', 'Vaslui', 142],
    ['Vaslui', 'Iasi', 92],
    ['Iasi', 'Neamt', 87],
    ['Urziceni', 'Hirsova', 98],
    ['Hirsova', 'Eforie', 86]
]


class City:
    def __init__(self, name):
        self.name = name
        self.roads = []
        self.coordinates = []

    def set_coordinates(self, coordinates):
        self.coordinates = coordinates

    def add_road(self, road):
        if road not in self.roads:
            self.roads.append(road)


class Road:
    def __init__(self, connected_cities, cost, pheromone=0):
        self.connected_cities = connected_cities
        self.cost = cost
        self.pheromone = pheromone

    def set_pheromone(self, pheromone):
        self.pheromone = pheromone


class Ant:
    def __init__(self):
        self.cities = []  # cities the ant passes through, in sequence
        self.path = []  # roads the ant uses, in sequence


if __name__ == "__main__":
    # Construct list of City objects
    cities = {}
    for coord1, coord2, name in location_list:
        cities[name] = City(name)
        cities[name].set_coordinates([coord1, coord2])

    # Construct list of Road objects
    roads = []
    for city1, city2, cost in step_cost:
        road = Road([cities[city1], cities[city2]], cost)
        cities[city1].add_road(road)
        cities[city2].add_road(road)
        roads.append(road)

    # Define origin and destination classes
    origin = cities['Arad']
    destination = cities['Bucharest']

    n_ant = 10
    alpha = 1
    rho = 0.1

    # Set initial pheromone of each road to 0.01
    initial_pheromone = 0.01
    for road in roads:
        road.set_pheromone(initial_pheromone)

    # Initiate n_ant ants
    ants = [Ant() for _ in range(n_ant)]
