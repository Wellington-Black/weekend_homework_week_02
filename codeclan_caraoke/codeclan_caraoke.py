from src.room import Room
from src.song import Song
from src.guest import Guest
from src.drinks import Drink

rock_room = Room("Rock Room", 10, 10, 1000)
reggae_room = Room("Reggae Room", 10, 10, 1000)
pop_room = Room("Pop Room", 10, 10, 1000)

#Rock Songs
cydonia = Song("Knights of Cydonia", "Muse")
byoby = Song("B.Y.O.B", "System Of A Down")
rock = Song("Rock is Dead", "Marilyn Manson")
rock_room.playlist = [cydonia, byoby, rock]

#Reggae Songs
reggae_songs = redemption = Song("Redemption Song", "Bob Marley")
milk = Song("Milk and Honey", "Hollie Cook")
ship = Song("Tight Ship", "Stephen Marley and Damian Marley")
reggae_room.playlist = [redemption ,milk, ship]

#Pop Songs
oops = Song("Opps!... I did it Again", "Britney Spears")
rolling = Song("Rolling in the Deep", "Adele")
river = Song("Cry Me a River", "Justin Timberlake")
pop_room.playlist = [oops, rolling, river]

#Drinks
rum = Drink("Rum", 5)
vodka = Drink("Vodka", 5)
gin = Drink("Gin", 25)

#Stock
rock_room.drinks = [vodka, gin]
reggae_room.drinks = [rum,vodka]
pop_room.drinks = [gin, rum]



def create_guest():
   print("Hello, Welcome to Codeclan Caraoke \n Please enter your details")
   global guest
   guest = Guest.from_guest_input()
   

def main_menu():
  print(f"Hello {guest.name}! Pick an option from the menu: \n 1: Rock Room \n 2: Reggae Room \n 3: Pop Room \n 4: Go home ")

def rock_room_menu():
  print(f"Welcome to the {rock_room.name} {guest.name}! what would you like to do next? \n 1: Choose a song \n 2: Order a drink \n 3: Go home")

def reggae_room_menu():
  print(f"Welcome to the {reggae_room.name} {guest.name}! what would you like to do next? \n 1: Choose a song \n 2: Order a drink \n 3: Go home")  

def pop_room_menu():
  print(f"Welcome to the {pop_room.name} {guest.name}! what would you like to do next? \n 1: Choose a song \n 2: Order a drink \n 3: Go home")

def pick_from_main_menu():
  first_choice = input(main_menu())
  loop = True
  #ROCK ROOM
  while loop == True:
    if int(first_choice) == 1:
      second_choice = input(rock_room_menu())
      if int(second_choice) == 1:
        print(guest.cheering(rock_room))
        second_choice
      elif int(second_choice) == 2:
        print(rock_room.sell_drink(guest, gin))
        second_choice
      elif int(second_choice) == 3:
        print("Have a good night")
        break
  #REGGAE ROOM
    elif int(first_choice) == 2:
      second_choice = input(reggae_room_menu())
      if int(second_choice) == 1:
        print(guest.cheering(reggae_room))
        second_choice
      elif int(second_choice) == 2:
        print(rock_room.sell_drink(guest, rum))
        second_choice
      elif int(second_choice) == 3:
        print("Have a good night")
        break
  
  #POP ROOM
    elif int(first_choice) == 3:
      second_choice = input(pop_room_menu())
      if int(second_choice) == 1:
        print(guest.cheering(pop_room))
        second_choice
      elif int(second_choice) == 2:
        print(rock_room.sell_drink(guest, vodka))
        second_choice
      elif int(second_choice) == 3:
        print("Have a good night")
        break
    elif int(first_choice) == 4:
      print("Have a good night")
      break

create_guest()
print(guest.fav_song)
pick_from_main_menu()

