import os
import requests
import time
file_path = "../gazetteers/ner_counts.tsv"
geonames_username = "jafar_ud_din"

def get_coordinates(place, username=geonames_username, fuzzy=0, timeout=1):
  """This function gets a single set of coordinates from the geonames API.

  Args:
    place (str): the place name
    username (str): your geonames user name
    fuzzy (int): 0 = exact matching, 1 = fuzzy matching (allow similar but not exact matches)
    timeout (int): number of seconds to wait before a call to the geonames API
      (to avoid being blocked for overloading the server)

  Returns:
    dictionary: keys: latitude, longitude
  """
  # wait to not overload the server:
  time.sleep(timeout)
  # make the API call:
  url = "http://api.geonames.org/searchJSON?"
  params = {"q": place, "username": username, "fuzzy": fuzzy, "maxRows": 1, "isNameRequired": True}
  response = requests.get(url, params=params)
  # convert the response into a dictionary:
  results = response.json()
  print(results)
  # get the first result:
  try:
    result = results["geonames"][0]
    return {"latitude": result["lat"], "longitude": result["lng"]}
  except (IndexError, KeyError):
    print("No results found for your API call", response.request.url)
    return None

import csv

# Get the place names from the TSV file
place_names = []
with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter="\t")  # Create a CSV reader object
    next(reader)  # Skip the header row
    for row in reader:
        place_names.append(row[0])  # Append the place name (first column) to the list

#checking that the gazetteer folder exists
os.makedirs("gazetteer", exist_ok=True)


# Get the coordinates for each place and write to a new TSV file
filename = "ner_gazetteer.tsv"
output_path = "gazetteer/NER_gazetteer."
#checking that the gazetteer folder exists
os.makedirs("gazetteer", exist_ok=True)
with open(output_path, mode="w", encoding="utf-8") as outfile:
    writer = csv.writer(outfile, delimiter="\t")  # Create a CSV writer object
    # Write the header row
    writer.writerow(["name", "latitude", "longitude"])
    for name in place_names:
        coordinates = get_coordinates(name)  # Assuming you have the get_coordinates function defined
        if coordinates:
            print("=>", coordinates)
            writer.writerow([name, coordinates['latitude'], coordinates['longitude']])  # Write the data row
        else:
            print("=>", coordinates)
            writer.writerow([name, "NA", "NA"])
