class Song:
   def __init__(self):
      self.list={}
   
   def create_song(self, title, artist, genre):
      
        if title in self.list and self.list[title]["artist"] == artist:
            return "Song already exists"
        
        self.list[title]={"title": title, "artist": artist, "genre": genre}
        return f"{title} was added."

   def update_song(self, title, change):
      if title not in self.list:
         return "Song does not exist"
      new= input(f"What will you like to change the {change} to? ")
     
      if change  == 'title':
         self.list[new] = self.list.pop(title)
         self.list[new]['title']=new
         return f"The {change} of the song: {title} was updated"
      elif change == 'artist':
         self.list[title][change]=new
         return f"The {change} of the song: {title} was updated"
      elif change == 'genre': 
         self.list[title][change]=new
         return f"The {change} of the song: {title} was updated"
      else: 
         return "Invalid input"

   def delete_song(self, title):
      if title in self.list:
         self.list.pop(title)
         return f"{title} was removed"
      else:
         return "Song does not exist"

   def get_song(self):
      title= input("Which song are you looking for? ")
      if title in self.list:
         return self.list[title]
      else:
         return "Song does not exist"