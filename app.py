from flask import Flask, request, jsonify
from database import get_collection
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)


MONGO_URI = "mongodb+srv://harutselartspain:kakulik5@university.to34f.mongodb.net/UNIVERSITYuniversity?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URI)
    db = client["univesity"]
    programs_collection = db["Programs"]

    # Intentar obtener los datos
    programs = list(programs_collection.find({}, {'_id': 0}))
    print("Programas encontrados:", programs)

except Exception as e:
    print("Error de conexión o consulta:", e)

#@app.route('/programs', methods=['GET'])
#def get_programs():
 #   try:
  #      # Obtener todos los documentos de la colección 'Programs'
   #     programs = list(programs_collection.find({}, {'_id': 0}))  # Excluir el campo `_id`
    #    return jsonify(programs), 200  # Devolver en formato JSON con código 200 OK
   # except Exception as e:
        # Manejo de errores en la conexión o consulta
    #    return jsonify({"error": str(e)}), 500

#if __name__ == "__main__":
 #   app.run(host="0.0.0.0", port=5000, debug=True)

# @app.route('/programs', methods=['GET'])
# def get_programs():
#     try:
#         # Conectar a la colección 'Programs'
#         collection = get_collection('Programs')
#         programs = list(collection.find({}, {'_id': 0}))  # Excluir `_id`
#         return jsonify(programs), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

@app.route('/programs', methods=['POST'])
def create_program():
    try:
        # Conectar a la colección 'Programs'
        collection = get_collection('Programs')
        data = request.json
        collection.insert_one(data)
        return jsonify({"message": "Program added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
