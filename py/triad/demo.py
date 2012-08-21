'''
Kevin Cantu
June 2012
'''

from triad.words_en import bookToWords
from triad.words    import loadWords
from triad.password import generate

#def makeGenerator(book):
def makeGenerator(vocabList):
   '''
   generate and save the list of words from an English book,
   then load the words and return a password generator
   '''

   #bookToWords(book, 'demo.json')
   #words = loadWords('demo.json')
   words = loadWords(vocabList)

   def gen(key0, key1, n=5, hexSep=False):
      return generate(words, key0, key1, n, hexSep)

   return gen
