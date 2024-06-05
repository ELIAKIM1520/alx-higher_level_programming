#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table
where name matches the argument"""
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
    cursor = db_conn.cursor()
    cursor.execute("SELECT * \
                        FROM `states` \
                        WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    for row in cursor.fetchall():
        print(row)
