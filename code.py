#!/usr/bin/python
# -*- coding: utf-8 -*-

# Input: Array of distinct characters (e.g. [’a’,’c’,’d’]) and an integer k
# Output: list of all possible strings consisting of exactly k characters from the input
import itertools

def possibleStrings(word, integer):
	counter = 0
	# Creates the permutations
	for p in itertools.product(word, repeat=integer):
		print p
		counter += 1
	print "The total of permutations was %s." % (counter)

def askForArray():
	# Asks for the elements in the array
	char_array = list()
	num = raw_input("Enter how many elements you want in your list:")
	print 'Enter numbers in array: '
	for i in range(int(num)):
		n = raw_input("num :")
		char_array.append(n)
	print 'ARRAY: ',char_array
	return char_array

def askForInteger():
	# Asks for the integer k
	integer = raw_input("Enter the integer k:")
	return int(integer)

def createWord(char_array):
	# Create a string with the characters
	word = '' # String containing all the characters in char_array

	for c in char_array:
		word += c	
	return word

if __name__ == '__main__':
	possibleStrings(createWord(askForArray()), askForInteger())
	