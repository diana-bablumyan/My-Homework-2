import json
import yaml
import os

# print(os.getcwd())

class Bands(object):
    def __init__(self, name, origin, genres, members, actnow, songs):
        self.name = name
        self.origin = origin
        self.genres = genres
        self.members = members
        self.actnow = actnow
        self.songs = songs

    def __repr__(self):
        return f"Name of band - {self.name}"

    def present(self):
        return f"Band's name - {self.name}\nOrigin - {self.origin}\nGenre - {self.genres}\n"\
               f"Number of members - {self.members}\n"\
               f"Active now - {self.actnow}\nSome songs - {self.songs}"

    def to_json(self):
        data_ = {
            'name': self.name,
            'origin': self.origin,
            'genres': self.genres,
            'members': self.members,
            'act_now': self.actnow,
            'songs': self.songs
        }
        return data_

    def to_text(self):
        data_1 = {
            'name': self.name,
            'origin': self.origin,
            'genres': self.genres,
            'members': self.members,
            'act_now': self.actnow,
            'songs': self.songs
        }

        return data_1

with open("band_sample_yaml.yml", "r") as yaml_file:
    data = yaml.load(yaml_file, Loader=yaml.FullLoader)
    # print(data)

bands = []
for band in data['bands']:
    # print(band)
    bands.append(
        Bands(
            name=band['name'],
            origin=band['origin'],
            genres=band['genres'],
            members=band['members'],
            actnow=band["actnow"],
            songs=band['songs']
        )
    )
for band in bands:
    print(band.present())

filtered_bands_json = []
filtered_bands_txt = []
for band in bands:
    if band.members > 4:
        # print(band.present())
        filtered_bands_json.append(band.to_json())
        filtered_bands_txt.append(band.to_text())

# for band in filtered_bands_txt:
#     print(band)

json_data = {"bands": filtered_bands_json}
# print(filtered_bands_json)
txt_data = str({"bands": filtered_bands_txt})
# print(filtered_bands_txt)

# JSON to JSON
with open("filtered_band.json", "w") as json_file:
    json.dump(json_data, json_file, indent=4)

# JSON to TEXT
with open("filtered_band.txt", "w") as txt_file:
    json.dump(txt_data, txt_file)

# JSON to YAML
with open("filtered_band.yml", "w") as yaml_file:
    yaml.dump(json_data, yaml_file)
