#import libraries: plotly express and pandas
import pandas as pd
import plotly.express as px

#load regex_counts.tsv file 


ner_counts_df = pd.read_csv("ner_counts.tsv", sep="\t") #name of places with cordinates
ner_gazetteer_df = pd.read_csv("ner_gazetteer.tsv", sep="\t") # frequancy of places

# Clean column names by stripping spaces
ner_counts_df.columns = ner_counts_df.columns.str.strip()
ner_gazetteer_df.columns = ner_gazetteer_df.columns.str.strip()
# merge the datafram with common placename
merged_df = pd.merge(ner_gazetteer_df, ner_counts_df, left_on="name", right_on="name", how="inner")

# Print the merged dataframe to verify
print(merged_df)

# Convert 'latitude' and 'longitude' to numeric, and drop rows with missing values
merged_df['latitude'] = pd.to_numeric(merged_df['latitude'], errors='coerce')
merged_df['longitude'] = pd.to_numeric(merged_df['longitude'], errors='coerce')
merged_df = merged_df.dropna(subset=['latitude', 'longitude'])
#Remove rows where 'frequency' is NaN
merged_df = merged_df.dropna(subset=['frequency'])

# Check if the 'frequency' column exists, otherwise use the appropriate column name from your data
if 'frequency' not in merged_df.columns:
    print("Frequency column not found. Please check the column name.")
else:
    # Create the map using scatter_map (updated method)
    fig = px.scatter_map(
        data_frame=merged_df,  # Explicitly pass the DataFrame here
        lat="latitude",  # Latitude column name
        lon="longitude",  # Longitude column name
        hover_name="name",  # Hover text for each point (can be 'name' or 'Place' depending on the column in your data)
        size="frequency",  # Column for point sizes
        color="frequency",  # Column for point colors
        title="NER-extracted Places",
        zoom=2
    )
                     
fig.update_layout(map_style="carto-positron-nolabels")
#display in the browser:
fig.show()
# save it in HTML  
fig.write_html("ner_map.html")
# save image in png
fig.write_image("ner_map.png")
