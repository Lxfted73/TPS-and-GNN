from Create_Cities import RandomCitiesList
from Brute_Force_TSP import BruteForceTSP

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