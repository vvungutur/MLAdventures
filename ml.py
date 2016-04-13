from flask import Flask, render_template, flash

# configuration
DEBUG = True
SECRET_KEY = '#notErlang'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def show_entries():
    entries = ['one', 'two', 'three']
    flash('Hey, look! A message!')
    return render_template('index.html', entries=entries)

if __name__ == "__main__":
    app.run()
