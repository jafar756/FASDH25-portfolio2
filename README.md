# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2

## 0. portfolio task 
### purpose 
### Steps 

## 1. Document your project 
### purpose 
### Steps

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

## 4A.  Map the regex-extracted placenames

### The porpose
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
