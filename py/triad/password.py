'''
Kevin Cantu
June 2012
'''

import string
import binascii
import scrypt

def generate(vocab, key0, key1, n=5, hexSep=False):
   '''
   Use scrypt's hash function on our password/salt to generate 64 bytes
   of so-called entropy.  Then use this to choose several (default: 4)
   of the vocabulary words.

   When desired, bytes of capitalized hex (e.g. 'C7') can be inserted
   between words.

   Note: asking for more words doesn't does not change the hash function call,
   just the word selection, so an exception will be thrown if you ask
   for too many words.

   Vocabulary can be supplied from any source you desire.  The results aren't
   as secure as random passwords, but seem better than what most people use.
   '''
   nn = n

   vocabSize = len(vocab)
   words = []

   entropy = kindaRandomOracle(key0, key1)

   if hexSep:
      # leave room for hex octets between the words
      bytesPerWord = (len(entropy) - (nn-1)) / nn
      mm = nn * 2 - 1
   else:
      bytesPerWord =  len(entropy) / nn
      mm = nn

   wordSize = 2 ** (bytesPerWord * 8)

   # if we would lose too much entropy
   # i.e., 21 words or less with octets between, or 32 words or less without
   if wordSize < vocabSize:
      raise Exception('Too many words requested...')

   start = 0
   end = 0

   for ii in range(mm):
      # hex octet separators
      if hexSep and ii % 2 == 1:
         start = end
         end   = end + 1
         byte = binascii.hexlify(entropy[int(start)])
         words.append(byte.upper())

      # words
      else:
         start = end
         end   = end + bytesPerWord

         # we lose entropy here be dropping words off the end
         key = entropy[start:end] 
         # we lose more entropy here by cramming a number into this smaller range
         # less significant digits end up getting dropped
         scaledKey = str2int(key) * vocabSize / wordSize

         # c'est la vie
         words.append(vocab[scaledKey])


   return ' '.join(words)
   
def kindaRandomOracle(key0, key1):
   '''
   Use scrypt to generate a hash based on
   the two passwords or password/salt you specify.

   This is intentionally NOT random.  Calling it entropy is weird, too.
   But it is scrypt.
   '''

   val = scrypt.hash(key0.encode('utf8'), key1.encode('utf8'))
   return val

def str2int(ss):
   '''
   Take a string of bytes as hexadecimal and
   return the integer value.
   '''

   val = int(binascii.hexlify(ss), 16)
   return val

