from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template("searchbar.html")

@app.route("/usersearch")
def search():
    mysql = connectToMySQL("SearchBar_Flask")
    query = "SELECT * FROM countries WHERE name LIKE %%(name)s;"
    data = {
        "name" : request.args.get('name') + "%"  # get our data from the query string in the url
    }
    results = mysql.query_db(query, data)
    return render_template("partials/results.html", countries = results)
    # return render_template("success.html", users = results) # render a template which uses the results

if __name__ == "__main__":
    app.run(port=5004,debug=True) 
