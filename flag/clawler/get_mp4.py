import requests
 
url = 'https://pic.ibaotu.com/00/51/34/88a888piCbRB.mp4'

r = requests.get(url, stream=True)
 
with open('test.mp4', "wb") as mp4:
    for chunk in r.iter_content(chunk_size=1024 * 1024):
        if chunk:
            mp4.write(chunk)
 
