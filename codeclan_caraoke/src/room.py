class Room:

    def __init__(self, name, room_capacity, entry_fee, till):
        self.name = name
        self.guest_list = []
        self.playlist = []
        self.room_capacity = room_capacity
        self.entry_fee = entry_fee
        self.till = till
        self.drinks = []
        

    def add_guest(self, guest):
        self.guest_list.append(guest)
    
    def check_out_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song_to_playlist(self, song):
       self.playlist.append(song)
       
    def remove_song_from_playlist(self, song):
        self.playlist.remove(song)
    
    def __repr__(self):
        return "Room('{}')".format(self.name)

    def check_in_guest(self, guest):
        if self.room_capacity > len(self.guest_list):
            guest.money -= self.entry_fee
            self.till += guest.money
            self.add_guest(guest)
            return f"Welcome {guest.name}"
        else:
            return f"Apologies {guest.name}, the room is full"

    
    def sell_drink(self, guest, drink):
        if drink in self.drinks and guest.money >= drink.price:
            self.till += drink.price
            guest.buy_drink(drink)
            return f"Enjoy your {drink}"
        elif drink not in self.drinks:
            return f"Sorry we run out of {drink}"
        else:
            return "Sorry, that's not enough money"
        