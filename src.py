import requests
import os


mydir = ''
baseUrl = ''

arr = (os.listdir(mydir))
for i in range(len(arr)):
    imgName = arr[i].replace('mv2', '~mv2')
    url = baseUrl + imgName
    print(url)
    with open('image_2018_'+str(i)+'.jpg', 'wb') as f:
        f.write(requests.get(url).content)
