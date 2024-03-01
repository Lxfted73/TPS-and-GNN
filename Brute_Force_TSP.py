import itertools
import numpy as np
from Create_Cities import  RandomCitiesList

class BruteForceTSP:
    def __init__(self, cities):
        self.cities = cities

    def calculate_distance(self, city1, city2):
        """Calculate Euclidean distance between two cities."""
        return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** 0.5

    def total_distance(self, path):
        """Calculate the total distance of a path."""
        total = 0
        for i in range(len(path)-1):
            city1 = (path[i]['x'], path[i]['y'])
            city2 = (path[i+1]['x'], path[i+1]['y'])
            total += self.calculate_distance(city1, city2)
        return total

    def brute_force_tsp(self):
        """Solve the TSP using brute force."""
        num_cities = len(self.cities)
        shortest_path = None
        min_distance = float('inf')
        start_city_index = 0
        start_city = self.cities[start_city_index]
        for perm_indices in itertools.permutations(range(num_cities)):
            print("Perm_Indices", perm_indices)
            perm = [self.cities[i] for i in perm_indices]
            perm = perm[start_city_index:] + perm[:start_city_index]
            if perm[0]['index'] == start_city_index:
                distance = self.total_distance(perm)
                if distance < min_distance:
                    min_distance = distance
                    shortest_path = perm
                    #print("Shortest Path: ", shortest_path)
            else:
                break
        shortest_path.append(start_city)
        return shortest_path, min_distance

# Create an instance of the RandomCitiesList class
cities = RandomCitiesList()

# Set random state
cities.set_random_state(41)

# Generate random cities
cities.generate_random_cities()

# Plot the cities
# cities.plot_cities(cities.cities)

# Create TSP solver instance
brute_force_tsp_solver = BruteForceTSP(cities.cities)

# Solve TSP using brute force
shortest_path, min_distance = brute_force_tsp_solver.brute_force_tsp()

cities.plot_route(shortest_path)
