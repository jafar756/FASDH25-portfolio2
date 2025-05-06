
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



# define which folder to use:
#Loop through the articles for data visualization
folder = "../articles"

# define the patterns we want to search:

# load the gazetteer from the tsv file:
path = "../gazetteers/geonames_gaza_selection.tsv"
with open(path, encoding="utf-8") as file:
    data = file.read()

# build a dictionary of patterns from the place names in the first column:
patterns = {}
frequencies = {}
rows = data.split("\n")
for row in rows[1:]:
    cells = row.split("\t")
    ascii_name = cells[0].strip().lower()
    if len(cells) > 5:
        all_names = [ascii_name]
        alternate_names = cells[5].strip()

        if alternate_names:
        
            for name in alternate_names.split(","):
                
                all_names.append(name.strip().lower())
        
        escaped_names = []
        for name in all_names:
            if name:

                escaped_names.append(re.escape(name.lower()))
        regex_pattern = "|".join(escaped_names)
        patterns[ascii_name] = regex_pattern
        frequencies[ascii_name] = 0
        
        
        
    
# count the number of times each pattern is found in the entire folder:
monthly_frequencies = {}
mentions_per_month = {}
for filename in os.listdir(folder):
    # build the file path:
    file_path = f"{folder}/{filename}"
    article_date = filename[:10]
    if article_date < "2023-10-07":
        continue
    month = article_date[:7]

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of the patterns in the text:
    text_lower = text.lower()
    for name, pattern in patterns.items():
        matches = re.findall(pattern, text_lower)
        n_matches = len(matches)
        if n_matches > 0:
            frequencies[name] += n_matches
            key = (name, month)
            if key not in monthly_frequencies:
                monthly_frequencies[key] = 0
            monthly_frequencies[key] += n_matches
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
monthly_df = pd.DataFrame(monthly_rows, columns=["asciiname", "month", "frequency"])
monthly_df.to_csv("monthly_frequencies.tsv", sep="\t", index=False)

