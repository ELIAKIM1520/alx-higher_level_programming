#!/usr/bin/python3
"""Displays all the values in the states tab;e of the database and
that is safe from sql injection
"""
import sys
import MySQLdb
if __name__ == '__main__':
    db_conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    cursor = db_conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    safer_state_name = sys.argv[4].replace("'", "''")
    cursor.execute(query, (safer_state_name,))
    for row in cursor.fetchall():
        print(row)
