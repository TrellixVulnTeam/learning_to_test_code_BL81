"""
A class should have one, and only one, responsibility (reason to change)
"""

class Album:
    def __init__(self, name, artist) -> None:
        self.name = name
        self.artist = artist
        self.songs = []

    def add_song(self, song) -> None:
        print(f"adding song: {song}")
        self.songs.append(song)
    
    def remove_song(self, song) -> None:
        print(f"removing song: {song}")
        self.songs.remove(song)

    def __str__(self) -> str:
        return f"Album '{self.name}' by {self.artist}\nTracklist:{self.songs}"

    # breaks the

if __name__ == "__main__":
    album1 = Album("facts", "kevin")
    print(album1)
    album1.add_song("ain't it the truth") 
    print(album1)


    album2 = Album("straight butta", "smoothie")
    print(album2)
    album2.add_song("island on the moon")
    print(album2)
