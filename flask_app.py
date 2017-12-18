
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

# Instanciar o Flask
app = Flask(__name__)
# Ativar o DEBUG
app.config["DEBUG"] = True

# Informaçoes do banco de dados para o SQLAlchemy fazer a conexao
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="DocMcCoy",
    password="senha123",
    hostname="DocMcCoy.mysql.pythonanywhere-services.com",
    databasename="DocMcCoy$comments",
)
# Configuracoes do SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Instanciar o DB
db = SQLAlchemy(app)

# Classe que sera armazenada no banco, com seus respectivos campos
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# Index, com seus respectivos metodos
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", comments=Comment.query.all())
    # caso o metodo seja "POST":
    comment = Comment(content=request.form['contents'])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('index'))
