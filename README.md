# urban-octo-spork
Introduction to the Theory of Computation Class Assignment

Program that takes as input an array of distinct characters (e.g. [’a’,’c’,’d’]) and an integer k, and outputs a list of all possible strings consisting of exactly k characters from the input. Each possible string should appear only once in the output.

Example: 
Input = [a, b, c]
k = 3


Output:
1) aaa

2) aab

3) aba

4) baa

5) aac

6) aca

7) caa

8) abc

9) acb

10) bac

11) cab

12) ccc

13) cca

14) cac

15) acc

16) ccb

17) cbc

18) bcc

19) bbb

20) bba

21) bab

22) abb

23) bbc

24) bcb

25) cbb

26) bca

27) cba

This is just permutations, so for an array of size N and strings of length K, we would have N<sup>K</sup> possible strings. 

In this example the array is of size 3 and k = 3, the number of possible strings of length 3 is 3<sup>3</sup>, or 27. If k = 6, then we can have 3<sup>6</sup> possible strings, and so on.

