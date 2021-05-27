import json
import os
import requests


# print(os.getcwd())


class Images(object):
    def __init__(self, images):
        self.images = images

    def __repr__(self):
        return f"{self.images}"


with open("images_json.json", "r") as json_file:
    data = json.load(json_file)


images_link = []
for image in data['images']:
    # print(image)
    images_link.append(
        Images(
            images=image['link']
        )
    )
# print(images_link)
file_names = ['image1.png', 'image2.png', 'image3.png', 'image4.png', 'image5.png']
j = 0
for i in images_link:
    i = str(i)
    try:
        response = requests.get(i)
        # print(response)
        check = response.status_code
        if check == 200:
            with open(file_names[j], 'wb') as file:
                file.write(response.content)
                j += 1
            print("Images are successfully  created!!!")
        else:
            print("Images are not created!!!", response.status_code, response.reason)
    except:
        print("Please, check your internet connection")
