class Song:
    def __init__(self, title):
        self.title = title
        self.prev = None
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, title):
        new_song = Song(title)
        if not self.head:
            self.head = self.tail = self.current = new_song
        else:
            self.tail.next = new_song
            new_song.prev = self.tail
            self.tail = new_song
        print(f"Added: {title}")

    def delete_song(self, title):
        temp = self.head
        while temp:
            if temp.title == title:
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev
                if self.current == temp:
                    self.current = temp.next if temp.next else temp.prev
                print(f"Deleted: {title}")
                return
            temp = temp.next
        print("Song not found")

    def play_next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            print("Playing:", self.current.title)
        else:
            print("End of playlist")

    def play_previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            print("Playing:", self.current.title)
        else:
            print("Start of playlist")

    def show_current(self):
        if self.current:
            print("Playing:", self.current.title)
        else:
            print("No song playing")

    def show_playlist(self):
        print("\nFull Playlist:")
        temp = self.head
        if not temp:
            print("Playlist is empty")
            return
        while temp:
            print("-", temp.title)
            temp = temp.next

# Main Program
playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")

while True:
    print("\nOptions:")
    print("1. Add Song")
    print("2. Delete Song")
    print("3. Play Next")
    print("4. Play Previous")
    print("5. Show Current Song")
    print("6. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Enter song title: ")
        playlist.add_song(title)
    elif choice == "2":
        title = input("Enter song title to delete: ")
        playlist.delete_song(title)
    elif choice == "3":
        playlist.play_next()
    elif choice == "4":
        playlist.play_previous()
    elif choice == "5":
        playlist.show_current()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice")

# Show full playlist after exit
playlist.show_playlist()
