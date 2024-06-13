from flask import Flask, render_template
from database import db
from routes.products import bp

app = Flask(__name__)

# Configuración de la conexión a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(bp, url_prefix='/products')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
