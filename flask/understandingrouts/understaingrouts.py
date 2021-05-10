from flask import Flask  
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"
@app.route("/dojo")
def DJ():
    return "Dojo"
@app.route("/say/<name>")
def hell(name):
    return "Hello"+" "+name
@app.route("/<int:num>/<name>")
def hel(num,name):
    n=name*num
    return n
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Sorry! No response. Try again."
if __name__=="__main__":
    app.run(debug=True)