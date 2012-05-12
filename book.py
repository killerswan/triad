# Kevin Cantu
# May 2012

import string
import json
import codecs

def test1():
   # as regular strings (why?)
   book.bookToJSON("pg2009.txt", "oos.json")
   words = loadWordsJSON("oos.json")

def loadWordsJSON(path):
   j = codecs.open(path, "r", "utf-8")
   words = json.loads(j.read())
   j.close()
   return words

# file with text -> file with json array
def bookToJSON(bookPath, wordsPath):
   words = openBook(bookPath)
   uwords = uniqueWords(words)
   jwords = json.dumps(uwords, indent=3) + "\n"
   out = codecs.open(wordsPath, "w", "utf-8")
   out.write(jwords)
   out.close()

# unique words
def uniqueWords(words):
   uniques = {}

   for w in words:
      if w in uniques:
         uniques[w] += 1
      else:
         uniques[w] = 1

   return uniques.keys()

# import the book
def openBook(path):
   src = codecs.open(path, "r", "utf-8")
   text = src.read()
   src.close()
   text_ = "".join(map(replacements, text))
   words = text_.split()
   return filter(notEmpty, filter(freqFilter, map(adjustCase, words)))

def replacements(ch):
   # I don't think this is unicode safe yet...
   if ch in string.punctuation:
      return " "
   elif not ch in string.printable:
      return " "
   else:
      return ch

def adjustCase(word):
   return word.lower()

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

   return not word in mostCommon


