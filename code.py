#!/usr/bin/python
# -*- coding: utf-8 -*-

# Input: Array of distinct characters (e.g. [’a’,’c’,’d’]) and an integer k
# Output: list of all possible strings consisting of exactly k characters from the input

num_array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    num_array.append(int(n))
print 'ARRAY: ',num_array