'''
Kevin Cantu
June 2012
'''

import triad.words_en
import triad.words
import triad.password

def makeGenerator(book):
   '''
   generate and save the list of words from an English book,
   then load the words and return a password generator
   '''

   triad.words_en.bookToWords(book, 'demo.json')
   words = triad.words.loadWords('demo.json')

   def gen(pw1, pw2, n=5):
      return triad.password.generate(words, pw1, pw2, n)

   return gen
