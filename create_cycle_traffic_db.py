import os
from tempfile import TemporaryDirectory
import requests, zipfile, io
import csv

import sqlite3



# Bestehende Datenbank löschen
# if os.path.exists("cycle_traffic.db"):
#     os.remove("cycle_traffic.db")

# SqLite
con = sqlite3.connect('cycle_traffic.db')
cur = con.cursor()

# Datenbanktabellen anlegen
cur.execute('''CREATE TABLE stations (id int, name text, dir1_description text, dir2_description text, latitude real, longitude real)''')
cur.execute('''CREATE TABLE count_values (station_id int, datetime text, sum int, dir1 int, dir2 int)''')

# Fahrradzählstationen
# Wolbecker Straße fehlt in den csv-Daten
# Koordinaten nicht exakt, da eine Messstation je Richtung
stations = [
    (100034978, 'Gartenstraße', 'stadteinwärts', 'stadtauswärts', 51.97154102512242, 7.635686416805148),
    (100031300, 'Hafenstraße', 'Channel 1 IN', 'Channel 2 OUT', 51.95426, 7.62974),
    (100034980, 'Hammer Straße', 'stadteinwärts', 'stadtauswärts', 51.95459383834764, 7.62605660547107),
    (100034982, 'Hüfferstraße', 'stadteinwärts', 'stadtauswärts', 51.96192737985029, 7.610653812811146),
    (100053305, 'Kanalpromenade', 'Richtung Osttor', 'Richtung Zentrum', 51.91734212654504, 7.649359703063966),
    (100035541, 'Neutor', 'stadteinwärts', 'stadtauswärts', 51.966988, 7.615511),
    (100031297, 'Promenade', 'Richtung Mauritztor', 'Richtung Salzstraße', 51.960595599885565, 7.634015197473532),
    (100034983, 'Warendorfer Straße', 'stadteinwärts', 'stadtauswärts', 51.961847945566, 7.63768440685822),
    (100034981, 'Weseler Straße', 'stadteinwärts', 'stadtauswärts', 51.95074, 7.61753)]

for station in stations:
    cur.execute("INSERT INTO stations VALUES (?, ?, ?, ?, ?, ?)", station)
con.commit()


with TemporaryDirectory() as tmp_dir_path:
    r = requests.get('https://github.com/od-ms/radverkehr-zaehlstellen/archive/refs/heads/main.zip')
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(tmp_dir_path)

    # Gartenstraße
    station_dir_path = os.path.join(tmp_dir_path, 'radverkehr-zaehlstellen-main','100034978')
    for filename in os.listdir(station_dir_path):
        with open(os.path.join(station_dir_path, filename)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    cur.execute("INSERT INTO count_values VALUES (?, ?, ?, ?, ?)", ('100034978', row[0], row[1], row[2], row[3]))
                line_count += 1
            con.commit()

    # Hafenstraße
    station_dir_path = os.path.join(tmp_dir_path, 'radverkehr-zaehlstellen-main','100031300')
    for filename in os.listdir(station_dir_path):
        with open(os.path.join(station_dir_path, filename)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    cur.execute("INSERT INTO count_values VALUES (?, ?, ?, ?, ?)", ('100031300', row[0], row[1], row[2], row[3]))
                line_count += 1
            con.commit()

    # Hammer Straße
    station_dir_path = os.path.join(tmp_dir_path, 'radverkehr-zaehlstellen-main','100034980')
    for filename in os.listdir(station_dir_path):
        with open(os.path.join(station_dir_path, filename)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    cur.execute("INSERT INTO count_values VALUES (?, ?, ?, ?, ?)", ('100034980', row[0], row[1], row[2], row[3]))
                line_count += 1
            con.commit()

    # Hüfferstraße
    station_dir_path = os.path.join(tmp_dir_path, 'radverkehr-zaehlstellen-main','100034982')
    for filename in os.listdir(station_dir_path):
        with open(os.path.join(station_dir_path, filename)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    cur.execute("INSERT INTO count_values VALUES (?, ?, ?, ?, ?)", ('100034982', row[0], row[1], row[2], row[3]))
                line_count += 1
            con.commit()

    # Kanalpromenade
    station_dir_path = os.path.join(tmp_dir_path, 'radverkehr-zaehlstellen-main','100053305')
    for filename in os.listdir(station_dir_path):
        with open(os.path.join(station_dir_path, filename)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    cur.execute("INSERT INTO count_values VALUES (?, ?, ?, ?, ?)", ('100053305', row[0], row[1], row[2] + row[4], row[3] + row[5]))
                line_count += 1
            con.commit()

    # Neutor
    station_dir_path = os.path.join(tmp_dir_path, 'radverkehr-zaehlstellen-main','100035541')
    for filename in os.listdir(station_dir_path):
        with open(os.path.join(station_dir_path, filename)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    cur.execute("INSERT INTO count_values VALUES (?, ?, ?, ?, ?)", ('100035541', row[0], row[1], row[2], row[3]))
                line_count += 1
            con.commit()

    # Promenade
    station_dir_path = os.path.join(tmp_dir_path, 'radverkehr-zaehlstellen-main','100031297')
    for filename in os.listdir(station_dir_path):
        with open(os.path.join(station_dir_path, filename)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    cur.execute("INSERT INTO count_values VALUES (?, ?, ?, ?, ?)", ('100031297', row[0], row[1], row[2] + row[4] + row[6], row[3] + row[5] + row[7]))
                line_count += 1
            con.commit()

    # Warendorfer Straße
    station_dir_path = os.path.join(tmp_dir_path, 'radverkehr-zaehlstellen-main','100034983')
    for filename in os.listdir(station_dir_path):
        with open(os.path.join(station_dir_path, filename)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    cur.execute("INSERT INTO count_values VALUES (?, ?, ?, ?, ?)", ('100034983', row[0], row[1], row[2], row[3]))
                line_count += 1
            con.commit()

    # Weseler Straße
    station_dir_path = os.path.join(tmp_dir_path, 'radverkehr-zaehlstellen-main','100034981')
    for filename in os.listdir(station_dir_path):
        with open(os.path.join(station_dir_path, filename)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    cur.execute("INSERT INTO count_values VALUES (?, ?, ?, ?, ?)", ('100034981', row[0], row[1], row[2], row[3]))
                line_count += 1
            con.commit()

con.close()
