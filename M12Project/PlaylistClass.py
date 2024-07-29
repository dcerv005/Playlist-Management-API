
class Node:
    def __init__(self, song):
        self.song = song
        self.prev=None
        self.next=None

class PlaylistManager:
    def __init__(self):
        self.head=None
        self.tail=None

    def add_song(self, song):
        new_song = song
        new_node=Node(new_song)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next=new_node
            new_node_prev=self.tail
            self.tail =new_node
        return f"Song: {song['title']} was added to the playlist"
    def delete_song(self, title):
        current = self.head
        while current:
            if current.song['title'] == title:
                if current == self.head:        
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev=current.prev
                
                return True
            current = current.next
        return False
    
    def get_playlist(self):
        if not self.head:
            return "Playlist is empty"
        current=self.head
        list_songs=[]
        while current:
            list_songs.append(current.song)
            current=current.next
        return list_songs


    
        
        