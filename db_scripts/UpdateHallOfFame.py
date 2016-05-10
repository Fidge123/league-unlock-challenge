#!/usr/bin/env python3
"""Take match and player data, get champ and save it to the database"""

import json
import psycopg2

with open('db_config') as file:
    HOST = file.readline().strip()
    DBNAME = file.readline().strip()
    USER = file.readline().strip()
    PASS = file.readline().strip()

def update():
    conn_string = "host=" + HOST + " dbname=" + DBNAME + " user=" + USER + " password=" + PASS
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    query ="DELETE FROM player_halloffame WHERE 1=1;"
    cursor.execute(query)
    conn.commit()
    for i in range(1,9):
        if i == 1:
            query = "SELECT id, region, ((kills+assists)/deaths*1.0) AS kda FROM player ORDER BY kda DESC LIMIT 3;"
        elif i == 2:
            query = "SELECT id, region FROM player ORDER BY assists DESC LIMIT 3;"
        elif i == 3:
            query="SELECT id, region FROM player ORDER BY kills DESC LIMIT 3;"
        elif i == 4:
            continue
            #query="SELECT "
        elif i == 5:
            query="SELECT id, region FROM player ORDER BY minion DESC LIMIT 3;"
        elif i == 6:
            continue
            #query="SELECT id, region FROM player ORDER BY highestcrit DESC LIMIT 3;"
        elif i == 7:
            query="SELECT id, region FROM player ORDER BY highestcrit DESC LIMIT 3;"
        elif i == 8:
            query="SELECT id, region FROM player ORDER BY ccduration DESC LIMIT 3;"
        cursor.execute(query)
        result1 = cursor.fetchone()
        result2 = cursor.fetchone()
        result3 = cursor.fetchone()
        player_id = result1[0]
        region = result1[1]
        place = 1
        query = "INSERT INTO player_halloffame(playerid,region,hofid,place) VALUES (%s,%s,%s,%s);"
        data = (player_id,region,i,place)
        cursor.execute(query,data)
        player_id = result2[0]
        region = result2[1]
        place = 2
        query = "INSERT INTO player_halloffame(playerid,region,hofid,place) VALUES (%s,%s,%s,%s);"
        data = (player_id,region,i,place)
        cursor.execute(query,data)
        player_id = result3[0]
        region = result3[1]
        place = 3
        query = "INSERT INTO player_halloffame(playerid,region,hofid,place) VALUES (%s,%s,%s,%s);"
        data = (player_id,region,i,place)
        cursor.execute(query,data)
        conn.commit()
        
