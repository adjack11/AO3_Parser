import json

from flask import Flask, render_template

app = Flask(__name__)

# setting up route (to avoid 404) - Idk what this is yet so look up
@app.route('/')
# defining function for the route
def index(): # run/do these things when I visit the local url
    with open("current_work.json", "r", encoding ="utf-8") as file:
        story = json.load(file)

    return render_template("Template.html", fic = story)

if __name__ == "__main__":
    app.run(debug = True) # errors will show on the page