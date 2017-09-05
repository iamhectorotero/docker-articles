from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
cl = MongoClient("localhost:27017")
db = cl["test"]
dummy_number = 0

@app.route("/", methods=["GET", "POST"])
def insert_dummy():
    global dummy_number
    if request.method == "POST":
        db.coll.insert_one({"number": dummy_number})
        dummy_number += 1
        return "Post succeded"
    
    elif request.method == "GET":
        return str(list(db.coll.find({})))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
