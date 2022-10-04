from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, url="mongodb://localhost:27017/mars_app")


@app.route("/")
def home():
   mars_info = mongo.db.collection.find_one()

return render_template("index.html", mars=mars_info)

@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect("/")
if __name__ == "__main__":
   app.run(debug=True)