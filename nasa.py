import requests

url = 'https://images-api.nasa.gov/search?q=Ilan%20Ramon'
image_metadata_url= 'https://images-assets.nasa.gov/image/{0}/metadata.json' #KSC-03pd2975/metadata.json'

# params = dict(
#     origin='Chicago,IL',
#     destination='Los+Angeles,CA',
#     waypoints='Joplin,MO|Oklahoma+City,OK',
#     sensor='false'
# )

resp = requests.get(url=url)
data = resp.json()

for item in data['collection']['items']:

    item_nasa_id = item['data'][0]['nasa_id']
    item_href = item['links'][0]['href']
    image_metadata = requests.get(url=image_metadata_url.format(item['data'][0]['nasa_id']))
    file_type = str(image_metadata.json()['File:FileSize']).split(' ')[1]

    if file_type != "MB": #kb
        file_zise = int(str(image_metadata.json()['File:FileSize']).split(' ')[0])
        if file_zise > 1000:
            print(file_zise)
            print(item_nasa_id)
            print(item_href)