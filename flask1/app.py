from flask import Flask, json
from flask import request
from flask.templating import render_template
import mysql.connector

sysdb = mysql.connector.connect(
    host = "localhost",
    database = "class",
    user = "root",
    password = "lf21227a"

)

mycursor = sysdb.cursor()
sql = "SELECT username FROM user;"
mycursor.execute(sql)
usernamedata = []

for x in mycursor.fetchall():
    usernamedata.append(x[0])

app = Flask(__name__) #__name__代表目前執行的模組

@app.route("/") #函式的裝飾(Decorator):已函示已函式為基礎，提供附加的功能
def home():
    return render_template("home.html")

# 註冊程式
@app.route("/signup", methods=["POST"])
def signup():
    user = request.form["user"]
    username = request.form["username"]
    password = request.form["password"]
    if len(user) > 0 and len(username) > 0 and len(password) > 0: #確認每筆資料都有填入
        if username not in usernamedata: #確認沒有相同帳號
            mycursor = sysdb.cursor()
            sql = f"INSERT INTO user(name, username, password) VALUE (\"{user}\",\"{username}\",\"{password}\");"
            mycursor.execute(sql)
            return render_template("home.html") + "Query ok!"
        else:
            return render_template("home.html") + "Please enter another username"
    else:
        return render_template("home.html") + "尚有欄位偽填入"
        

# 登入程式
@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    if username not in usernamedata:
        return render_template("home.html") + "unknown username"
    else:
        mycursor = sysdb.cursor()
        sql = f"SELECT password FROM user WHERE username = '{username}';"
        mycursor.execute(sql)
        if password != mycursor.fetchall()[0][0]:
            return render_template("home.html") + "password error"
        else:
            mycursor = sysdb.cursor()
            sql = f"SELECT * FROM user WHERE username = '{username}';"
            mycursor.execute(sql)
            user = mycursor.fetchall()[0][1]
            return f"welcome {user} !"

if __name__ == "__main__":
    app.run(port=3000)



