import json, requests, csv, openpyxl, os, time

#import excel file
print('opening workbook...')
os.chdir('C:\\Users\\chris\\Documents')
wb = openpyxl.load_workbook('Resume Data.xlsx')
sheet = wb['Missing']

#grab city and country from excel
places = []
url = "https://us1.locationiq.com/v1/search.php"

for row in range(2, sheet.max_row +1):
    country = sheet['B' + str(row)].value
    city = sheet['C' + str(row)].value
    location = city + ' ' + country

    #get coordinates from LocationIQ API
    data = {
        'key': '', #enter your unique key here
        'q': location,
        'format': 'json'
    }

    response = requests.get(url, params=data)
    response.raise_for_status()

    locationInfo = json.loads(response.text)
    location = [city, country, locationInfo[0]['lat'], locationInfo[0]['lon']]
    print(location)
    places.append(location)
    time.sleep(0.5)

#write to csv file
with open('locationDataAPI.csv', 'w', newline='') as csvFile:
    w = csv.writer(csvFile)
    w.writerow(['City', 'Country', 'Latitude', 'Longitude'])
    w.writerows(places)

print('Done')
