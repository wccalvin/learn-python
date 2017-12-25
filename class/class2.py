#!//usr/local/bin/python2

class Song(object):
    """This is for song lyrics"""
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_along(self):
        for line in self.lyrics:
            print line

song1 = Song(['I found a love for me', 'Darling just dive right in',
              'And follow my lead'])

song1.sing_along()
