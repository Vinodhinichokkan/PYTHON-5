import requests
import json
import csv
import pymongo
import mysql.connector
import pandas as pd

# API URL
API_URL = "https://dummyjson.com/products"

# Fetch data from API
response = requests.get(API_URL)
data = response.json()

# Extract required fields
products = [
    {
        "pid": item["id"],
        "pname": item["title"],
        "category": item["category"],
        "price": item["price"],
        "rating": item["rating"]
    }
    for item in data.get("products", [])
]

# Save to JSON file
with open("products.json", "w") as json_file:
    json.dump(products, json_file, indent=4)

# Save to CSV file
csv_file = "products.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["pid", "pname", "category", "price", "rating"])
    writer.writeheader()
    writer.writerows(products)

# Insert into MongoDB
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["ecommerce"]
mongo_collection = mongo_db["products"]
mongo_collection.insert_many(products)

# Insert into MySQL
mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="ecommerce"
)
mysql_cursor = mysql_conn.cursor()

mysql_cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        pid INT PRIMARY KEY,
        pname VARCHAR(255),
        category VARCHAR(255),
        price DECIMAL(10,2),
        rating DECIMAL(3,2)
    )
""")

mysql_cursor.executemany("""
    INSERT INTO products (pid, pname, category, price, rating)
    VALUES (%(pid)s, %(pname)s, %(category)s, %(price)s, %(rating)s)
    ON DUPLICATE KEY UPDATE 
    pname=VALUES(pname), category=VALUES(category), 
    price=VALUES(price), rating=VALUES(rating)
""", products)

mysql_conn.commit()
mysql_cursor.close()
mysql_conn.close()

print("Data successfully stored in MongoDB, MySQL, JSON, and CSV.")