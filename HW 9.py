import threading
import json
import os
import requests

# print(os.getcwd())


with open("images_json.json", "r") as json_file:
    data = json.load(json_file)


images_link = []
for image in data['images']:
    images_link.append(image['link'])
# print(images_link)


def file_download():
    file_names = ['image1.png', 'image2.png', 'image3.png', 'image4.png', 'image5.png']
    j = 0
    for i in images_link:
        i = str(i)
        try:
            response = requests.get(i)
            check = response.status_code
            if check == 200:
                with open(file_names[j], 'wb') as file:
                    file.write(response.content)
                    j += 1
                print("Images are successfully  created!!!")
            else:
                print("Images are not created!!!", response.status_code, response.reason)
        except ConnectionError:
            print("Please, check your internet connection")

# file_download()

thread_list = []
x = threading.Thread(target=file_download)
thread_list.append(x)
x.start()


