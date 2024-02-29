import numpy as np
import matplotlib.pyplot as plt
import random

class RandomCitiesList:
    def __init__(self):
        self.cities = None
        self.num_cities = 10
        self.x_range = (0, 100)
        self.y_range = (0, 100)
        self.random_state = 42

    def set_settings(self, num_cities, x_range, y_range, random_state):
        self.num_cities = num_cities
        self.x_range = x_range
        self.y_range = y_range
        self.random_state = random_state


    #Function to output Random Cities List
    def generate_random_cities(self):
        self.cities = self.generate_random_city_locations(self.num_cities, self.x_range,
                                       self.y_range, self.random_state)

    #Function to Home City 
    def select_home_city(self, cities_list, random_state = 42):
        random.seed(random_state)
        return random.choice(cities_list)


    # Function to generate random city locations
    def generate_random_city_locations(self, num_cities, x_range, y_range, random_state = 42):
        random.seed(random_state)
        cities = []
        for _ in range(num_cities):
            x = random.randint(*x_range)
            y = random.randint(*y_range)
            cities.append((x, y))
        return cities

    # Function to calculate distance between two cities
    def calculate_distance(self, city1, city2):
        return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

    # Function to create distance matrix
    def create_distance_matrix(self, cities):
        num_cities = len(cities)
        distance_matrix = np.zeros((num_cities, num_cities))
        for i in range(num_cities):
            for j in range(num_cities):
                distance_matrix[i][j] = self.calculate_distance(self, cities[i], cities[j])
        return distance_matrix

    # Function to plot cities
    def plot_cities(self, cities, home_city=None):
        plt.figure(figsize=(8, 6))
        plt.scatter(*zip(*cities), color='blue')
        for i, (x, y) in enumerate(cities):
            plt.text(x, y, str(i), fontsize=12)  # Label each city with its index
        if home_city is not None:
            plt.scatter(home_city[0], home_city[1], color='red', marker='x', label='Home City')
        plt.title('Cities')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.show()