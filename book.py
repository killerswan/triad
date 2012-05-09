# Kevin Cantu
# May 2012

import string
import random

# example usage of this file
def USAGE():
   exec open ("book.py")
   words = openBook("/home/kevin/Desktop/pg2009.txt")  # Darwin's Origin of Species, from Gutenberg
   randomWords(words,5)

# grab some words
def randomWords(book, nn):
   blen = len(book)
   words = []

   for ii in range(nn):
      rnd = random.randrange(0, blen)
      words.append(book[rnd])

   return words

# import the book
def openBook(path):
   text = open(path).read()
   text_ = "".join(map(replacements, text))
   words = text_.split()
   return filter(notEmpty, filter(freqFilter, map(adjustCase, words)))

def replacements(ch):
   if ch in string.punctuation:
      return " "
   elif not ch in string.printable:
      return " "
   else:
      return ch

def adjustCase(word):
   filtered = word
   converted = str.lower(filtered)
   return converted

def notEmpty(word):
   # remove empty words
   # remove single-letter words
   return len(word) > 1

def freqFilter(word):
   # 100 most common english words...
   mostCommon = [
      "the", "be", "to", "of", "and", "a", "in", "that", "have", "I", 
      "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", 
      "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", 
      "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", 
      "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", 
      "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", 
      "person", "into", "year", "your", "good", "some", "could", "them", "see", "other", 
      "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", 
      "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
      "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"
   ]

   return not word in mostCommon[0:50]


