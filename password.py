# Kevin Cantu
# May 2012

import scrypt

def generate(wordList, pass0, pass1, nn=4):
   entropy = kindaRandomOracle(pass0, pass1)
   wordCount = len(wordList)
   words = []

   bytesPerWord = len(entropy) / nn

   if 2 ** (bytesPerWord * 8) < wordCount:
      raise Exception('Too many words requested...')

   for ii in range(nn):
      key = entropy[ bytesPerWord * (ii) : bytesPerWord * (ii + 1) ]
      scaledKey = str2int(key) % wordCount
      words.append(wordList[scaledKey])

   return ' '.join(words)
   
def kindaRandomOracle(pw0, pw1):
   return scrypt.hash(pw0, pw1)

def str2int(s):
   return int(s.encode('hex'), 16)

