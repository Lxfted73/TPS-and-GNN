from Create_Cities import RandomCitiesList
from Brute_Force_TSP import BruteForceTSP
import time
# Create an instance of the RandomCitiesList class
cities = RandomCitiesList()

# Set random state
cities.set_random_state(44)
cities.set_num_cities(5)

# Generate random cities
cities.generate_random_cities()

# Plot the cities
cities.plot_cities(cities.cities)

# Create TSP solver instance
brute_force_tsp_solver = BruteForceTSP(cities.cities)

# Record the start time
start_time = time.time()
# Solve TSP using brute force
shortest_path, min_distance = brute_force_tsp_solver.brute_force_tsp()
end_time = time.time()
# Calculate the elapsed time
elapsed_time = end_time - start_time
print("Elapsed Time:", elapsed_time, "seconds")

cities.plot_route(shortest_path)



