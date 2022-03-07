import osmnx as ox
import geopandas as gpd
import os

# Import top 20 cities by population file
urban_areas = gpd.read_file('states/20_cities.geojson')

# Create list of city names
ua_names = urban_areas['NAME10']
cities = []
for i in range(len(ua_names)):
    cities.append(ua_names[i])
cities

# Create list of city coordinates as tuples
ua_coords = urban_areas['coords']
city_coords = []
for i in range(len(ua_coords)):
    city_coords.append(ua_coords[i])
    
from ast import literal_eval as make_tuple
coords = [make_tuple(x.strip()) for x in city_coords]
coords

# Get list of OSM ID numbers
id_name = urban_areas['OSM_ID']
osm_id = []
for i in range(len(id_name)):
    osm_id.append(id_name[i])
osm_id

# Create list of city tags with unique relation IDs
city_tags = []
for i in range(len(cities)):
    tag = {'admin_level':'8','OSM': osm_id[i]}
    city_tags.append(tag)
city_tags

# Get city boundary data from OSM 
city_parking = []
for i in range(len(cities)):
    geometries = ox.geometries_from_point(coords[i], city_tags[i])
    city_parking.append(geometries)
    print('Processed %s of 20' %(i))
    
# Print list of collected data to review + filter out empty shapes, e.g. (0,1)
for i in range(len(city_parking)):
    print(city_parking[i].shape, cities[i])

# Remove Charlotte
city_parking.pop(3)
cities.pop(3)

# Remove Denver
city_parking.pop(4)
cities.pop(4)

# Remove San Francisco
city_parking.pop(5)
cities.pop(5)

# Remove San Diego
city_parking.pop(6)
cities.pop(6)

# Remove New York
city_parking.pop(6)
cities.pop(6)

# Remove Phoenix
city_parking.pop(11)
cities.pop(11)

# Remove San Antonio
city_parking.pop(11)
cities.pop(11)

# Remove Washington DC
city_parking.pop(12)
cities.pop(12)

# Filter cleaned up list for only city boundaries with polygon geometries
city_parking_filtered = []
for i in range(len(city_parking)):
    city = city_parking[i]
    city_boundary = city[(city['geometry'].geom_type == 'Polygon') | (city['geometry'].geom_type == 'MultiPolygon')]
    city_parking_filtered.append(city_boundary)

# Review list a second time for cleaning
for i in range(len(city_parking_filtered)):
    print(city_parking_filtered[i].shape, cities[i])
    
# Remove San Jose
city_parking_filtered.pop(5)
cities.pop(5)

# Define filepath for saved files
dest = '/Users/lily/Documents/GitHub/parking_lots/city_boundaries/'

# Correct cities list to only contain the city names without the state attached
import re
city_names = []
for i in range(len(cities)):
    get_name = cities[i]
    fixed_name = re.sub(r',[^,]*$', '', get_name)
    city_names.append(fixed_name)
city_names

# Export the city boundary geodataframes to shapefiles
for i in range(len(city_parking_filtered)):
    city = city_parking_filtered[i]
    city_gdf = gpd.GeoDataFrame(geometry=list(city['geometry']), crs=4326)
    city_gdf.to_file(dest + city_names[i].replace(' ', '_') + '_boundary.shp')