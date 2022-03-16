from flask import Flask

app = Flask(__name__)
app.secret_key = "some key" # create secret key

# don't forget to import flask, pymysql, and flask_bcrypt in shell