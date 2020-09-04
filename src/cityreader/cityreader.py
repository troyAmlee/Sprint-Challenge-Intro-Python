# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

# city,state_name,county_name,lat,lng,population,density,timezone,zips

class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon
  def __str__(self):
    return f"{self.name} {self.lat} {self.lon}"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
  # Implement the functionality to read from the 'cities.csv' file
  # Ensure that the lat and lon valuse are all floats
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open('cities.csv') as c:
    for i in c:
      splitted = i.split(',')
      # print(splitted[0])
      if (splitted[0] != 'city'):
        cities.append(City(splitted[0], float(splitted[3]), float(splitted[4])))
  
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100 -- upper-right - ending range
# Enter lat2,lon2: 32,-120 -- lower-left - starting range
# Enter lat1,lon1: 32,-100 -- upper-left - starting range
# Enter lat2,lon2: 45,-120 -- lower-right - ending range
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

print("Enter lat1,lon1: 45,-100")
print("Enter lat2,lon2: 32,-120")

firstinput =  input("Enter lat1,lon1 (y,x): ")
inp1 = firstinput.split(',')
secondinput =  input("Enter lat2,lon2 (y,x): ")
inp2 = secondinput.split(',')

# Evaluate |upper-right vs lower-left||upper-left vs lower-right|

upper_right = []
lower_left = []
upper_left = []
lower_right = []

if ((float(inp1[1]) > float(inp2[1])) and (float(inp1[0]) > float(inp2[0])) ):
  upper_right = inp1 # ending range
  lower_left = inp2 # starting-range
elif((float(inp1[1]) < float(inp2[1])) and (float(inp1[0]) < float(inp2[0]))):
  upper_right = inp2
  lower_left = inp1
elif((float(inp1[1]) < float(inp2[1])) and (float(inp1[0]) > float(inp2[0]))):
  upper_left = inp1 # starting range
  lower_right = inp2 # ending range
elif((float(inp1[1]) > float(inp2[1])) and (float(inp1[0]) < float(inp2[0]))):
  upper_left = inp2
  lower_right = inp1

if (len(upper_right) > 0):
  latt1 = float(lower_left[0])
  lonn1 = float(lower_left[1])
  latt2 = float(upper_right[0])
  lonn2 = float(upper_right[1])
elif (len(upper_left) > 0):
  latt1 = float(upper_left[0])
  lonn1 = float(upper_left[1])
  latt2 = float(lower_right[0])
  lonn2 = float(lower_right[1])



print(f"\n({int(latt1)}, {lonn1}) ({latt2}, {lonn2})\n")


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = [i.name + f"({i.lat},{i.lon})" for i in cities if((int(i.lat) in range(int(lat1), int(lat2))) and (int(i.lon) in range(int(lon1), int(lon2))))]
  
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within

print(cityreader_stretch(latt1, lonn1, latt2, lonn2, cityreader(cities)))