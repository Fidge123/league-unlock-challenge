#!/usr/bin/env python3
"""Take match and player data, get champ and save it to the database"""

from os import environ
import psycopg2

# with open("db_config") as file:
#     HOST = file.readline().strip()
#     DBNAME = file.readline().strip()
#     USER = file.readline().strip()
#     PASS = file.readline().strip()
#
# CONN_STRING = "host=" + HOST + " dbname=" + DBNAME + " user=" + USER + " password=" + PASS

CONN_STRING = environ["DATABASE_URL"]
# local way
# "host=" + environ['HOST'] + " dbname=" + environ['DBNAME'] + " user=" + environ['USER'] + " password=" + environ['PW']

HOF_UPDATE = "UPDATE player_halloffame SET (playerid, region) = (%s,%s) WHERE hofid = %s AND place = %s;"

def update():
    """Update Hall of Fame data"""
    conn = psycopg2.connect(CONN_STRING)
    cursor = conn.cursor()
    for hofid in range(1, 9):
        if hofid == 1:
            query = "SELECT id, region, ((kills + assists) / GREATEST(deaths, 1) * 1.0) AS kda FROM player ORDER BY kda DESC LIMIT 3;"
        elif hofid == 2:
            query = "SELECT id, region FROM player ORDER BY assists DESC LIMIT 3;"
        elif hofid == 3:
            query = "SELECT id, region FROM player ORDER BY kills DESC LIMIT 3;"
        elif hofid == 4:
            continue
        elif hofid == 5:
            query = "SELECT id, region FROM player ORDER BY minion DESC LIMIT 3;"
        elif hofid == 6:
            continue
        elif hofid == 7:
            query = "SELECT id, region FROM player ORDER BY highestcrit DESC LIMIT 3;"
        elif hofid == 8:
            query = "SELECT id, region FROM player ORDER BY ccduration DESC LIMIT 3;"
        cursor.execute(query)
        result = cursor.fetchall()
        place = 1

        for player in result:
            player_id = player[0]
            region = player[1]
            data = (player_id, region, hofid, place)
            cursor.execute(HOF_UPDATE, data)
            place += 1
