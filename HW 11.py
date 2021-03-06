import sqlite3
from sqlite3 import Error
import os
import sys
import json
from pprint import pprint


path = os.getcwd()
# print(os.getcwd())

database = os.path.join(path, 'film.db')
# print(database)

try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
    sys.exit()

curs = conn.cursor()


# # 1.Movies which name starts with âBâ
movies_name_M = """ SELECT * FROM film
                    WHERE title LIKE 'M%';
                    """

result = curs.execute(movies_name_M)
# pprint(result.fetchall())


# # 2.The movie which duration is the largest from film table
max_duration = """SELECT MAX(length)
                    FROM film;
                    """
result_1 = curs.execute(max_duration)
# pprint(result_1.fetchall())


# # 3.Write the data from film table into a json file
result_for_json = """SELECT * FROM film"""


result_2 = conn.execute(result_for_json)
# pprint(result_2.fetchall())

new_list = []
for item in result_2:
    dict_ = {'film_id': item[0],
             'title': item[1],
             'descreption': item[2],
             'release_year': item[3],
             'rate': item[4],
             'length': item[5],
             'speacial_features': item[6]}
    new_list.append(dict_)
# print(new_list)
if new_list:
    message = "Success"
else:
    message = "Not found"
json_data = {
                'Films': new_list,
                'Message': message
}
with open("film_json", 'w') as file:
    json.dump(json_data, file, indent=4)

# # 4. Films which release date is above 2010 and rate is between 3 and 5

filtered_data = """SELECT * 
                FROM film
                WHERE release_year > 2010 and rate between 3 and 5
                """
result_4 = conn.execute(filtered_data)
# pprint(result_4.fetchall())

new_table = """ CREATE TABLE IF NOT EXISTS filtered_film(
                                        'film_id' integer PRIMARY KEY,
                                        'title' text,
                                        'descreption' text,
                                        'release_year' integer,            
                                        'rate' integer,
                                        'length' integer,
                                        'speacial_features' text
                                    ); """

conn.execute(new_table)
conn.commit()
insert_query = """INSERT INTO filtered_film (film_id, title, descreption,
                       release_year, rate, length, speacial_features)
                       VALUES( ?, ?, ?, ?, ?, ?, ?);
                 """

for item in result_4:
    print(item)
    curs.execute(insert_query, item)
conn.commit()
