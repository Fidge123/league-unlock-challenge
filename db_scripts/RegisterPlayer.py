#!/usr/bin/env python3
"""Take player data and save it to the database"""

import json
import psycopg2
import requests

with open('key') as file:
    KEY = {'api_key': file.readline().strip()}

with open('db_config') as file:
    HOST = file.readline().strip()
    DBNAME = file.readline().strip()
    USER = file.readline().strip()
    PASS = file.readline().strip()

def register_player(name, region, email, password, leagueid):
    """Main function"""

    api = 'https://' + region + '.api.pvp.net/api/lol/' + region
    player = json.loads(requests.get(api + '/v1.4/summoner/by-name/' + name, params=KEY).text)[name.lower()]

    conn_string = "host=" + HOST + " dbname=" + DBNAME + " user=" + USER + " password=" + PASS
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    query = "INSERT INTO player(id, leaguename, region, email, password, leagueid) VALUES (%s,%s,%s,%s,%s,%s);"
    data = (player["id"], player["name"], region, email, password, leagueid)
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()
