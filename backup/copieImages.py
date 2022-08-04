# get surftocat.png image from octodex to local 


import requests
import os

url = 'https://octodex.github.com/images/surftocat.png'

response = requests.get(url)

# test if the file exists and if it does, skip the download
if os.path.isfile('surftocat.png'):
    print('file exists, skipping download')
    # skip the download
    # continue
else:
    # download the file
    print('downloading file')
    with open('surftocat.png', 'wb') as f:
        f.write(response.content)

print('done')