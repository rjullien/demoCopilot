#get and image called surftocat.png from octodex and save it locally

import requests
import os

url = 'https://octodex.github.com/images/surftocat.png'

# test if the file exists and if it does, skip the download
if not os.path.exists('surftocat.png'):
    r = requests.get(url)
    with open('surftocat.png', 'wb') as f:
        f.write(r.content)
        print('File downloaded')
else:
    print('File already exists')

    