from flask import Flask, render_template


app=Flask(__name__, template_folder="templatess")

@app.route('/')
def homi():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)