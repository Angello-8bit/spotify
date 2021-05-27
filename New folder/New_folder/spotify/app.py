from os import getenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from .models import DB, Track, Song_Cluster, Song_NN, Output
from .spotify import get_info_and_add, get_features_nn, get_predictions_nn

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://thtzecnljihlkk:f550535265a8ebabf35ec13099e02e0a6c1b44531d86e31cdeb5af9c082a6847@ec2-18-204-101-137.compute-1.amazonaws.com:5432/d37n857kndi13e'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)
    

    @app.route("/")
    def root():
        return render_template("base.html")


    @app.route("/user_submitted", methods=["GET", "POST"])
    def user_submitted():

        track_name = request.form
        model_input = get_features_nn(track_name['track_name'])
        track_names = get_predictions_nn(model_input)

        return render_template("user.html", track_name=track_name['track_name'], tracks=track_names)
    
    @app.route("/about")
    def about():
        return render_template("about.html")
    
    return app

