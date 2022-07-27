from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template("index.html", users=users)

@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/create', methods=['POST'])
def create():
    #request.form = {first_name: "Elena", last_name: "De Troya", email: "elena@cd.com"}
    User.guardar(request.form)
    return redirect('/')

@app.route('/delete/<int:id>') #/delete/1
def delete(id): #id = 1
    formulario = { #formulario = {"id":1}
        "id": id
    }
    User.borrar(formulario)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)