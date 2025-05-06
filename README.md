# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2

## 0. portfolio task 
### purpose 
### Steps 

## 1. Document your project 
### purpose 
### Steps

## 2A. Use gazeteer and regex to extract places in gaza
##


## 2B Using Stanza to extract all places names from the corpus
### purpose 
- The goal of the project is to extract, clean, count and geocode all place names mentioned in the selected articles written in January 2024.  
### Steps
- I Install and uses the stanza library in collab, for NLP task. 
-- Then I import python libraries, for example stanza for NLP processing, os for directory handling and re for text cleaning and normalization
-- Then I download the English language models and build a pipeline
-- The pipeline used to tokenize text, split multi word tokens and extract named entities
-- Then I clone the Github repository using the fork of my group member
-- Filter the articles directory and adds only the .txt files written in january 2024 to a list
-- The reading all articles, perform NER and counts the frequency of each place name
-- Clean and standardize the place names.
-- For Gaza's, Gaza City and Gaza Strip are all mapped to Gaza. This prevents counting the same place multiples times under different names
-- goes the january files again but this time uses the normalized names to count place mentions more accurately
-- write the cleaned place names and their frequency counts into a tab separated values fofile for further sue
-- Displays the content of the saved TSV file, showing the list of unique , cleaned place names and how many times each appeared in january 2024 news articles. 
