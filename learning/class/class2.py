#!/usr/bin/env python

class Song(object):
	"""This is for song lyrics"""
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_along(self):
		for line in self.lyrics:
			print line

song1 = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])
song2 = Song(["They rally around the family", "With pockets full of shells"])

song1.sing_along()
song2.sing_along()
