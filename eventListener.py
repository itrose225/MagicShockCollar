from flask import Flask
import main

app = Flask("ShockCollar")

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()