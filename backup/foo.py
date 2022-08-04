#get an image from https://octodex.github.com/images/surftocat.png and save it locally
 
import requests
import os

url = 'https://octodex.github.com/images/surftocat.png'

response = requests.get(url)

with open('surftocat.png', 'wb') as f:
    f.write(response.content)

print('done')
