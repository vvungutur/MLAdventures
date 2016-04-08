from flask import Flask, render_template, flash

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='Erlang123'
)

@app.route("/")
def show_entries():
    entries = ['one', 'two', 'three']
    flash('Hey, look! A message!')
    return render_template('index.html', entries=entries)

if __name__ == "__main__":
    app.run()
