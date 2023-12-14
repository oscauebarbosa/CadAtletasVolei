from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'Senai'


class  volleyball_players:
    def __init__(self, nome, idade, posicao, experiencia, cidade, estado, dia, hora):
        self.nome = nome
        self.idade = idade
        self.posicao = posicao
        self.experiencia = experiencia
        self.cidade = cidade
        self.estado = estado
        self.dia = dia
        self.hora = hora


lista = []


@app.route('/atletas')
def  volleyball_players2():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Volei.html', Titulo ="Atletas: ", ListaAtletas = lista)


@app.route('/cadastro')
def cadastro():
    if 'Usuario_Logado' not in session:
        return redirect('/')
    else:
        return render_template('Cadastro.html', Titulo = "Cadastro de Atletas")


@app.route('/criar', methods= ['POST'])
def criar():
    if 'salvar' in request.form:
        nome = request.form['nome']
        idade = request.form['idade']
        posicao = request.form['posicao']
        experiencia = request.form['experiencia']
        cidade = request.form['cidade']
        estado = request.form['estado']
        dia = request.form['dia']
        hora = request.form['hora']
        obj =  volleyball_players(nome, idade, posicao, experiencia, cidade, estado, dia, hora)
        lista.append(obj)
        return redirect('/atletas')
    elif 'deslogar' in request.form:
        return redirect('/')


@app.route('/excluir/<nomeatletas>', methods=['GET','DELETE'])
def excluir(nomeatletas) :
    for i, atletas in enumerate(lista):
        if atletas.nome == nomeatletas:
            lista.pop(i)
            break
    return redirect('/atletas')

@app.route('/editar/<nomeatletas>', methods=['GET'])
def editar(nomeatletas):
    for i, atletas in enumerate(lista):
        if atletas.nome == nomeatletas:
            return render_template("Editar.html", atletas=atletas, Titulo="Alterar Atletas")

@app.route('/alterar', methods = ['POST','PUT'])
def alterar():
    nome = request.form['nome']
    for i, atletas in enumerate(lista):
        if atletas.nome == nome:
            atletas.nome = request.form['nome']
            atletas.idade = request.form['idade']
            atletas.posicao = request.form['posicao']
            atletas.experiencia = request.form['experiencia']
            atletas.cidade = request.form['cidade']
            atletas.estado = request.form['estado']
            atletas.dia = request.form['dia']
            atletas.hora = request.form['hora']

    return redirect('/atletas')


@app.route('/')
def login():
    session.clear()
    return render_template('Login.html', Titulo = "Faça seu login")


@app.route('/autenticar', methods = ['POST'])
def autenticar():
    if request.form['usuario'] == 'Caue' and request.form['senha']=='123':
        session['Usuario_Logado'] = request.form['usuario']
        flash('Usuario Logado com Sucesso')
        return redirect('/cadastro')
    else:
        flash('Usuario não encontrado')
        return redirect('/')




if __name__ == '__main__':
    app.run()