# Import libraries
import osmnx as ox
import geopandas as gpd
import os

# Read file with 20 most populated US cities
urban_areas = gpd.read_file('states/20_cities.geojson')

# Extract list of OSM city search fields
ua_names = urban_areas['NAME10']
cities = []
for i in range(len(ua_names)):
    cities.append(ua_names[i])
cities

# Extract list of just city names
city_name = []
for i in range(len(cities)):
    name = ','.join(cities[i].split(',')[:-1])
    city_name.append(name)
city_name

# Create list of parking tags
parking_tags = {'amenity':'parking'}

# Query + Export parking lot shapefiles
for i in range(len(cities)):
    parking = ox.geometries_from_place(cities[i], parking_tags)
    parking_lots = parking[(parking['geometry'].geom_type == 'Polygon') | (parking['geometry'].geom_type == 'MultiPolygon')]
    parking_gdf = gpd.GeoDataFrame(geometry=list(parking_lots['geometry']), crs=4326)
parking_gdf.to_file("/parking_lots" + city_name[i].replace(' ', "_" + '_parks.shp')
    