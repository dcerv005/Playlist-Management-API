
class Playlist:
    def __init__(self):
      self.list={}

    def create_playlist(self, playlist_name):
        if playlist_name['name'] in self.list:
           return f"Playlist, {playlist_name['name']}, already exists"
        else: 
            self.list[playlist_name['name']]=[]
            return f'{playlist_name['name']}, created'
        
    def get_playlist(self, name):

        if name in self.list:
            return self.list[name]
        else:
            return "Playlist does not exist"
        
    def add_song(self, playlist_name, song):
        if playlist_name in self.list:
            if song['title'] in self.list[playlist_name]:
                return f'{song['title']} is already in this playlist'
           
            self.list[playlist_name].append(song['title'])
            return f'{song['title']} was added to {playlist_name}'
        else:
            return f'{playlist_name} doesnt exist in list of playlists'
    
    def delete_song(self, playlist, song_name):
        if playlist in self.list:
            if song_name not in self.list[playlist]:
                return f'{song_name} is not in this playlist'
           
            self.list[playlist].remove(song_name)
            return f'{song_name} was removed from {playlist}'
        else:
            return f'{playlist} doesnt exist in list of playlists'
        
    def delete_playlist(self, title):
      if title in self.list:
         self.list.pop(title)
         return f"{title} was removed"
      else:
         return "playlist does not exist"









    
        
        
