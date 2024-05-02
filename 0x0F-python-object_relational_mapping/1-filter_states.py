#!/usr/bin/python3
"""Lists all states with a name starting with N from the database
hbtn_0e_0_usa
"""
import sys
import MySQLdb
if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
	port=3306
        db=sys.argv[3]
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
