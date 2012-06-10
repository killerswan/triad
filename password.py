'''
Kevin Cantu
June 2012
'''

import binascii
import scrypt

def generate(vocab, pass0, pass1, nn=5, sep=False):
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

   if sep:
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
      if sep and ii % 2 == 1:
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

