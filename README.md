## Analyzing Parking Lot Surface Area Coverage in US Cities

####Lily Kuentz

In this study, I will examine the proportion of land use dedicated to parking lots across twenty major US cities.

#### Research questions: 

* How much surface area is dedicated to parking in US cities?
* How does the proportion of city-wide parking lot coverage vary across the continental US with respect to differences in car cultures?

The datasets used in this study will include:

* osmnx
* numpy
* matplotlib
* geopandas
* os
* glob

###Methodology:
For this study I will query Open Street Map to identify the parking lot polygons in the top twenty US cities (by population). Core Based Statistical Areas (CBSAs) from the US census will be used to outline metropolitan areas. I will sum the area of the parking lot polygons within each city and calculate the percentage of parking lot surface area within those CBSAs. The results of each city calculation will be projected onto a continent-wide map of the US.

### Expected Outcomes
The primary product of this project will be a reproducible script that can be used for different scales of analysis and futures updates to OSM data. The results of the present analysis will be used to validate the claims of previous studies of parking lot land use. This outcome will also produce a dataset that can be utilized in comparative studies of car culture between different US cities.

Herriges, D. (2019) Parking Dominates Our Cities. But Do We Really *See* It? <a>https://www.strongtowns.org/journal/2019/11/27/parking-dominates-our-cities-but-do-we-really-see-it</a>

Jakle, J.A., Sculle, K.A. (2004) Land Use in a Car Culture. University of Virginia Press.

Ryan, J.C. (2021) Assessing the impacts of urban golf courses on access to greenspace in the United States. <a>https://github.com/JohnnyRyan1/parks-and-golf</a>

Scharnhorst, E. (2018) Quantified Parking: Comprehensize Parking Inventories for Five U.S. Cities. Research Institute for Housing America.

Strong Towns (2018) The Many Costs of Too Much Parking. <a>https://www.strongtowns.org/journal/2018/11/20/the-many-costs-of-too-much-parking</a>

United States Census Bureau (2021) Core Based Statistical Areas, Metropolitan/Micropolitan Statistical Area. TIGER/Line Shapefiles. <a>https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html</a>
