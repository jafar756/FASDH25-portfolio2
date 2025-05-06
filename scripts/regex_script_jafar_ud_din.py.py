
import re
import os
import pandas as pd


def write_tsv(data, column_list, path):
    """This function converts a dictionary to a tsv file.

    It takes three arguments:
        data (dict): the dictionary
        column_list (list): a list of column names
        path (str): the path to which the tsv file will be written
    """
    
    # turn the dictionary into a list of (key, value) tuples (this is correct):
    items = list(data.items())
    # create a dataframe from the items list (this is correct):
    df = pd.DataFrame.from_records(items, columns=column_list)
    # write the dataframe to tsv:
    df.to_csv(path, sep="\t", index=False)




#path to the articles
folder = "../articles"



# load the gazetteer from the tsv file:
path = "../gazetteers/geonames_gaza_selection.tsv"
with open(path, encoding="utf-8") as file:
    data = file.read()

# dictionaries to store findings
patterns = {} #store regex patterns for each location
frequencies = {} #total mentions across all articles
rows = data.split("\n")
#process each row in the gazetteer to build search patterns
for row in rows[1:]: #skips the header row
    cells = row.split("\t")
    ascii_name = cells[0].strip().lower() #the main place name
    if len(cells) > 5:
        all_names = [ascii_name] #store all variation of teh place name
        alternate_names = cells[5].strip() #get alternate names from the gazetteer

        if alternate_names:
        
            for name in alternate_names.split(","):
                
                all_names.append(name.strip().lower())#add cleaned alternate names
        
        escaped_names = []
        for name in all_names:
            if name:

                escaped_names.append(re.escape(name.lower())) #escape special regex characters #learned from chatgpt
        #join all names with OE (|) to match any variation in one go
        regex_pattern = "|".join(escaped_names)
        #save the regex pattern and initialize frequency counter
        patterns[ascii_name] = regex_pattern
        frequencies[ascii_name] = 0
        
        
        
    
# Dictionaries to store detailed frequency counts
monthly_frequencies = {}
mentions_per_month = {}
#loop through every article in the folder
for filename in os.listdir(folder):
    # build the file path:
    file_path = f"{folder}/{filename}"
    article_date = filename[:10] #filename is date of article
    if article_date < "2023-10-07":#skips article before 7 oct
        continue
    month = article_date[:7] #skiping the day 

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of the patterns in the text:
    
    text_lower = text.lower()
    #search for place names in the article using regex patterns
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text_lower) #find all the matches
        n_matches = len(matches) #count how many times the place is mentioned
        if n_matches > 0:
            frequencies[name] += n_matches #update overall frequency
            #track monthly frequencing using(place, month) as key
            key = (name, month)
            if key not in monthly_frequencies:
                monthly_frequencies[key] = 0
            monthly_frequencies[key] += n_matches
             #track mentions per month per place
            if name not in mentions_per_month:
                mentions_per_month[name] = {}
            if month not in mentions_per_month[name]:
                mentions_per_month[name][month] = 0
            mentions_per_month[name][month] += n_matches
            
       
# print the frequency of each pattern:
for name, count in frequencies.items():
    if count >= 1:
        print(f"found {name} {count} times: {mentions_per_month[name]}")

# call the function to write your tsv file:
monthly_rows = []
for (name, month), freq in monthly_frequencies.items():
    monthly_rows.append((name, month, freq))
    #convert the list into a dataframe and saving it 
monthly_df = pd.DataFrame(monthly_rows, columns=["asciiname", "month", "frequency"])
monthly_df.to_csv("monthly_frequencies.tsv", sep="\t", index=False)

