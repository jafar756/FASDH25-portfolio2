#import libraries: plotly express and pandas
import pandas as pd
import plotly.express as px

#load regex_counts.tsv file 


regex_counts_df = pd.read_csv("regex_counts.tsv", sep="\t") #name of places with cordinates
ner_gazetteer_df = pd.read_csv("ner_gazetteer.tsv", sep="\t") # frequancy of places

# Clean column names by stripping spaces 
regex_counts_df.columns = regex_counts_df.columns.str.strip()
ner_gazetteer_df.columns = ner_gazetteer_df.columns.str.strip()
# merge the datafram with common placename
merged_df = pd.merge(ner_gazetteer_df, regex_counts_df, left_on="name", right_on="name", how="inner")



 # If the date column exists in coordinates_df 
if 'date' in merged_df.columns:
    merged_df['date'] = pd.to_datetime(merged_df['date']) #convert to datetime learn from chatgpt
    
# Extract year-month if date exists
if 'date' in merged_df.columns:
    merged_df['month'] = merged_df['date'].dt.month #Extract month learn from chatgpt
    merged_df['year'] = merged_df['date'].dt.year   #Extract year learn from chatgpt
    
# set the dataframe :
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option("max_colwidth", 15)
#print the dataframe :
print(merged_df)
#  Add this block **right after** you create or load `merged_df`

merged_df['latitude'] = pd.to_numeric(merged_df['latitude'], errors='coerce')
merged_df['longitude'] = pd.to_numeric(merged_df['longitude'], errors='coerce')
merged_df = merged_df.dropna(subset=['latitude', 'longitude'])
#create the map :
fig = px.scatter_map(merged_df,
                     lat="latitude",
                     lon="longitude",
                      size="frequency",
                     animation_frame="months", 
                     color="frequency",
                     hover_name="name",
                     hover_data=["frequency","months"],
                    color_continuous_scale=px.colors.sequential.YlOrRd,
                  title="Regex-Extracted Place Map"
)
                     
fig.update_layout(map_style="carto-positron-nolabels")
#display in the browser:
fig.show()
# save it in HTML  
fig.write_html("regex_map.html")
# save image in png
fig.write_image("regex_map.png")
