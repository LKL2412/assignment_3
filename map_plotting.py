import city_country_csv_reader
from locations import create_example_countries_and_cities
from trip import Trip, create_example_trips
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def plot_trip(trip: Trip, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots a trip on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.
    """

    city = [trip.departure]
    for cityy in trip.next_city:
        city.append(cityy)

    #detertime which part to zoom on map
    max_distance_countries = (-1, None, None) #distance, city 1, city 2
    for i in range(len(city)):
        for j in range(i + 1, len(city)):
            distance = city[i].distance(city[j])
            if distance > max_distance_countries[0]:
                max_distance_countries = (distance, city[i], city[j])

    coordinates = [0, 0, 0, 0] #longitude1, longitude2, latitude1, latitude2
    coordinates[0] = min(max_distance_countries[1].longitude,max_distance_countries[2].longitude) - 5
    coordinates[1] = max(max_distance_countries[1].longitude,max_distance_countries[2].longitude) + 5
    coordinates[2] = min(max_distance_countries[1].latitude, max_distance_countries[2].latitude)

    # setup Lambert Conformal basemap.
    m = Basemap()
    #width=12000000, height=9000000, projection = 'lcc',lat_1=80,lat_2=20,lat_0=10,lon_0=50.

    # draw coastlines.
    m.drawcoastlines()

    #draw the lines connecting two cities
    for index in range(len(city) - 1):
        m.drawgreatcircle(city[index].longitude, city[index].latitude, city[index + 1].longitude, city[index + 1].latitude, linewidth=line_width, color=colour)

    #picture file name
    pic_name = 'map'
    for cityy in city:
        pic_name += '_'
        pic_name += cityy.name
    pic_name += '.png'
    plt.savefig(pic_name)


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    create_example_countries_and_cities()

    trips = create_example_trips()

    for trip in trips:
        plot_trip(trip)
