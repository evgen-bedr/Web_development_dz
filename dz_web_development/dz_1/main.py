from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'


@app.route('/user/<user_name>')
def return_name(user_name):
    return f"Hallo {user_name}"


if __name__ == '__main__':
    app.run()
