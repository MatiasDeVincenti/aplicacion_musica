from flask import Flask,render_template
from . import db
app = Flask(__name__)

@app.route('/canciones')
def canciones():
   consulta = """
       SELECT Name, Milliseconds, Composer FROM tracks;
    """

   con = db.get_db()
   res = con.execute(consulta)
   lista_canciones = res.fetchall()
   pagina = render_template('canciones.html',canciones=lista_canciones)
   return pagina