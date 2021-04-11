import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.flaca = Song("Flaca","Andres Calamaro")

            ##### MVP TESTS #####

    def test_song_has_name(self):
        self.assertEqual("Flaca", self.flaca.name)

    def test_song_has_artist(self):
        self.assertEqual("Andres Calamaro", self.flaca.artist)
    
    def test_song_format_for_devs(self):
        self.assertEqual("Flaca by Andres Calamaro", self.flaca.__repr__())

    def test_song_format_for_user(self):
        self.assertEqual("Song Flaca by Andres Calamaro", self.flaca.__str__())
        
            ##### EXTENSIONS TESTS #####
    