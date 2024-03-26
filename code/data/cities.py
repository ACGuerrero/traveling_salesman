import json
import numpy as np

cities_data = {
  "cities": [
    {
      "name": "Strasbourg",
      "latitude": 48.5734,
      "longitude": 7.7521,
            "country": "France",
            "continent": "Europe"
    },
    {
      "name": "Nancy",
      "latitude": 48.6921,
      "longitude": 6.1844,
            "country": "France",
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
      "name": "Mulhouse",
      "latitude": 47.7508,
      "longitude": 7.3359,
            "country": "France",
            "continent": "Europe"
    },
    {
      "name": "Dijon",
      "latitude": 47.322,
      "longitude": 5.0415,
            "country": "France",
            "continent": "Europe"
    },
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
      "name": "Caracas",
      "latitude": 10.4806,
      "longitude": -66.9036,
      "country": "Venezuela",
      "continent": "South America"
    },
    {
            "name": "Tokyo",
            "latitude": 35.6895,
            "longitude": 139.6917,
            "country": "Japan",
            "continent": "Asia"
        },
        {
            "name": "Sydney",
            "latitude": -33.8688,
            "longitude": 151.2093,
            "country": "Australia",
            "continent": "Oceania"
        },
        {
            "name": "Rio de Janeiro",
            "latitude": -22.9068,
            "longitude": -43.1729,
            "country": "Brazil",
            "continent": "South America"
        },
        {
            "name": "Moscow",
            "latitude": 55.7558,
            "longitude": 37.6176,
            "country": "Russia",
            "continent": "Europe"
        },
        {
            "name": "Cairo",
            "latitude": 30.0444,
            "longitude": 31.2357,
            "country": "Egypt",
            "continent": "Africa"
        },
        {
            "name": "Los Angeles",
            "latitude": 34.0522,
            "longitude": -118.2437,
            "country": "United States",
            "continent": "North America"
        },
        {
            "name": "Mumbai",
            "latitude": 19.076,
            "longitude": 72.8777,
            "country": "India",
            "continent": "Asia"
        },
        {
            "name": "London",
            "latitude": 51.5074,
            "longitude": -0.1278,
            "country": "United Kingdom",
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
            "name": "Dubai",
            "latitude": 25.276987,
            "longitude": 55.296249,
            "country": "United Arab Emirates",
            "continent": "Asia"
        },
        {
            "name": "Singapore",
            "latitude": 1.3521,
            "longitude": 103.8198,
            "country": "Singapore",
            "continent": "Asia"
        },
        {
            "name": "Rome",
            "latitude": 41.9028,
            "longitude": 12.4964,
            "country": "Italy",
            "continent": "Europe"
        },
        {
            "name": "Toronto",
            "latitude": 43.65107,
            "longitude": -79.347015,
            "country": "Canada",
            "continent": "North America"
        },
        {
            "name": "Buenos Aires",
            "latitude": -34.6037,
            "longitude": -58.3816,
            "country": "Argentina",
            "continent": "South America"
        },
        {
            "name": "Seoul",
            "latitude": 37.5665,
            "longitude": 126.978,
            "country": "South Korea",
            "continent": "Asia"
        },
        {
            "name": "Berlin",
            "latitude": 52.5200,
            "longitude": 13.4050,
            "country": "Germany",
            "continent": "Europe"
        },
        {
            "name": "São Paulo",
            "latitude": -23.5505,
            "longitude": -46.6333,
            "country": "Brazil",
            "continent": "South America"
        },
        {
            "name": "Bangkok",
            "latitude": 13.7563,
            "longitude": 100.5018,
            "country": "Thailand",
            "continent": "Asia"
        },
        {
            "name": "Sydney",
            "latitude": -33.8688,
            "longitude": 151.2093,
            "country": "Australia",
            "continent": "Oceania"
        },
        {
            "name": "Amsterdam",
            "latitude": 52.3676,
            "longitude": 4.9041,
            "country": "Netherlands",
            "continent": "Europe"
        },
        {
            "name": "Istanbul",
            "latitude": 41.0082,
            "longitude": 28.9784,
            "country": "Turkey",
            "continent": "Asia"
        },
        {
            "name": "Lima",
            "latitude": -12.0464,
            "longitude": -77.0428,
            "country": "Peru",
            "continent": "South America"
        },
        {
            "name": "Stockholm",
            "latitude": 59.3293,
            "longitude": 18.0686,
            "country": "Sweden",
            "continent": "Europe"
        },
        {
            "name": "Dublin",
            "latitude": 53.3498,
            "longitude": -6.2603,
            "country": "Ireland",
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
            "name": "Cape Town",
            "latitude": -33.9249,
            "longitude": 18.4241,
            "country": "South Africa",
            "continent": "Africa"
        },
        {
            "name": "Hanoi",
            "latitude": 21.0285,
            "longitude": 105.8542,
            "country": "Vietnam",
            "continent": "Asia"
        },
        {
            "name": "Oslo",
            "latitude": 59.9139,
            "longitude": 10.7522,
            "country": "Norway",
            "continent": "Europe"
        },
        {
            "name": "Auckland",
            "latitude": -36.8485,
            "longitude": 174.7633,
            "country": "New Zealand",
            "continent": "Oceania"
        },
                {
            "name": "Vienna",
            "latitude": 48.2082,
            "longitude": 16.3738,
            "country": "Austria",
            "continent": "Europe"
        },
        {
            "name": "Copenhagen",
            "latitude": 55.6761,
            "longitude": 12.5683,
            "country": "Denmark",
            "continent": "Europe"
        },
        {
            "name": "Helsinki",
            "latitude": 60.1695,
            "longitude": 24.9354,
            "country": "Finland",
            "continent": "Europe"
        },
        {
            "name": "Seville",
            "latitude": 37.3886,
            "longitude": -5.9823,
            "country": "Spain",
            "continent": "Europe"
        },
        {
            "name": "Krakow",
            "latitude": 50.0647,
            "longitude": 19.9450,
            "country": "Poland",
            "continent": "Europe"
        },
        {
            "name": "Bangalore",
            "latitude": 12.9716,
            "longitude": 77.5946,
            "country": "India",
            "continent": "Asia"
        },
        {
            "name": "Budapest",
            "latitude": 47.4979,
            "longitude": 19.0402,
            "country": "Hungary",
            "continent": "Europe"
        },
        {
            "name": "Lisbon",
            "latitude": 38.7223,
            "longitude": -9.1393,
            "country": "Portugal",
            "continent": "Europe"
        },
        {
            "name": "Edinburgh",
            "latitude": 55.9533,
            "longitude": -3.1883,
            "country": "United Kingdom",
            "continent": "Europe"
        },
        {
            "name": "Kyoto",
            "latitude": 35.0116,
            "longitude": 135.7681,
            "country": "Japan",
            "continent": "Asia"
        }
  ]
}
if __name__ == '__main__':
    # Shuffle the list of cities
    np.random.shuffle(cities_data["cities"])

    # Export the cities data to a JSON file
    with open('cities.json', 'w') as export_file:
        json.dump(cities_data, export_file, indent=2)
    print("Cities exported to 'cities.json'")