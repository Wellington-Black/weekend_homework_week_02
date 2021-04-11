import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room
from src.drinks import Drink

class TestGuest(unittest.TestCase):

    def setUp(self):

        self.flaca = Song("Flaca", "Andres Calamaro")
        self.eleanor = Song("Eleanor Rigby", "The Beatles")
        self.juanma = Guest("Juanma", 10, "Flaca")
        self.Manel = Guest("Manel", 20)
        self.room_1 = Room("Room 1", 2, 10, 100)
        self.room_2 = Room("Room 2", 10, 50, 200)
        self.rum = Drink("Rum", 5)
        self.vodka = Drink("Vodka", 5)
        self.gin = Drink("Gin", 25)

        ##### MVP TESTS #####

    def test_guest_has_name(self):
        self.assertAlmostEqual("Juanma", self.juanma.name)

    def test_guest_format_for_devs(self):
        self.assertEqual("Guest Juanma", self.juanma.__repr__())

        ##### EXTENSIONS TESTS #####

    def test_has_money(self):
        self.assertEqual(10, self.juanma.money)

        ##### ADVANCED EXTENSIONS TESTS #####

    def test_guest_has_favourite_song(self):
        self.juanma.fav_song = "Flaca"
        self.assertEqual("Flaca", self.juanma.fav_song)

    def test_guest_cheering_if_favourite_song(self):
        self.room_1.playlist = [self.flaca, self.eleanor]
        self.assertEqual("Yeah!", self.juanma.cheering(self.room_1))

    def test_guest_moans_if_no_favourite_song(self):
        self.room_1.playlist = [self.eleanor]
        self.assertEqual("Meh, they don't have my song...🥺", self.juanma.cheering(self.room_1))

    def test_guest_has_buy_drink(self):
        self.juanma.buy_drink(self.rum)
        self.assertEqual(5, self.juanma.money)

    def test_client_buys_drink_sentence(self):
        self.room_1.drinks = [self.rum, self.vodka, self.gin]
        self.assertEqual("I love Rum!", self.juanma.buy_drink(self.rum))
        


    