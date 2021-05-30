import threading
import json
import os
import requests

# print(os.getcwd())

with open('image_thr_json.json', 'r') as file:
    data = json.load(file)

link_list = []
for i in data['images']:
    link_list.append(i['link'])
# print(link_list)

def download(link, number):
    response = requests.get(link)
    with open(f'photo{number}.png', 'wb') as image:
        image.write(response.content)

thread_list = []
number = 1
for link in link_list:
    thread_ = threading.Thread(target=download, args=(link, number, ))
    thread_list.append(thread_)
    thread_.start()
    number += 1

for thrd in thread_list:
    thrd.join()