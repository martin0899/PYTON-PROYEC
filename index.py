from flask import Flask, render_template

app = Flask(__name__)

# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")
@app.route('/calendar')
def calendar():
    return render_template("calendar.html")
@app.route('/exel')
def exel():
    return render_template("crear_exel.html")
@app.route('/horario')
def horario():
    return render_template("horario.html")

@app.route('/about',strict_slashes=False)
def about():
    return render_template("about.html")

# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
