import os, json
import requests_oauthlib, requests
import flask, flask_socketio
from spotify import Spotify


app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app) 
music_library = Spotify()

@app.route('/')
def hello():
    return flask.render_template('index.html')
    
@socketio.on('connect') 
def on_connect():
    print('Someone connected!')

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')

@socketio.on('query created') 
def on_query_created(data):
    print('Got the artist name:', data)
    
    artist = data['query']
    albums = music_library.get_artists_albums(artist)
    print(albums)
    
    socketio.emit('albums received', { 
        'albums': albums,
    })
    
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)