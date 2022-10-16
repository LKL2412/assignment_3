import city_country_csv_reader
from locations import City, Country
from trip import Trip
from vehicles import Vehicle, create_example_vehicles
import networkx as nx
import math


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Trip:
    """
    Returns a shortest path between two cities for a given vehicle,
    or None if there is no path.
    """
    graph = nx.Graph()

    for city in City.cities.values():
        for city2 in City.cities.values():
            travel_time = vehicle.compute_travel_time(city, city2)
            if travel_time != math.inf:
                graph.add_edge(city, city2, weight = travel_time)
    
    shortest_trip = nx.shortest_path(graph, from_city, to_city, weight="weight")
    trip = Trip(from_city)
    for path in shortest_trip[1:]:
        trip.add_next_city(path)
    
    return trip
    


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    vehicles = create_example_vehicles()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    for vehicle in vehicles:
        print("The shortest path for {} from {} to {} is {}".format(vehicle, melbourne, tokyo, find_shortest_path(vehicle, melbourne, tokyo)))
