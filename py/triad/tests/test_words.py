import unittest
import json
import codecs
import os
import tempfile
from triad.words import saveWords, loadWords

class TestWords(unittest.TestCase):

   sample = ['these', 'are', 'sample', 'words']

   def setUp(self):
      mode, self.file = tempfile.mkstemp()
      
   def test_loaded_equals_saved(self):
      'Test that words loaded from a file match those saved'

      saveWords(self.file, self.sample)

      self.assertEqual(self.sample, loadWords(self.file))
      os.remove(self.file)

if __name__ == '__main__':
   unittest.main()

