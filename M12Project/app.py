from flask import Flask
from SongClass import Song
from PlaylistClass import PlaylistManager

app = Flask(__name__)

playlist = PlaylistManager()

song= Song()

@app.route("/")
def all_songs():
   
   return song.list
@app.route("/create_song")
def add_song():
   
   title = input("What is the title of the new song? ")
   artist = input("Who is the artist of the new song? ")
   genre = input("What is the genre of the new song? ")
   return song.create_song(title, artist, genre)

@app.route("/update_song")
def update_song():
   title = input ("Which song do you want to update? ")
   change = input("What would you like to update? (title/artist/genre) ")
   return song.update_song(title, change)

@app.route("/get_song")
def get_song():
   
   
   return song.get_song()

@app.route("/delete_song")
def delete_song():
   title = input ("Which song do you want to delete? ")
   return song.delete_song(title)

@app.route("/create_playlist")
def create_playlist():
   
   new_song= song.get_song()
   return playlist.add_song(new_song)

@app.route("/modify_playlist")
def modify_playlist():
   change= input("Would you like to add or delete a song? ")
   if change == 'add':
      new_song= song.get_song()
      return playlist.add_song(new_song)
   elif change == 'delete':
      title = input("Which song do you wish to delete?(title only) ")
      if playlist.delete_song(title):
         return f"Song: {title} was deleted from the playlist"
   else:
      return "Please enter either add or delete."
   
@app.route("/get_playlist")
def get_playlist():
   return playlist.get_playlist()
      





if __name__ == '__main__':  
   app.run(debug=True)