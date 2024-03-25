import json
import numpy as np

cities_data = {
  "cities": [
    {
      "name": "Besancon",
      "latitude": 47.238,
      "longitude": 6.0244,
      "country": "France",
      "continent": "Europe"
    },
    {
      "name": "New Delhi",
      "latitude": 28.6139,
      "longitude": 77.209,
      "country": "India",
      "continent": "Asia"
    },
    {
      "name": "Quebec",
      "latitude": 46.8139,
      "longitude": -71.208,
      "country": "Canada",
      "continent": "North America"
    },
    {
      "name": "Nancy",
      "latitude": 48.6921,
      "longitude": 6.1844,
      "country": "France",
      "continent": "Europe"
    },
    {
      "name": "Caracas",
      "latitude": 10.4806,
      "longitude": -66.9036,
      "country": "Venezuela",
      "continent": "South America"
    },
    {
      "name": "Dijon",
      "latitude": 47.322,
      "longitude": 5.0415,
      "country": "France",
      "continent": "Europe"
    },
    {
      "name": "Athens",
      "latitude": 37.9838,
      "longitude": 23.7275,
      "country": "Greece",
      "continent": "Europe"
    },
    {
      "name": "Paris",
      "latitude": 48.8566,
      "longitude": 2.3522,
      "country": "France",
      "continent": "Europe"
    },
    {
      "name": "Mexico City",
      "latitude": 19.4326,
      "longitude": -99.1332,
      "country": "Mexico",
      "continent": "North America"
    },
    {
      "name": "Buenos Aires",
      "latitude": -34.6118,
      "longitude": -58.4173,
      "country": "Argentina",
      "continent": "South America"
    },
    {
      "name": "Chicago",
      "latitude": 41.8781,
      "longitude": -87.6298,
      "country": "United States",
      "continent": "North America"
    },
    {
      "name": "Bangkok",
      "latitude": 13.7563,
      "longitude": 100.5018,
      "country": "Thailand",
      "continent": "Asia"
    },
    {
      "name": "Mulhouse",
      "latitude": 47.7508,
      "longitude": 7.3359,
      "country": "France",
      "continent": "Europe"
    },
    {
      "name": "New York",
      "latitude": 40.7128,
      "longitude": -74.006,
      "country": "United States",
      "continent": "North America"
    },
    {
      "name": "Helsinki",
      "latitude": 60.1695,
      "longitude": 24.9354,
      "country": "Finland",
      "continent": "Europe"
    },
    {
      "name": "Madrid",
      "latitude": 40.4168,
      "longitude": -3.7038,
      "country": "Spain",
      "continent": "Europe"
    },
    {
      "name": "Beijing",
      "latitude": 39.9042,
      "longitude": 116.4074,
      "country": "China",
      "continent": "Asia"
    },
    {
      "name": "Reykjavik",
      "latitude": 64.1466,
      "longitude": -21.9426,
      "country": "Iceland",
      "continent": "Europe"
    },
    {
      "name": "Seoul",
      "latitude": 37.5665,
      "longitude": 126.978,
      "country": "South Korea",
      "continent": "Asia"
    },
    {
      "name": "Brasilia",
      "latitude": -15.7801,
      "longitude": -47.9292,
      "country": "Brazil",
      "continent": "South America"
    },
    {
      "name": "Sidney",
      "latitude": -33.8688,
      "longitude": 151.2093,
      "country": "Australia",
      "continent": "Oceania"
    },
    {
      "name": "Sydney",
      "latitude": -33.8688,
      "longitude": 151.2093,
      "country": "Australia",
      "continent": "Oceania"
    },
    {
      "name": "London",
      "latitude": 51.5099,
      "longitude": -0.118,
      "country": "United Kingdom",
      "continent": "Europe"
    },
    {
      "name": "Beyrouth",
      "latitude": 33.8886,
      "longitude": 35.4955,
      "country": "Lebanon",
      "continent": "Asia"
    },
    {
      "name": "Tokyo",
      "latitude": 35.6895,
      "longitude": 139.6917,
      "country": "Japan",
      "continent": "Asia"
    },
    {
      "name": "Strasbourg",
      "latitude": 48.5734,
      "longitude": 7.7521,
      "country": "France",
      "continent": "Europe"
    },
    {
      "name": "Mumbai",
      "latitude": 19.076,
      "longitude": 72.8777,
      "country": "India",
      "continent": "Asia"
    }
  ]
}
if __name__ == '__main__':
    # Shuffle the list of cities
    np.random.shuffle(cities_data["cities"])

    # Export the cities data to a JSON file
    with open('data/cities.json', 'w') as export_file:
        json.dump(cities_data, export_file, indent=2)
    print("Cities exported to 'cities.json'")