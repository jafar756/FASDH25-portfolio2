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





#3. Create a Gazatteer for the NER Places
## Purpose
 --Taking names from ner.counts.tsv file, which has place names and get the coordinates for those places using GeoNames API and save the information AS NER_gazetteer.tsv file.
## what the script is doing
 --Reads the place names from 'ner_counts.tsv'
--uses the Geonames API(http://www.geonames.org/) for coordinates.
--prints coordinates for the place names.
--prints NA where coordinates are not found which would be manually added later.
--saves the output in a tsv file.

--the following place had not their coordinates and were manually fixed.
--names           lat            long
--Dahiyeh	 33.85°	        35.51°
Shujayea	 31.50056°	34.47000°				
Abudaqa	         43.2374°	79.8782°		
Mazzeh	         33.5014°       36.2468°		
Nairoukh	31.07°	        10.51°
Shawawra	31.69111°	35.27222			
Beruit	        33.8938°       35.5018°
Bahaa	        20.0123°	        41.4686°		
Rawaa	        51.7662°	        20.2562°
Philadelphi	39.9526°	       75.1652°
Yir’On	        33.0772° 	        35.4543°
 