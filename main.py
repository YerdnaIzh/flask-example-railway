import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Hi, there"

if __name__ == '__main__':
    app.run()
