from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Observable App!"

@app.route('/work')
def do_work():
    time.sleep(1)
    return "Simulated work done."

if __name__ == "__main__":
    app.run(debug=True)