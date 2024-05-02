#!/usr/bin/python3
"""takes in the name of states as an argument and lists all cities of the
state"""
import sys
import MySQLdb
if __name__ == '__main__':
    db_conn = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )
    c = db_conn.cursor()
    c.execute("""
    SELECT *
    FROM cities
    INNER JOIN states
    ON cities.state_id=states.id
    ORDER BY cities.id
    """)
    print(', '.join([city[2]
                    for city in c.fetchall()
                    if city[4] == sys.argv[4]]))
