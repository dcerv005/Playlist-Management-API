
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






# class Node:
#     def __init__(self, song):
#         self.song = song
#         self.prev=None
#         self.next=None

# class PlaylistManager:
#     def __init__(self):
#         self.head=None
#         self.tail=None

#     def add_song(self, song):
#         new_song = song
#         new_node=Node(new_song)

#         if not self.head:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next=new_node
#             new_node_prev=self.tail
#             self.tail =new_node
#         return f"Song: {song['title']} was added to the playlist"
#     def delete_song(self, title):
#         current = self.head
#         while current:
#             if current.song['title'] == title:
#                 if current == self.head:        
#                     self.head = current.next
#                 if current == self.tail:
#                     self.tail = current.prev
#                 if current.prev:
#                     current.prev.next = current.next
#                 if current.next:
#                     current.next.prev=current.prev
                
#                 return True
#             current = current.next
#         return False
    
#     def get_playlist(self):
#         if not self.head:
#             return "Playlist is empty"
#         current=self.head
#         list_songs=[]
#         while current:
#             list_songs.append(current.song)
#             current=current.next
#         return list_songs


    
        
        