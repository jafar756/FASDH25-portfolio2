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
-- Generated flexible regex patterns to match spelling variations for each place name.
-- Iterated through the corpus folder, reading each article file.
-- Filtered articles by date, including only those written after the start of the 2023 Gaza war
-- Then Match place names in each article using the regex patterns and count the occurrences.
-- Extracted the article’s month from its filename for monthly aggregation.
-- Updated a nested dictionary to store place-wise mention counts per month.
-- Writen the results to a regex_counts.tsv file with columns: placename, month, and count.
## 2B Using Stanza to extract all places names from the corpus
### purpose 
- The goal of the project is to extract, clean, count and geocode all place names mentioned in the selected articles written in January 2024.  
### Steps
- Installed and uses the stanza library in collab, for NLP task. 
-- Imported python libraries and language model
-- downloaded the English language models and build a pipeline
-- Cloned the corpus in the portfolio repo
-- I extracted the place names from articles written in January 2024
-- Counted the number of times place name used
-- Cleaned up the duplicate names and merge
-- writen the cleaned place names and their frequency counts into a tab separated values fofile for further
--  Displays the content of the saved TSV file, showing the list of unique , cleaned place names and how many times each appeared in january 2024 news articles. 
