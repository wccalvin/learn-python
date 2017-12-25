#!//usr/local/bin/python2

class Stuff(object):

    def __init__(self):
        self.idea = "This is just a variable stored"

    def apple(self):
        return "I am Apple!"

thing = Stuff()
print thing.apple()
print thing.idea
