from flask import Flask, request
from markupsafe import escape
# from twitch import twitch

shockLevel = 0


def getShockLevel():
    return str(shockLevel)

def shock(power):
    #insert output to pin to change power
    #then shock
    return

def changePower(power):
    shockLevel = power
    return shockLevel