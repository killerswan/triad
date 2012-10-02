# coding: utf-8

import unittest
from triad.password import str2int, kindaRandomOracle, generate

class TestPassword(unittest.TestCase):

   def test_utf8_oracle(self):
      'Test support for UTF-8 strings'

      expected_hex = '1d8306508ce47b8d8ddef958d2b31fa6641b265f7f9a4d5298d158a99f6f7c5c48e58afa7443db55eadefdba7bb3e7e5a3c9a9e0b44998d1eafc0e43c915e10f'
      actual = kindaRandomOracle(u'卢浦大桥', u'马岭河大桥')
      self.assertEqual(64, len(actual))
      self.assertEqual(expected_hex.decode('hex'), actual)

   def test_hexlify_endianness(self):
      'Test string2int conversion (may be arch specific)'

      self.assertEqual(108170603228769,           str2int('banana'))
      self.assertEqual(563759332872332832960366L, str2int('watermelon'))

   def test_too_many_words_requested(self):
      '''
      Test for problems with too little "entropy"

      Words are chosen with a fraction of the bytes from scrypt.
      The more words requested, the smaller the number of bytes each.
      If too small, only a portion of the vocabulary could be reached,
      and that would be uncool.
      '''

      vocabulary = map(str, range(2**16))

      # OK: each word is chosen with >=2 bytes - OK for 2**16
      generate(vocabulary, 'one', 'two', n=32)

      # BAD: each word is chosen with <=1 byte - BAD for 2**16
      self.assertRaises(Exception, generate, vocabulary, 'one', 'two', n=33)

if __name__ == '__main__':
   unittest.main()

