import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song
from src.drinks import Drink

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_1 = Room("Room 1", 2, 10, 100)
        self.room_2 = Room("Room 2", 10, 50, 200)
        self.juanma = Guest("Juanma", 10, "Flaca")
        self.manel = Guest("Manel", 20)
        self.conchi = Guest("Conchi", 30)
        self.flaca = Song("Flaca","Andres Calamaro")
        self.eleanor = Song("Eleanor Rigby", "The Beatles")
        self.rum = Drink("Rum", 5)
        self.vodka = Drink("Vodka", 5)
        self.gin = Drink("Gin", 25)


            ##### MVP TESTS #####
    
    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room_1.name)
    
    def test_room_has_guest_list(self):
        self.assertEqual(0, len(self.room_1.guest_list))

    def test_room_has_playlist(self):
        self.assertEqual(0, len(self.room_1.playlist))

    def test_check_in_guest(self):
        self.room_1.add_guest(self.juanma)
        self.assertEqual(1, len(self.room_1.guest_list))
    
    def test_check_out_guest(self):
        self.room_1.guest_list = [self.manel, self.conchi]
        self.room_1.check_out_guest(self.manel)
        self.assertEqual(1, len(self.room_1.guest_list))

    def test_room_add_song_to_playlist(self):
        self.room_1.add_song_to_playlist(self.eleanor)
        self.assertEqual(1, len(self.room_1.playlist))

    
    def test_room_remove_song_from_playlist(self):
        self.room_1.playlist = [self.flaca, self.eleanor]
        self.room_1.remove_song_from_playlist(self.eleanor)
        self.assertEqual(1, len(self.room_1.playlist))

    def test_room_format_for_devs(self):
        self.assertEqual("Room('Room 1')", self.room_1.__repr__())

            ##### EXTENSIONS TESTS #####

    def test_room_max_capacity(self):
        self.assertEqual(2, self.room_1.room_capacity)

    def test_guest_cant_check_in(self):
        self.room_1.guest_list = [self.juanma, self.manel]
        self.assertEqual("Apologies Conchi, the room is full", self.room_1.check_in_guest(self.conchi))

    def test_guest_can_check_in(self):
        self.room_1.guest_list = [self.manel]
        self.assertEqual("Welcome Juanma", self.room_1.check_in_guest(self.juanma))

    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room_1.entry_fee)

    def test_room_has_till(self):
        self.assertEqual(100, self.room_1.till)

    def test_entry_fee_reduces_guest_money(self):
        self.room_1.check_in_guest(self.manel)
        self.assertEqual(10, self.manel.money)
  
    def test_entry_fee_adds_to_till(self):
        self.room_1.check_in_guest(self.manel)
        self.assertEqual(110, self.room_1.till)

    def test_room_has_drink_stock(self):
        self.assertEqual(0,len(self.room_1.drinks))

    def test_drink_takes_money_from_client(self):
        self.room_1.drinks = [self.rum, self.vodka]
        self.room_1.sell_drink(self.juanma,self.rum)
        self.assertEqual(5, self.juanma.money)

    def test_drink_add_money_to_till(self):
        self.room_1.drinks = [self.rum, self.vodka, self.gin]
        self.room_1.sell_drink(self.juanma,self.rum)
        self.assertEqual(105, self.room_1.till)

    def test_drink_out_of_stock(self):
        self.room_1.drinks = [self.vodka]
        self.assertEqual("Sorry we run out of Rum", self.room_1.sell_drink(self.juanma, self.rum))

    def test_drink_in_stock_broke_client(self):
        self.room_1.drinks = [self.vodka, self.rum, self.gin]
        self.assertEqual("Sorry, that's not enough money", self.room_1.sell_drink(self.juanma, self.gin))

    
