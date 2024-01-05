#importing libraries for data manipulation (pandas),
#geospatial operations (shapely.geometry, geopandas), and 
#plotting (matplotlib.pyplot, matplotlib.offsetbox).
#Reference source: https://www.youtube.com/watch?v=euCbgfj5DvM
#reference source: https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html

import pandas as pd
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Read the dataset into a dataframe
df = pd.read_csv(r'C:\Users\jiten\OneDrive\Desktop\python assignment 2\GrowLocations.csv')

# The geographic coordinates for the UK are 55.3781° N, 3.4360° W. 
# However, in the dataset, the columns representing latitude and longitude are inaccurately named. 
# To address this, Data cleaning and column renaming as the latitude and longitude columns are incorrectly named as per the data values. 
df = df.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'})

# Data cleaning
# Filter out rows with invalid latitude and longitude values
df = df[(df['Latitude'] >= 50.681) & (df['Latitude'] <= 57.985) & (df['Longitude'] >= -10.592) & (df['Longitude'] <= 1.6848)]

# Verify column names
expected_columns = ['Latitude', 'Longitude']
if not all(col in df.columns for col in expected_columns):
    raise ValueError("Column names do not match the expected columns.")

# Create a GeoDataFrame with Shapely geometry
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = GeoDataFrame(df, geometry=geometry)

# Load the custom map image
map_image = plt.imread(r'C:\Users\jiten\OneDrive\Desktop\python assignment 2\map7.png')
# Plot sensor locations on the custom map
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(map_image, extent=[-10.592, 1.6848, 50.681, 57.985])

# Plot sensor locations on the map
gdf.plot(ax=ax, marker='o', color='red', markersize=20, label='Sensor Locations')

# Show legend
ax.legend()

# Show the map
plt.show()
