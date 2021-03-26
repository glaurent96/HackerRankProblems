#!/bin/python3

# COUNT LETTER FREQUENCY

word = input("Enter a word: ")

ALPHABET=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(0,26):
    if word.count(Alphabet[i]) != 0 or word.count(ALPHABET[i]) != 0:
        print(ALPHABET[i],":",word.count(Alphabet[i]) + word.count(ALPHABET[i]))