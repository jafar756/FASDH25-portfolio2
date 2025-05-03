
# Input: articles folder and gazetter file

# Import libraties:


# re- for regular expression matching
# os - for reading article filenames from the folder
# pandas as pd - for saving the final results in TSV format
import re
import os
import pandas as pd

# defining the folder that contains the articles; and the path to the gazetter file
folder = '../articles'

# Loading the gazetter file (TSV format) and read it into Python
path = "../gazetteers/geonames_gaza_selection.tsv"
with open(path, encoding="utf-8") as file:
    data = file.read()
                
    
# Extract place names fromm the gazetter


# Create a dictionary to store the frequency count for each place name (initializing to 0)
patterns ={}
rows = data.split('\n')
for row in rows:
        cells = row.split("\t")
        ascii_name = cells[0]
        alternate_names = cells[0]
        patterns[ascii_name] = 0
#count the number of times each place name is found in the articles 
for filename in os.listdir(folder):
     
    #build the file path
    file_path = f"{folder}/{filename}"
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    #load the articles (text file) into python:
    

    #find all the occurences of the patterns in the text:
    for pattern in patterns:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        # add the number of times it was found to the total frequency:
        patterns[pattern] += n_matches
    print(patterns)
        


# Looping through all the article files in the folder:
#for fiename in os.listdir(folder):
   
   # Skiping articles written  before October 7, 2023 (start of the Gaza war)
    #if filename < "2023-10-07":
        #continue
   # loading the article content into python
#create a veriable for month
     #month = "_".join(filename.split("_")[:2])

     #with open(os.path.join(folder, filename), encoding="utf-8") as file:
         #text = file.read()
  # for each place name:
     # Using regex to find all matches of that place name in the article text
     # counting how many times it was found
     # Adding that number to the place name's total frequency in the dictionary/ per month

# printing the frequency of each place

# call the function to write the dictionary results to a TSV file
# TSV will have three columns: place name and frequency
#columns = ["asciiname", "frequency"]
#tsv_filename = "frequencies.tsv"
#write_tsv(patterns, columns, tsv_filename)   











































#output: count of how many times each place from the gazetter is methioned in the articles each month since 7 october 2023
