import requests
import json

f = open('storage.json')
data = json.load(f)
f.close()

c = 0

for i in range(len(data)):
    imgs = data['page'+str(1+i)+'_data'].split(',')

    for img in imgs:
        if 'http' in img:
            c += 1
            print('Downloading '+str(c))
            img_data = requests.get(img).content
            with open('imgs/img'+str(c)+'.jpg', 'wb') as handler:
                handler.write(img_data)
