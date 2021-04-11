class Song:

    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

    def __repr__(self):
        return f"{self.name} by {self.artist}"

    def __str__(self):
        return f"Song {self.name} by {self.artist}"