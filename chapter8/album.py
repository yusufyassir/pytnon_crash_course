def make_album(a_name, a_title):
    """returns album atrist and title in dictionary"""
    album = {'artist' : a_name, 'title' : a_title, }
    return album
#title = input("enter albums title: ")
#artist = input("enter albums artist: ")

#album = make_album(artist, title)

#print(f"the album {album['title'].title()} is made by {album['artist'].title()}.")

def make_album1(a_name, a_title, a_songs):
    """returns album, atrists, no. of songs"""
    al = {'artist' : a_name, 'title' : a_title, 'songs' : a_songs}
    return al

title = input("\nenter albums title: ")
artist = input("enter albums artist: ")
songs = input("enter albumssong number: ")

album = make_album1(artist, title, songs)

print(f"\nthe album {album['title'].title()} is made by {album['artist'].title()}.")
print(f"and has {album['songs']} songs.")