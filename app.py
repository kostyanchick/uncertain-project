from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "ROAD TO 2K"


if __name__ == '__main__':
    app.run()
