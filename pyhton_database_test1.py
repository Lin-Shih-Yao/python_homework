from flask import Flask, json
from flask import request
from flask.templating import render_template
import mysql.connector
from webbrowser import open
a = input()
b = input()
sysdb = mysql.connector.connect(
    host = "localhost",
    database = "class",
    user = "root",
    password = "lf21227a"

)
#username驗證
mycursor = sysdb.cursor()
sql = "SELECT username FROM user;"
mycursor.execute(sql)
usernamedata = []
for x in mycursor.fetchall():
    usernamedata += x

answer = []
if a in usernamedata:
    answer.append("username_pass")
else:
    answer.append("username_error")

#password驗證
mycursor = sysdb.cursor()
sql = f"SELECT password FROM user WHERE username = '{a}';"
mycursor.execute(sql)
passworddata = []
for y in mycursor.fetchall():
    passworddata += y

if b in passworddata:
    answer.append("password_pass")
else:
    answer.append("password_error")
    
mycursor.close()
sysdb.close()

#回覆給使用者
if "username_error" in answer:
    open("http://127.0.0.1:3000/username_error")
    app = Flask(__name__) #__name__代表目前執行的模組

    @app.route("/") #函式的裝飾(Decorator):已函示已函式為基礎，提供附加的功能
    def index():
        return "Sign in"

    @app.route("/username_error")
    def username_error():
        return "UNKNOWN USERNAME"

    @app.route("/password_error")
    def password_error():
        return "PASSWORD ERROR !"

    @app.route("/sign_in_pass")
    def ok():
        return "PASS!"
        
    @app.route("/home")
    def home():
        return render_template("home.html")

    app.run(port=3000)
    
elif "password_error" in answer:
    open("http://127.0.0.1:3000/password_error")
    app = Flask(__name__) #__name__代表目前執行的模組

    @app.route("/") #函式的裝飾(Decorator):已函示已函式為基礎，提供附加的功能
    def index():
        return "Sign in"

    @app.route("/username_error")
    def username_error():
        return "UNKNOWN USERNAME"

    @app.route("/password_error")
    def password_error():
        return "PASSWORD ERROR !"

    @app.route("/sign_in_pass")
    def ok():
        return "PASS!"
        
    @app.route("/home")
    def home():
        return render_template("home.html")

    app.run(port=3000)
    
else:
    open("http://127.0.0.1:3000/sign_in_pass")
    app = Flask(__name__) #__name__代表目前執行的模組

    @app.route("/") #函式的裝飾(Decorator):已函示已函式為基礎，提供附加的功能
    def index():
        return "Sign in"

    @app.route("/username_error")
    def username_error():
        return "UNKNOWN USERNAME"

    @app.route("/password_error")
    def password_error():
        return "PASSWORD ERROR !"

    @app.route("/sign_in_pass")
    def ok():
        return "PASS!"
        
    @app.route("/home")
    def home():
        return render_template("home.html")

    app.run(port=3000)
    

