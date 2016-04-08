
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    x = str(test(2,2)) 
    return x
def test(a, b):
    return a + b

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)

