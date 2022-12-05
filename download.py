import requests
import json

f = open('storage.json')
data = json.load(f)
f.close()

count = 0

images = data["page1_data"].split(",")

for img in images:
    count += 1
    img_data = requests.get(img).content
    with open('images/img'+str(count)+'.jpg', 'wb') as handler:
        handler.write(img_data)
