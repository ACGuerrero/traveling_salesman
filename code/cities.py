import json

# Define the cities data
cities_data = {
  "cities": [
    {
      "name": "Strasbourg",
      "latitude": 48.5734,
      "longitude": 7.7521
    },
    {
      "name": "Nancy",
      "latitude": 48.6921,
      "longitude": 6.1844
    },
    {
      "name": "Paris",
      "latitude": 48.8566,
      "longitude": 2.3522
    },
    {
      "name": "Mulhouse",
      "latitude": 47.7508,
      "longitude": 7.3359
    },
    {
      "name": "Dijon",
      "latitude": 47.322,
      "longitude": 5.0415
    },
    {
      "name": "Besancon",
      "latitude": 47.238,
      "longitude": 6.0244
    },
    {
      "name": "New York",
      "latitude": 40.7128,
      "longitude": -74.006
    },
    {
      "name": "London",
      "latitude": 51.5099,
      "longitude": -0.118
    },
    {
      "name": "Tokyo",
      "latitude": 35.6895,
      "longitude": 139.6917
    },
    {
      "name": "Sydney",
      "latitude": -33.8688,
      "longitude": 151.2093
    },
    {
      "name": "Mumbai",
      "latitude": 19.076,
      "longitude": 72.8777
    },
    {
      "name": "Madrid",
      "latitude": 40.4168,
      "longitude": -3.7038
    },
    {
      "name": "Athens",
      "latitude": 37.9838,
      "longitude": 23.7275
    },
    {
      "name": "Helsinki",
      "latitude": 60.1695,
      "longitude": 24.9354
    },
    {
      "name": "Beyrouth",
      "latitude": 33.8886,
      "longitude": 35.4955
    },
    {
      "name": "New Delhi",
      "latitude": 28.6139,
      "longitude": 77.209
    },
    {
      "name": "Bangkok",
      "latitude": 13.7563,
      "longitude": 100.5018
    },
    {
      "name": "Beijing",
      "latitude": 39.9042,
      "longitude": 116.4074
    },
    {
      "name": "Seoul",
      "latitude": 37.5665,
      "longitude": 126.978
    },
    {
      "name": "Sidney",
      "latitude": -33.8688,
      "longitude": 151.2093
    },
    {
      "name": "Buenos Aires",
      "latitude": -34.6118,
      "longitude": -58.4173
    },
    {
      "name": "Brasilia",
      "latitude": -15.7801,
      "longitude": -47.9292
    },
    {
      "name": "Caracas",
      "latitude": 10.4806,
      "longitude": -66.9036
    },
    {
      "name": "Mexico City",
      "latitude": 19.4326,
      "longitude": -99.1332
    },
    {
      "name": "Chicago",
      "latitude": 41.8781,
      "longitude": -87.6298
    },
    {
      "name": "Quebec",
      "latitude": 46.8139,
      "longitude": -71.208
    },
    {
      "name": "Reykjavik",
      "latitude": 64.1466,
      "longitude": -21.9426
    }
  ]
}

cities_fr = {'cities': cities_data["cities"][0:6]}

# Export the cities data to a JSON file
with open('data/cities.json', 'w') as export_file:
    json.dump(cities_data, export_file, indent=2)

with open('data/citiesfr.json', 'w') as export_file:
    json.dump(cities_fr, export_file, indent=2)

print("Cities exported to 'cities.json'")