'''
Kevin Cantu
June 2012
'''

from triad.words_en import bookToWords
from triad.words    import loadWords
from triad.password import generate

#def makeGenerator(book):
class Generator(object):
   '''
   generate and save the list of words from an English book,
   then load the words and return a password generator
   '''
   def __init__(self, vocabList):
      self.words = loadWords(vocabList)

   def gen(self, key0, key1, n=5, hexSep=False):
      return generate(self.words, key0, key1, n, hexSep)

