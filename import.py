import mysql.connector
config={"user":"shweta",
        "server":"",
        "password":"",
        "database":""}
conn=mysql.connector.connect(**config)
def add_contact():
    