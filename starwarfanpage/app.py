from flask import Flask,  render_template, request, url_for


app=Flask(__name__)

@app.route("/")
def home():
    return render_template('inicio.html')


app.run(debug=True)