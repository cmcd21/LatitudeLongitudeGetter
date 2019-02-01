# Latitude & Longitude Getter
Get longitude and latitude of a city/town from .xlsx workbook.

Maps in Tableau often only locate the main areas (major citeis). Latitude and longitude can be entered for any unknown locations.
I had over 50 unknown locations so wanted to automate the process of getting their co-ordinates.

There are 2 programs in this folder:

## latLongAPI

  1. Imports excel file
  2. grabs city and country from excel
  3. loops through every city
  4. uses www.locationIQ.com API to find co-ordinates
  5. writes data to .csv file
  
## latLongSelenium
  1. Imports excel file
  2. grabs city and country from excel
  3. loops through every city
  4. opens chrome to www.latlong.net/ using selenium
  5. Types in the city and country and enter
  6. finds co-ordinates
  7. writes data to .csv file
  
The API method is more efficient but I also wanted to test out seleium.

### Note
- a unique key is required for the API program. This is provided for free when you sign up to LocationIQ.com
- there is a daily search limit on latlong.net
