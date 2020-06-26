from observer import User
import publisher

# help(publisher)

print()
dir(publisher)

exit()

simon = User('Simon')
tina = User('Tina')   

jazz = publisher.Jazz()
jazz.attach(simon)
jazz.attach(tina)
jazz.add_track('Hello, this is a track')

funk = publisher.Funk()
funk.attach(simon)
funk.add_track('wooo, funk track')

simon.play_songs()