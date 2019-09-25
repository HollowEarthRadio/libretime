#!/usr/bin/env python
import psycopg2
#import re

def openAirtimeDatabase():
    conn_string = "host='localhost' dbname='airtime' user='airtime' password='airtime'"

    conn = psycopg2.connect(conn_string)

    return conn

def getRandomTitle(conn, cursor):
    command = 'SELECT filepath FROM cc_files where mood ilike \'FCC\' and hidden=false ORDER BY random() LIMIT 1'

    cursor.execute(command)
    output = cursor.fetchone()

    return output

conn = openAirtimeDatabase()

cursor = conn.cursor()

random = getRandomTitle(conn, cursor)

print("/srv/airtime/stor/" + str(random[0]));

