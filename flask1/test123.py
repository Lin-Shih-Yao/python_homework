import mysql.connector
sysdb = mysql.connector.connect(
    host = "localhost",
    database = "class",
    user = "root",
    password = "lf21227a"

)
user = "xyz"
username = "xyz123"
password = "123"
mycursor = sysdb.cursor()
sql = "INSERT INTO user(name, username, password) VALUE (\"{user}\",\"{username}\",\"{password}\");"
mycursor.execute(sql)