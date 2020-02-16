from flask import Flask


def create_app():
    app = Flask(__name__)
    
    app.config['MONGO_URI'] = 'mongodb+srv://npysklyw:hackathon@cluster0-g1qmd.gcp.mongodb.net/test?retryWrites=true&w=majority'

    from .db import mongo
    mongo.init_app(app) 
    
    from .views import main
    app.register_blueprint(main)

    return app
