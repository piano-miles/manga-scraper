import requests
import json
import os
from os import path
from tqdm import tqdm

def download(file):
    f = open(file)
    data = json.load(f)
    f.close()

    if not path.exists('images'):
        os.mkdir(os.getcwd()+'/images')
        print('Created image directory.')
    else:
        print('Image directory exists.')

    imgs = []
    for i in range(len(data)):
        for j in data['page'+str(1+i)+'_data'].split(','):
            imgs.append(j)

    c = 0
    print('Downloading images.')
    H = {'referer': 'https://www.webtoons.com/en/action/omniscient-reader/episode-23/viewer?title_no=2154&episode_no=24'}
    for img in tqdm(imgs):
        if 'http' in img:
            c += 1

            try:
                img_data = requests.get(img, headers=H).content
            except Exception as e:
                print("An error occurred when fetching the images.\n"+str(e))
                quit()

            with open('images/img'+str(c)+'.jpg', 'wb') as handler:
                handler.write(img_data)
