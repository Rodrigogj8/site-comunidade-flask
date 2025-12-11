from comunidade import app, database, bcrypt
from flask import render_template, url_for, request, flash, redirect
from comunidade.forms import FormLogin, FormCriarConta
from comunidade.models import Usuario  


lista_usuarios = ['Rodrigo', 'Camila', 'Iracema', 'Valmir', 'Drogo']

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html", lista_usuarios=['Rodrigo', 'Camila', 'Iracema', 'Valmir', 'Drogo'])


@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criar_conta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f"Login feito com sucesso para o e-mail: {form_login.email.data}", "alert-success")
        return redirect(url_for('home'))

    if form_criar_conta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criar_conta.senha.data)
        usuario = Usuario(username=form_criar_conta.username.data, email=form_criar_conta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f"Conta criada com sucesso para o e-mail: {form_criar_conta.email.data}", "alert-success")
        return redirect(url_for('home'))      
    
    return render_template("login.html",form_login=form_login, form_criar_conta=form_criar_conta)

