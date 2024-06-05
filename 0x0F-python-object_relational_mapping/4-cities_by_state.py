#!/usr/bin/python3
""" lists all cities from the database
Takes 3 arguments
results must be sorted in ascending order
"""
import sys
import MySQLdb
if __name__ == "__main__":
    db_conn = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )
    c = db_conn.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM states JOIN
            cities ON states.id=cities.state_id ORDER BY cities.id ASC"""
    c.execute(query)
    for city in c.fetchall():
        print(city)
