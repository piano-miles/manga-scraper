import requests
import json

data = ''

def load(file):
    f = open(file)
    data = json.load(f)
    f.close()

def download():
    c = 0
    for i in range(len(data)):
        imgs = data['page'+str(1+i)+'_data'].split(',')

        for img in imgs:
            if 'http' in img:
                c += 1
                print('Downloading '+str(c))
                img_data = requests.get(img).content
                with open('images/img'+str(c)+'.jpg', 'wb') as handler:
                    handler.write(img_data)
