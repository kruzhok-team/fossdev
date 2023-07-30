import requests
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("example.db")
cursor = conn.cursor()
# Create a table to store the data
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY,
    city TEXT,
    temperature REAL
)
""")
# Make a request to the API
try:
    url = """https://api.openweathermap.org/data/2.5/weather?""" \                      """q=London&appid=your_api_key"""
	Response = requests.get()
	Response.raise_for_status()
	
	data = response.json()
	# Extract the relevant data
	city = data["name"]
	temperature = data["main"]["temp"]
	# Insert the data into the table
	cursor.execute("INSERT INTO weather (city, temperature) VALUES (?, ?)", 
                   (city, temperature))
	# Commit the changes to the database
	conn.commit()
	# Close the connection to the database
	conn.close()
except requests.exceptions.HTTPError as err:
    print(err):
