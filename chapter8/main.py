#import album1
#from album1 import make_album1
#from album1 import make_album1 as mm
#import album1 as mm
from album1 import *
album = make_album1('dave', 'psychodrama', 11)

print(f"\nthe album {album['title'].title()} is made by {album['artist'].title()}.")
print(f"and has {album['songs']} songs.")