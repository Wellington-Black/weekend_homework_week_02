from src.room import Room
from src.song import Song
from src.guest import Guest

juanma = Guest("Juanma", 10, "Flaca")
manel = Guest("Manel", 20)
conchi = Guest("Conchi", 30)
carra = Guest("Carra", 100, "Tranquility Base Hotel & Casino")

flaca = Song("Flaca","Andres Calamaro")
eleanor = Song("Eleanor Rigby", "The Beatles")
hotel_and_casino = Song("Tranquility Base Hotel & Casino", "Arctic Monkeys")


room_1 = Room("room 1",2, 10, 100)
room_2 = Room("room 2", 10, 10, 200)
room_3 = Room("room 3", 20, 200, 1000)


room_1.check_in_guest(juanma)
room_1.check_in_guest(manel)

room_1.check_out_guest(manel)

print(room_1.playlist)

room_1.add_song_to_playlist(flaca)

print(room_1.playlist)

print(juanma.cheering(room_1))
print(manel.cheering(room_1))

print(room_1.check_in_guest(conchi))
print(room_1.check_in_guest(carra))

print(juanma.money)
print(conchi.money)
print(carra.money)

print(room_1.till)



print(room_1.guest_list)



room_1.add_song_to_playlist(eleanor)

room_2.add_song_to_playlist(eleanor)

print(type(flaca))






