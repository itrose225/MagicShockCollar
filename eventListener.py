from flask import Flask
import main

app = Flask("ShockCollar")

@app.route("/shock", methods=['POST'])
def invoke_shock(power_level):
    return main.shock(power_level)


if __name__ == '__main__':
    app.run()