"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
import random
from faker import Faker

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute('''DROP TABLE IF EXISTS relationships''')
    cur.execute('''CREATE TABLE relationships
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name1 TEXT NOT NULL,
                    name2 TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    relationship_type TEXT NOT NULL)''')
    con.commit()
    con.close()


def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    fake = Faker()
    relationship_types = ['friend', 
                          'family', 
                          'colleague', 
                          'spouse']
    with sqlite3.connect(db_path) as con:
        cur = con.cursor()
        for i in range(100):
            name1 = fake.name()
            name2 = fake.name()
            start_date = fake.date_between(start_date='-10y', end_date='today')
            relationship_type = random.choice(relationship_types)
            cur.execute('''INSERT INTO relationships (name1, name2, start_date, relationship_type)
                            VALUES (?, ?, ?, ?)''', (name1, name2, start_date, relationship_type))
        con.commit()

if __name__ == '__main__':
   main()