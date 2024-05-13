from flask import Flask,render_template

app = Flask(__name__)

with app.app_context():
   from . import db
   db.init_app(app)

@app.route('/')
def hello():
   return 'Hello, World!'

@app.route('/artistas')
def artistas():
   consulta = """
       SELECT Name FROM artists;
    """

   con = db.get_db()
   res = con.execute(consulta)
   lista_artistas = res.fetchall()
   pagina = render_template('artista.html',artistas=lista_artistas)
   return pagina