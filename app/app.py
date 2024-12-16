import os
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo.errors import ConnectionFailure, DuplicateKeyError
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'miclavesecreta'  # Necesaria para usar 'flash'

# Configuración para recargar automáticamente los templates
app.config["DEBUG"] = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Conexión a MongoDB
mongo_host = os.getenv('MONGO_HOST', 'mongo')
mongo_root_username = os.getenv('MONGO_USER', False)
mongo_root_password = os.getenv('MONGO_PASSWORD', False)
mongo_port = os.getenv('MONGO_PORT', 27017)

client = MongoClient(
    host=mongo_host,
    port=int(mongo_port),
    username=str(mongo_root_username),
    password=str(mongo_root_password)
)

mongo_db = os.getenv('MONGO_DATABASE', 'dataBaseJuegosDeMesa')
db = client[mongo_db]
coleccion = db['juegos']

@app.route('/')
def home():
    juegos = list(coleccion.find())
    return render_template('index.html', juegos=juegos)

@app.route('/add', methods=['POST'])
def create():
    
    juego = {
        "_id": request.form['id'],
        "nombre": request.form['nombre'],
        "jugadores_min": int(request.form['min_jugadores']),
        "jugadores_max": int(request.form['max_jugadores']),
        "limite_edad": request.form['limite_edad'],
        "pais_origen": request.form['pais_origen'],
        "costo": float(request.form['costo'])
    }
    try:
        coleccion.insert_one(juego)
        flash('Juego creado exitosamente.', 'success')
    except DuplicateKeyError:
        flash('Error: El ID ya existe. Por favor, elige un ID único.', 'error')
    except Exception as e:
        flash(f'Error al crear juego: {e}', 'error')
    return redirect(url_for('home'))

@app.route('/edit/<game_id>', methods=['GET', 'POST'])
def update(game_id):
    if request.method == 'GET':
        juego = coleccion.find_one({"_id": game_id})
        if not juego:
            flash('Error: El juego no existe.', 'error')
            return redirect(url_for('home'))
        return render_template('edit_game.html', juego=juego)

    if request.method == 'POST':
        nuevo_id = request.form['id']
        updated_game = {
            "_id": nuevo_id,
            "nombre": request.form['nombre'],
            "jugadores_min": int(request.form['min_jugadores']),
            "jugadores_max": int(request.form['max_jugadores']),
            "limite_edad": request.form['limite_edad'],
            "pais_origen": request.form['pais_origen'],
            "costo": float(request.form['costo'])
        }
        try:
            if nuevo_id != game_id:
                coleccion.insert_one(updated_game)
                coleccion.delete_one({"_id": game_id})
            else:
                coleccion.update_one({"_id": game_id}, {"$set": updated_game})
            flash('Juego actualizado exitosamente.', 'success')
        except DuplicateKeyError:
            flash('Error: No se puede cambiar el ID al de un juego existente.', 'error')
        except Exception as e:
            flash(f'Error al actualizar el juego: {e}', 'error')
        return redirect(url_for('home'))

@app.route('/delete/<game_id>', methods=['POST'])
def delete(game_id):
    try:
        coleccion.delete_one({"_id": game_id})
        flash('Juego eliminado exitosamente.', 'success')
    except Exception as e:
        flash(f'Error al eliminar juego: {e}', 'error')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
