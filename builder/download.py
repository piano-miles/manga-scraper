import requests
import json
import os
from os import path
from tqdm import tqdm
import time

def download(file):
    with open(file) as f:
        data = json.load(f)
    if not path.exists('images'):
        os.mkdir(f'{os.getcwd()}/images')
        print('Created image directory.')
    else:
        print('Image directory exists.')

    imgs = []
    for i in range(len(data)):
        imgs.extend(iter(data[f'page{str(1 + i)}_data'].split(',')))
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

            with open(f'images/img{c}.jpg', 'wb') as handler:
                handler.write(img_data)

            if c%45==0:
                time.sleep(5) # Prevent over-requesting
