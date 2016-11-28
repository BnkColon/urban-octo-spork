#!/usr/bin/python
# -*- coding: utf-8 -*-

# Input: Array of distinct characters (e.g. [’a’,’c’,’d’]) and an integer k
# Output: list of all possible strings consisting of exactly k characters from the input
import itertools
import math

def possibleStrings(word, integer):
	for p in itertools.product(word, repeat=integer):
		print p

if __name__ == '__main__':
	num_array = ['a', 'b', 'c'] # List of characters
	integer = 3
	word = '' #String containing all the characters in num_array

	# Create a string with the characters
	for c in num_array:
		word += c

	possibleStrings(word, integer)
	