#get and image called surftocat.png from octodex and save it locally

import requests
import os

url = 'https://octodex.github.com/images/surftocat.png'

response = requests.get(url)

# test if the file exists and if it doesn't, save response to a file

if not os.path.exists('surftocat.png'):
    with open('surftocat.png', 'wb') as f:
        f.write(response.content)
        print('File saved') # print to the console
else:
    print('File already exists')



