from flask import render_template,session,request,url_for

#importando o app e o db
from loja import app, db
#puxando o app
@app.route('/')


def home():
    return "Carregando..."


@app.route('/registrar')


def registrar():
   return render_template('admin/registrar.html', title="Registrar usuario")
