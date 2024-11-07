import sqlite3


def save_earthquakes(place_mag_list):
    conn = sqlite3.connect('earthquakes.db')
    c = conn.cursor()
    c.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL)")
    c.executemany("INSERT INTO earthquakes VALUES (?, ?)", place_mag_list)
    conn.commit()
    conn.close()


def select_earthquakes():
    conn = sqlite3.connect('earthquakes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM earthquakes")
    earthquake_data = c.fetchall()
    [print(row) for row in earthquake_data]
    conn.commit()
    conn.close()
