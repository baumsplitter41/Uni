class MyClass:
    x = 5
    y = 3
    z = 8
p1 = MyClass()
p2 = MyClass()
p3 = MyClass()
print(p1.x)
print(p2.x+5)
print(p3.y,p3.z)

#Leere Klasse:
class lClass:
    pass

print("------------------------------------------------")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 18)
p2 = Person("Tobias", 25)
p3 = Person("Max", 30)

del p3.age 

p1.greet()
print(p1.name, p1.age)
p2.greet()
print(p2.name, p2.age)
#print(p3.age) -> causes error

print("------------------------------------------------")

class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Mondeo", 2014)
car1.display_info()
car2.display_info()
print(car2.brand)

print("------------------------------------------------")

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.add_song("Jump")
my_playlist.show_songs()
my_playlist.remove_song("Jump")
my_playlist.show_songs()
