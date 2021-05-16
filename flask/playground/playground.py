from flask import Flask,render_template

app = Flask(__name__)                     

@app.route("/")
@app.route("/<int:x>")
@app.route("/<int:x>/<int:y>")
@app.route("/<color>")
@app.route("/<color>/<color2>")
@app.route("/<int:x>/<color>")
@app.route("/<int:x>/<int:y>/<color>")
@app.route("/<int:x>/<int:y>/<color>/<color2>")
def home(x=8,y=8,color="red",color2="black"):
    return render_template("index.html",x=x,y=y,color=color,color2=color2)

if __name__=="__main__":
    app.run(debug=True) 
