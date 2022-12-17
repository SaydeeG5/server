from flask import Flask
import json


app = Flask("server")

@app.get("/")
def home():
    return "hello from flask"

@app.get("/test")
def test():
    return "This is another end point"

@app.get("/about")
def about():
    return "This is about Saydee"

######################################### Catalog API ########################################

@app.get("/api/version")
def version():
    version = {
        "V":"V.1.0.1",
        "name":"Candy_firewall",
        "zip": "your zipcode",
    }
    return json.dumps(version) 

    




app.run(debug=True)