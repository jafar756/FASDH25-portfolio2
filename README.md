# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2

## Blur 
- This project extracts place names from a **collection of historical articles using two techniques: regular expressions (regex) and Named Entity Recognition (NER)**. The extracted data is then mapped onto an interactive, animated map to visualize the frequency and distribution of these place names over time.

## Folder structure 
### ChatGpt Solution
- ner_map_chatgpt.solution
- regex_map_chatgpt solution
### Gazetteers
### Map Images 
- ner_map
- regex_map
### Output Data
- ner_counts.tsv
- regex_counts.tsv
- monthly_frequency.tsv
- NER_gazetteer
### Script 
- ner_map_rubica_shah
- regex_map_rubica_shah
- build_gazetter
- regex_script_jafar_udin_din.py
- copy_Gaza_NER2_
### articles
## 0. portfolio task - fork and clone the portfolio folder
### purpose 
- To begin our project, we first created an independent copy (a fork) of the original portfolio repository. This allowed our group to work collaboratively without affecting the main source.
### Steps 
- One member of our group (me) went to the original repository:
**https://github.com/OpenITI/FASDH25-portfolio2**
- I clicked the "Fork" button on the top right.
- This created a copy of the repository in my own GitHub account.
## 1. Document your project 
### purpose 
- This way we able to manage the project in an order that can be looked by everyone in the group, with time management through trello, code commenting and readme file. 
### Steps
- Used code commenting to know the work of code
- Used Trello for time management
- Laslty readme file to explain to other

## 2A. Use gazeteer and regex to extract places in gaza
### Purpose 
- Extracts place names in Gaza from a large corpus using a gazetteer and regex, counts their monthly mentions, and exports the results to a TSV file
### Steps 
- Loaded the Gaza gazetteer to extract place names and their alternate spellings.
- Generated flexible regex patterns to match spelling variations for each place name.
- Iterated through the corpus folder, reading each article file.
- Filtered articles by date, including only those written after the start of the 2023 Gaza war
- Then Match place names in each article using the regex patterns and count the occurrences.
- Extracted the article’s month from its filename for monthly aggregation.
- Updated a nested dictionary to store place-wise mention counts per month.
- Writen the results to a regex_counts.tsv file with columns: placename, month, and count.
## 2B Using Stanza to extract all places names from the corpus
### purpose 
- The goal of the project is to extract, clean, count and geocode all place names mentioned in the selected articles written in January 2024.  
### Steps
- Installed and uses the stanza library in collab, for NLP task. 
- Imported python libraries and language model
- downloaded the English language models and build a pipeline
- Cloned the corpus in the portfolio repo
- I extracted the place names from articles written in January 2024
- Counted the number of times place name used
- Cleaned up the duplicate names and merge
- writen the cleaned place names and their frequency counts into a tab separated values fofile for further
- Displays the content of the saved TSV file, showing the list of unique , cleaned place names and how many times each appeared in january 2024 news articles. 

## 3. Create a Gazatteer for the NER Places
### Purpose
 --Taking names from ner.counts.tsv file, which has place names and get the coordinates for those places using GeoNames API and save the information AS NER_gazetteer.tsv file.
### what the script is doing
- Reads the place names from 'ner_counts.tsv'
- uses the Geonames API(http://www.geonames.org/) for coordinates.
- prints coordinates for the place names.
- prints NA where coordinates are not found which would be manually added later.
- saves the output in a tsv file.

- the following place had not their coordinates and were manually fixed.
- names           lat            long
- Dahiyeh    33.85°             35.51°
- Shujayea     31.50056°  34.47000°                     
- Abudaqa              43.2374° 79.8782°          
- Mazzeh               33.5014°       36.2468°          
- Nairoukh    31.07°              10.51°
- Shawawra    31.69111°   35.27222                
- Beruit              33.8938°       35.5018°
- Bahaa         20.0123°          41.4686°        
- Rawaa         51.7662°          20.2562°
- Philadelphi 39.9526°           75.1652°
- Yir’On              33.0772°          35.4543

## 4A.  Map the regex-extracted placenames
### The purpose
The goal of this task is to show how often different places are mentioned in the text using method regex.
For regex, I made an animated map (regex_map.html, regex_map.png) that shows how place mentions change each month using data from regex_counts.tsv.
### steps
- Imported pandas and plotly.express to read data and create interactive maps. Installed kaleido to save maps as images.
- Loaded regex_counts.tsv (place names, frequency, and date) and ner_gazetteer.tsv (place names with latitude and longitude).
- Merged both files using the common place name so each place would have both frequency and coordinates to make the ouput more interactive.
- Removed extra spaces from column headers to avoid errors during merging.
- Converted the date column to datetime format so Python can understand and work with dates.
- Extracted month and year from the date for monthly animation.
- Adjusted display settings to show all columns clearly during process.
- Converted latitude and longitude columns to numbers because they might be read as text.
- Removed rows with missing coordinates (NaN) to avoid mapping errors.
- Used plotly.express.scatter_mapbox to create an animated map showing place name mentions by month.
- Used size and color of dots to show how often a place was mentioned.
- Applied a clean map style (carto-positron-nolabels) for better readability.
- Displayed the map in the browser.
- Saved it as regex_map.html (interactive) and regex_map.png (image).

## 4B. Map the NER-extracted placenames
### purpose:
- The goal of this task is to show how often different places are mentioned in the text using NER.
NER, I made a map (ner_map.html, ner_map.png) that shows which places were mentioned in January 2024, using ner_counts.tsv and NER_gazetteer.tsv.
-- These maps help us understand which places were talked about the most and how that changed over time or stayed the same.
### steps:
- Import pandas and plotly.express to handle data and create the map and install keldieo to save png.
-  Load ner_counts.tsv (contains place names and frequency) and ner_gazetteer.tsv (contains coordinates)
- Clean column names to prevent merge issues due to extra spaces.
- Merge both files on the common column name to combine frequencies with coordinates
- Rename columns for consistency and easier access
- Convert latitude and longitude to numeric values so they can be used for plotting
- Remove rows with missing coordinate or frequency data to avoid errors
- Create an interactive map using scatter_map to show place frequencies
- Use a simple base map style (open-street-map) that doesn't need a token
- Show the map in the browser
- Save the map as ner_map.html (interactive) and ner_map.png (image)

## comparison of maps generated from regex and ner
### Regex Map
- Extracted place names using regex.
- Focuses on one major location (likely Syria).
- Uses CARTO/plotly with a time slider.
- Color scale: Yellow to Red (high frequency = red).
- Less geographic spread.
### NER Map
- Extracted place names using Named Entity Recognition (NER).
- Shows multiple locations across the Middle East and North Africa.
- Uses Plotly or similar map.
- Color scale: Purple to Yellow (high frequency = yellow).
- Wider and richer location data
## Regex + Gazetteer
### Advantages:
Fast  for well-known place names.
You can control exactly what patterns to match.
Works well with  repetitive text (e.g., structured data).
### Disadvantages:
 Misses places with spelling variations or typos.
Hard to scale for large or diverse texts.
Requires manual updates to the gazetteer list.
 Named Entity Recognition (NER)
### Advantages:
Automatically detects place names in unstructured text.
Can identify new or uncommon locations.
No need to manually list all place names.
 ### Disadvantages:
Can misclassify non-locations as places.
Depends on language models, which may require training.
Slightly slower  than regex.

## map images
### ner_map.PNG https://github.com/jafar756/FASDH25-portfolio2/blob/main/Map%20images/ner_map.png
### regex_map.PNG https://github.com/jafar756/FASDH25-portfolio2/blob/main/Map%20images/regex_map.png

## Self critical analysis 
- One of the challenges we faced in this project was that the regex and gazetteer method is quite limited, what we see was that it only works well if the place names are already in the list, and even smallest changes in spelling or format can cause it to miss things. The NER method is more flexible and can recognize names on its own,  but it's not always accurate, it very often picks up names of organizations or people by mistake for example it picked up people like Netanyahu, and Hamas as a place name. The Geonames query params={"q": "Gaza Strip", "username": API_KEY} returned no results, forcing us to manually assign coordinates (31.5, 34.5). Another issue was with mapping the places, some names are used in multiple locations around the world, so getting the right coordinates wasn’t always straightforward. The familiarity with code would have improved more, because most of the code was new for me and then we came to know that we have to make another document for the ChatGpt solution, further when we start learning from chatgpt, it was giving us some higher level code, that was also confusing us, that also makes things more defficult for us. Thus it takes alot of time to know things much in depth. During map image formation, we have to make ourself familiar with U Kaleido, it requires to save PNG images, but the output was giving us frequent error, which we later know that we have to install it, moreover during working in the gitbash, we were having work collapse, where we unable to git pull or git push, which also hinder our work. 
