import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'YL9Nh45pxmTRzplfvhfdLCPrNyAzWKg3PAKbeAwy'}

response = requests.get(url, params=params)
data = response.json()
print(data)

photos = data['photos']
photo_links = [photo['img_src'] for photo in photos]

for i, link in enumerate(photo_links, start=1):
    response = requests.get(link)
    with open(f'mars_photo{i}.jpg', 'wb') as file:
        file.write(response.content)
        print('Yes!')

