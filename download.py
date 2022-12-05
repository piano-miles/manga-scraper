import requests
import json
from tqdm import tqdm

f = open('storage.json')
data = json.load(f)
f.close()

count = 0

for i in tqdm(range(len(data))):
    images = data["page"+str(1+i)+"_data"].split(",")

    for img in images:
        count += 1
        img_data = requests.get(img).content
        with open('images/img'+str(count)+'.jpg', 'wb') as handler:
            handler.write(img_data)
