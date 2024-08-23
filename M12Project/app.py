from flask import Flask, request, jsonify
from SongClass import Song
from PlaylistClass import Playlist

app = Flask(__name__)

playlist = Playlist()

song= Song()

@app.route("/")
def all_songs():
   
   return song.list

@app.route("/songs", methods=['POST'])
def add_song():
   song_data= request.json
   print(song_data)
   title = song_data['title']
   artist = song_data['artist']
   genre = song_data['genre']
   response = song.create_song(title, artist, genre)
   return jsonify({'message' : response})

@app.route("/update_song/<string:title>", methods=['PUT'])
def update_song(title):
   song_updated_data = request.json
   
   return song.update_song(title, song_updated_data)

@app.route("/songs/<string:title>", methods=['GET'])
def get_song(title):
   
   
   return jsonify(song.get_song(title))

@app.route("/delete_song/<string:title>", methods=['DELETE'])
def delete_song(title):
   
   return song.delete_song(title)

@app.route("/create_playlist", methods=['POST'])
def create_playlist():
   playlist_name=request.json
   
   return playlist.create_playlist(playlist_name)

@app.route("/playlist/<string:playlist_name>", methods=['GET'])
def get_playlist(playlist_name):
   
   
   return jsonify(playlist.get_playlist(playlist_name))

@app.route("/add_to_playlist", methods=['POST'])
def add_song_to_playlist():
   playlist_data=request.json
   song_name = playlist_data["song_name"]
   adding_song=song.get_song(song_name)
   playlist_name = playlist_data["playlist_name"]
   
   return jsonify(playlist.add_song(playlist_name, adding_song))

@app.route("/remove_from_playlist", methods=['DELETE'])
def remove_from_playlist():
   remove_data=request.json
   playlist_name = remove_data['playlist']
   song_name= remove_data['song_name']
   return jsonify(playlist.delete_song(playlist_name, song_name))

@app.route("/delete_playlist/<string:playlist_name>", methods=['DELETE'])
def delete_playlist(playlist_name):

   return playlist.delete_playlist(playlist_name)


   

      





if __name__ == '__main__':  
   app.run(debug=True)