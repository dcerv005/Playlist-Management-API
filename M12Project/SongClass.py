class Song:
   def __init__(self):
      self.list={}
   
   def create_song(self, title, artist, genre):
      
        if title in self.list and self.list[title]["artist"] == artist:
            return "Song already exists"
        
        self.list[title]={"title": title, "artist": artist, "genre": genre}
        return f"{title} was added."

   def update_song(self, title, updated_data):
      if title not in self.list:
         return "Song does not exist"
          
      if title != updated_data['title']:
         self.list[updated_data['title']] = self.list.pop(title)
         self.list[updated_data['title']]['title'] = updated_data['title']
         self.list[updated_data['title']]['artist']=updated_data['artist']
         self.list[updated_data['title']]['genre']=updated_data['genre']

         return f"Song, {updated_data['title']} updated"
      if title == updated_data['title']:
         self.list[updated_data['title']]['artist']=updated_data['artist']
         self.list[updated_data['title']]['genre']=updated_data['genre']

         return f"Song, {title} updated"

      else: 
         return "Invalid input"

   def delete_song(self, title):
      if title in self.list:
         self.list.pop(title)
         return f"{title} was removed"
      else:
         return "Song does not exist"

   def get_song(self, title):
      
      if title in self.list:  #linear search
         return self.list[title]
      else:
         return "Song does not exist"
  
   # def get_songs(self):
      
   #    return self.list