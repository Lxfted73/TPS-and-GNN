from Create_Cities import RandomCitiesList

# Create an instance of the RandomCitiesList class
cities = RandomCitiesList()

cities.set_random_state(41)

# Generate random cities
cities.generate_random_cities()

# Plot the cities, optionally passing the home city
cities.plot_cities(cities.cities)
