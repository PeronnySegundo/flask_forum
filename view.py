from flask import *
from main import app
from model import *

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/login")
def loginpage():
    return render_template("login.html", title="Login")

@app.route("/pagetest")
def pagetest():
    return render_template("pagetest.html", title="Test")
    

@app.route('/logado', methods=['GET'])
def mostar_pag_logado():
    return render_template('/logado.html')

@app.route("/logado_funcao")
def logado_funcao():
    senha = request.form.get("senha")
    print(senha)
    if(validar_senha(str(senha))):
        print('a')
        return render_template("/logado.html")
    else:
        return render_template("/home.html")