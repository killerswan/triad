# Kevin Cantu
# May 2012

import book
import random
import scrypt

def kindaRandomOracle(pw0, pw1):
   return scrypt.hash(pw0, pw1)

def generate(wordList, pw0, pw1, nn=4):
   avail = len(wordList)
   entropy = kindaRandomOracle(pw0, pw1)
   words = []

   bytesPerWord = len(entropy) / nn

#   if bytesPerWord * 8 < avail:
#      raise Exception('Sorry, running out of bytes to use...')

   for ii in range(nn):
      key = entropy[ bytesPerWord * (ii) : bytesPerWord * (ii + 1) ]
      scaledKey = str2int(key) % avail
      words.append(wordList[scaledKey])

   return ' '.join(words)
   
def str2int(s):
   return int(s.encode('hex'), 16)

# grab some words
def randomWords(book, nn):
   blen = len(book)
   words = []

   for ii in range(nn):
      rnd = random.randrange(0, blen)
      words.append(book[rnd])

   return words


