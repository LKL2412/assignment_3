from locations import City, Country, test_example_countries_and_cities
import csv

def create_cities_countries_from_CSV(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.
    """
    content = []
    with open(path_to_csv) as csvfile:
        #read csv file into csv_reader with csv.reader
        csv_reader = csv.reader(csvfile)

        #assign first line of the csv file as the header
        headers = next(csv_reader)

        #save every content here into a list of dictionary (content)
        for row in csv_reader:
            row_data = {key: value for key, value in zip(headers, row)}
            content.append(row_data)

        #create instances for all city
        for city in content:
            City(name = city['city_ascii'], latitude = city['lat'], longitude = city['lng'], country = city['country'], capital_type = city['capital'], city_id = city['id'])
            Country(city['country'], city['iso3'])

if __name__ == "__main__":
    create_cities_countries_from_CSV("worldcities_truncated.csv")
    test_example_countries_and_cities()
