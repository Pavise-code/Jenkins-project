from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "API Jenkins opérationnelle sur Windows !"

if __name__ == "__main__":
    # On laisse 'debug=True' pour que notre futur scan de sécurité (Bandit) 
    # détecte une erreur et nous alerte.
    app.run(host="0.0.0.0", port=5000, debug=True)