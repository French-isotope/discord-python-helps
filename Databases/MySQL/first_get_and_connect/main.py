import mysql.connector
import json
import base64

conn = mysql.connector.connect(
    user='root',
    password='x',
    host='x',
    database='x')

if conn:
    print("Connected Successfully")
else:
    print("Connection Not Established")

def getSpeciesData(name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM hewankusayang WHERE namapopuler = '{name}'")
    # Ganti aja column di where nya
    result = cursor.fetchone()
    return json.dumps({"namapopuler": result[0], "namailmiah": result[1], "foto": result[2], "taxonomy": result[3], "kingdom": result[4], "genus": result[5], "class": result[6], "ordo": result[7], "family": result[8], "species": result[9], "deskripsi": result[10], "persebaran": result[11], "habitat": result[12], "iucn": result[13], "tersedia": result[14], "rataumur": result[15], "ratapanjang": result[16], "ratalebar": result[17], "rataberat": result[18]})

print(getSpeciesData('tnama'))
