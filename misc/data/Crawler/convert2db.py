#! /usr/bin/env python3

import sys
import json
import sqlite3

if __name__ == "__main__":
    with open(sys.argv[1]) as input:
        scorelist = json.load(input)
    conn = sqlite3.connect(sys.argv[2])
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS SCORE(
        YEAR INT, 
        PROVINCE INT, 
        TYPE INT, 
        SCHOOLID INT, 
        SCHOOLNAME CHAR(50), 
        BATCHID INT, 
        SCORE INT);""")

    conn.commit()

    for i, school in enumerate(scorelist):
        cur.execute("""INSERT INTO SCORE (YEAR, PROVINCE, TYPE, SCHOOLID, SCHOOLNAME, BATCHID, SCORE) VALUES (
            ?,?,?,?,?,?,?
        );""", (school["year"], school["local_province_id"], school["local_type_id"], school["school_id"], school["name"], school["local_batch_id"], school["min"]))

        if i % 100 == 0:
            conn.commit()
            print(i, len(scorelist))

    conn.commit()
