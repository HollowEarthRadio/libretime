#!/usr/bin/env python
import psycopg2
#import re

def openAirtimeDatabase():
    conn_string = "host='localhost' dbname='airtime' user='airtime' password='airtime'"

    conn = psycopg2.connect(conn_string)

    return conn

def getRandomTitle(conn, cursor):
#    command = 'SELECT id,filepath,artist_name,track_title,album_title,mood FRO$
    command = 'SELECT filepath FROM cc_files where mood ilike \'VoiceStationID\' and hidden=false ORDER BY random() LIMIT 1'

    cursor.execute(command)
    output = cursor.fetchone()

    return output

conn = openAirtimeDatabase()

cursor = conn.cursor()

random = getRandomTitle(conn, cursor)

print("/srv/airtime/stor/" + str(random[0]));

#
# Uncomment this to play the 4Culture voice spot
#print("/srv/airtime/stor/imported/19/unknown/unknown/unknown-4culture spot Voice, KHUH ID-192kbps.mp3");
