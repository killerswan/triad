import unittest
from triad.demo import Generator

class TestDemo(unittest.TestCase):

   def setUp(self):
      self.gg = Generator('../books/pg2009.json')

   def test_fivewords(self):
      'Demo with five words'

      actual = self.gg.gen('lincoln', 'vampire-slayer')
      expected = u'cows mounting molecules theoretically oftener'
      self.assertEqual(expected, actual)

   def test_threewords(self):
      'Demo with three words'

      actual = self.gg.gen('lincoln', 'vampire-slayer', n=3)
      expected = u'cows changes province'
      self.assertEqual(expected, actual)

   def test_threewords_hex(self):
      'Demo with three words, plus hex bytes'

      actual = self.gg.gen('lincoln', 'vampire-slayer', n=3, hexSep=True)
      expected = u'cows 3F changes 9F province'
      self.assertEqual(expected, actual)

if __name__ == '__main__':
   unittest.main()

