from flask import Flask,render_template
from . import db
app = Flask(__name__)

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