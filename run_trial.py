from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/001")
def trial1():
    return render_template("trial1.html")

@app.route("/002")
def trial2():
    return render_template("trial2.html")

@app.route("/003")
def trial3():
    return render_template("trial3.html")

@app.route("/004")
def trial4():
    return render_template("trial4.html")

@app.route("/005")
def trial5():
    return render_template("trial5.html")

@app.route("/006")
def trial6():
    return render_template("trial6.html")    

@app.route("/007")
def trial7():
    return render_template("trial7.html")    

@app.route("/008")
def trial8():
    return render_template("trial8.html")


@app.route("/009")
def trial9():
    return render_template("trial9.html")

@app.route("/010")
def trial10():
    return render_template("trial10.html")

@app.route("/011")
def trial11():
    return render_template("trial11.html")




if __name__ == "__main__":
    app.run(debug=True)