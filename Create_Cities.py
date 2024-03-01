import numpy as np
import matplotlib.pyplot as plt
import random



"""
Class Summary:

The RandomCitiesList class is designed to generate random city locations, calculate distances between cities, create a distance matrix, and plot cities on a scatter plot.

Attributes:

cities: A list containing the coordinates of generated cities.
num_cities: The number of cities to generate (default is 10).
x_range: A tuple specifying the range of x-coordinates for city generation (default is (0, 100)).
y_range: A tuple specifying the range of y-coordinates for city generation (default is (0, 100)).
random_state: The seed used for random number generation (default is 42).
Methods:

set_settings(num_cities, x_range, y_range, random_state): Sets the parameters for generating cities.
generate_random_cities(): Generates random city locations based on the specified settings.
generate_random_city_locations(num_cities, x_range, y_range, random_state=42): Generates random city locations within the specified ranges.
calculate_distance(city1, city2): Calculates the Euclidean distance between two cities.
create_distance_matrix(cities): Creates a distance matrix where each element represents the distance between two cities.
plot_cities(cities, home_city=None): Plots the generated cities on a scatter plot, with an option to highlight a home city.

"""
class RandomCitiesList:
    def __init__(self):
        self.cities = None
        self.home_city = None
        self.num_cities = 10
        self.x_range = (0, 100)
        self.y_range = (0, 100)
        self.random_state = 42

    def set_settings(self, num_cities, x_range, y_range, random_state):
        self.num_cities = num_cities
        self.x_range = x_range
        self.y_range = y_range
        self.random_state = random_state

    def set_random_state(self, random_state):
        self.random_state = random_state


    #Function to output Random Cities List
    def generate_random_cities(self):
        self.cities = self.generate_random_city_locations(self.num_cities, self.x_range,
                                       self.y_range)

    # Function to generate random city locations
    def generate_random_city_locations(self, num_cities, x_range, y_range):
        random.seed(self.random_state)
        cities = []
        for i in range(num_cities):
            x = random.randint(*x_range)
            y = random.randint(*y_range)
            city = {'x': x, 'y': y, 'index': i}
            cities.append(city)
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
    def plot_cities(self, cities):
        plt.figure(figsize=(8, 6))
        x_coords, y_coords, index = zip(*[(city['x'], city['y'], city['index']) for city in cities])
        plt.scatter(x_coords, y_coords, color='blue')
        for i in range(len(cities)):
            # +1/-3 after coordinates for offset
            plt.text(x_coords[i] + 1, y_coords[i] - 3, str(i), fontsize=12)  # Label each city with its index
        plt.title('Cities')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.show()

    def plot_route(self, route):
        plt.figure(figsize=(8, 6))
        x_coords, y_coords, index = zip(*[(city['x'], city['y'], city['index']) for city in route])
        plt.plot(x_coords, y_coords, color='blue')
        for i in range(len(route)):
            # +1/-3 after coordinates for offset
            plt.text(x_coords[i] + 1, y_coords[i] - 3, str(i), fontsize=12)  # Label each city with its index
        plt.title('Cities')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.show()

# # Create an instance of the RandomCitiesList class
# cities = RandomCitiesList()
#
# # Set random state
# cities.set_random_state(41)
#
# # Generate random cities
# cities.generate_random_cities()
#
# # Plot the cities
# cities.plot_cities(cities.cities)