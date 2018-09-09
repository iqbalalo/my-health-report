from flask import Flask
from flask_cors import CORS
from modules.main.app import main_blueprint


app = Flask(__name__)
CORS(app)
app.config.from_object('config.DevelopmentConfig')

# Register blueprints
app.register_blueprint(main_blueprint)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)