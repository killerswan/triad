import unittest
import os
import tempfile
from triad.words    import saveWords, loadWords
from triad.words_en import bookToWords

class TestWordsEn(unittest.TestCase):

   original      = '../books/pg2009.txt'
   originalWords = '../books/pg2009.json'

   def setUp(self):
      mode, self.tempWords = tempfile.mkstemp()

   def high_level_test_OriginOfSpecies(self):
      'Test that we derive the same set of words from Darwin as before'
      bookToWords(self.original, self.tempWords)
      self.assertEqual(loadWords(self.originalWords),
                       loadWords(self.tempWords))
      
if __name__ == '__main__':
   unittest.main()

