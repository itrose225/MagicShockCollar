from flask import Flask, request
from markupsafe import escape
# from twitch import t

app = Flask(__name__)

shockLevel = 0


@app.route("/shock",methods=['GET'])
def getShockLevel():
    return str(shockLevel)

@app.route("/shock", methods=['POST'])
def shock(power):
    #insert output to pin to change power
    #then shock
    return

def changePower(power):
    shockLevel = power
    return shockLevel