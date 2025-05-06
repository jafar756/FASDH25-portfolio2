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
- Load the Gaza gazetteer to extract place names and their alternate spellings.
-- Generate flexible regex patterns to match spelling variations for each place name.
-- Iterate through the corpus folder, reading each article file.
-- Filter articles by date, including only those written after the start of the 2023 Gaza war
-- Match place names in each article using the regex patterns and count the occurrences.
-- Extract the article’s month from its filename for monthly aggregation.
-- Update a nested dictionary to store place-wise mention counts per month.
-- Write the results to a regex_counts.tsv file with columns: placename, month, and count.



## 2B Using Stanza to extract all places names from the corpus
### purpose 
- The goal of the project is to extract, clean, count and geocode all place names mentioned in the selected articles written in January 2024.  
### Steps
- I Install and uses the stanza library in collab, for NLP task. 
-- Import python libraries and language model
-- download the English language models and build a pipeline
-- Clone the corpus in the portfolio repo
-- I extracted the place names from articles written in January 2024
-- Count the number of times place name used
-- Clean up the duplicate names and merge
-- write the cleaned place names and their frequency counts into a tab separated values fofile for further
--  Displays the content of the saved TSV file, showing the list of unique , cleaned place names and how many times each appeared in january 2024 news articles. 
