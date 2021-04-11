class Guest:
    
    def __init__(self,name=None,money=None, fav_song=None):
        self.name = name
        self.money = money
        self.fav_song = fav_song

    @classmethod
    def from_guest_input(cls):
        return cls(
            input('Name: '),
            int(input('Money: ')), 
            input('Favorite song: '),
        )

    def __repr__(self):
        return f"Guest {self.name}"

    def cheering(self, room):
        for song in room.playlist:
            if song.name == self.fav_song:
                return "Yeah!"
            
        return "Meh, they don't have my song...🥺"

    def buy_drink(self, drink):
        self.money -= drink.price
        return f"I love {drink}!"



