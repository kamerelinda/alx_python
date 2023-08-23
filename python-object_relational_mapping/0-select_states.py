#!/usr/bin/python3
# imports module MySQLdb
import MySQLdb


def main():
    # Connecting to database in the localhost
    database = MySQLdb.connect(host='localhost', user='root',
                               passwd='fabi2star.', db='hbtn_0e_0_usa', port=3306)

    # create a cursor
    cur = database.cursor()

    # finding all the states in the database
    cur.execute("SELECT * FROM states ORDER BY states.id")

    # obtaining the results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # close cursor
    cur.close()

    # close database
    database.close()


if __name__ == "__main__":
    main()
