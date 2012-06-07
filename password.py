'''
Kevin Cantu
June 2012
'''

import binascii
import scrypt

def generate(vocab, pass0, pass1, nn=4):
   '''
   Use scrypt's hash function on our password/salt
   to generate 64 bytes of so-called entropy.
   (Strictly speaking, we can only work with whatever entropy
   is in the passwords you specify, so make them wordy.)
   
   Then use these to choose N (default: 4) of the vocabulary words.

   Note: asking for more words doesn't does not change the hash function call,
   just the word selection, so an exception will be thrown if you ask
   for too many words.
   '''

   vocabSize = len(vocab)
   words = []

   entropy = kindaRandomOracle(pass0, pass1)
   bytesPerWord = len(entropy) / nn
   wordSize = 2 ** (bytesPerWord * 8)

   # if we would lose too much entropy
   if wordSize < vocabSize:
      raise Exception('Too many words requested...')

   for ii in range(nn):
      # we lose entropy here be dropping words off the end
      key = entropy[ bytesPerWord * (ii) : bytesPerWord * (ii + 1) ]

      # we lose more entropy here by cramming a number into this smaller range
      # less significant digits end up getting dropped
      scaledKey = str2int(key) * vocabSize / wordSize

      # c'est la vie
      words.append(vocab[scaledKey])

   return ' '.join(words)
   
def kindaRandomOracle(pw0, pw1):
   '''
   Use scrypt to generate a hash based on
   the two passwords or password/salt you specify.

   This is intentionally NOT random.  Calling it entropy is weird, too.
   But it is scrypt.
   '''

   val = scrypt.hash(pw0, pw1)
   return val

def str2int(ss):
   '''
   Take a string of bytes as hexadecimal and
   return the integer value.
   '''

   val = int(binascii.hexlify(ss), 16)
   return val

