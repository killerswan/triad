# Kevin Cantu
# May 2012

import binascii
import scrypt

def generate(vocab, pass0, pass1, nn=4):
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
      scaledKey = str2int(key) * vocabSize / wordSize

      # c'est la vie
      words.append(vocab[scaledKey])

   return ' '.join(words)
   
def kindaRandomOracle(pw0, pw1):
   val = scrypt.hash(pw0, pw1)
   return val

def str2int(ss):
   val = int(binascii.hexlify(ss), 16)
   return val

