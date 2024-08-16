#  This Code is just for educational purpose
#  Some of the functions are not soo configured and also might be vulnarable 
#  this code is no where usable for production server 
#  using the same raw code in production might lead to some sql injection attack
#  happy learning (^_^)

from flask import Flask, request, jsonify, render_template, redirect, Response
import sqlite3, config
from  api_bp import bp


app = Flask(__name__, template_folder='html', static_folder='html/static')
app.register_blueprint(bp)
con = sqlite3.connect('database.db')
cur = con.cursor()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login/")
def login():
    cookies = request.cookies.to_dict()
    with  sqlite3.connect("database.db") as con:
        user = config.User(cookies)
        if user.is_authorised:
            return redirect("/checkout/")
    return render_template("login.html")

@app.route("/checkout/")
def checkout_page():
    item_key = request.args.get("item")
    cookies = request.cookies.to_dict()
    user = config.User(cookies)
    if not user.is_authorised: return redirect("/login/?refer={}".format(request.path.replace("/", "")))
    print(user.is_authorised)
    if not item_key:
        content = ""
        for i in config.ITEMS.keys():content += f"<a href='/checkout/?item={i}'>{i}</a><br>"
        return content
    item = config.ITEMS.get(item_key.lower())
  
    if bool(item and user.student):
        item["dprice"] = item["price"] - (item["price"]/100)*item["discount"]
        return item
    
    if item and not user.student:
          item["dprice"] = item["price"]
          return item
    
    return {"Status":"Item Not Found"}

    



app.run(host='0.0.0.0', port=8080)
