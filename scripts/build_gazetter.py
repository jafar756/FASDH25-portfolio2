
#Firstly, import necessary libraries
import os #for file and folder path handing
import requests #making Api calls to Geonames
import time #readind and writing TSV fils


#path to the TSV file containg place names
file_path = "../gazetteers/ner_counts.tsv"

#Geonames username which is required for using API
geonames_username = "jafar_ud_din"

#Defining a function to feth place coordinates
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
  # waiting to not overload the server
  time.sleep(timeout)
  # make the API call:
  url = "http://api.geonames.org/searchJSON?"
  params = {"q": place, "username": username, "fuzzy": fuzzy, "maxRows": 1, "isNameRequired": True}
  response = requests.get(url, params=params)#send request to the API
  # convert the API response from JSON format into a dictionary:
  results = response.json()
  print(results)
  # get the first result from API response:
  try:
    result = results["geonames"][0]
    return {"latitude": result["lat"], "longitude": result["lng"]}
  except (IndexError, KeyError):
    #it there is no result , print a message and return None
    print("No results found for your API call", response.request.url)
    return None

import csv #library for reading and writing TSV files

# Create a list to load place names extracted from the tsv file
place_names = []
#open the tsv file and read each row
with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter="\t")  #reads the tsv format
    next(reader)  # Skip the header row which is name, count, etc
    for row in reader:
        place_names.append(row[0])  # Append the place name (first column) to the list

#checking that the gazetteer folder exists
os.makedirs("gazetteer", exist_ok=True)


# Get the coordinates for each place and write to a new TSV file
filename = "ner_gazetteer.tsv"
output_path = "gazetteer/NER_gazetteer.tsv"
#checking that the gazetteer folder exists
os.makedirs("gazetteer", exist_ok=True)
#write place names and their coordinates into the output file
with open(output_path, mode="w", encoding="utf-8") as outfile:
    writer = csv.writer(outfile, delimiter="\t")  # Create a CSV writer object
    # Write the header row
    writer.writerow(["name", "latitude", "longitude"])
#loop through each place and get coordinates
    for name in place_names:
        coordinates = get_coordinates(name)  # Assuming  have the get_coordinates function defined
        if coordinates:
            print("=>", coordinates)
            #write the actual coordinates
            writer.writerow([name, coordinates['latitude'], coordinates['longitude']])  # Write the data row
        else:
            print("=>", coordinates)
            #write the error 
            writer.writerow([name, "NA", "NA"])
