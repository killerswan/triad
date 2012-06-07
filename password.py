# Kevin Cantu
# May 2012

import scrypt

def generate(wordList, pass0, pass1, nn=4):
   entropy = kindaRandomOracle(pass0, pass1)
   wordCount = len(wordList)
   words = []

   bytesPerWord = len(entropy) / nn

   print "bytes/word: " + str(bytesPerWord)

   wordRange = 2 ** (bytesPerWord * 8)

   if wordRange < wordCount:
      raise Exception('Too many words requested...')

   for ii in range(nn):
      key = entropy[ bytesPerWord * (ii) : bytesPerWord * (ii + 1) ]
      scaledKey = str2int(key) * wordCount / wordRange
      words.append(wordList[scaledKey])

      print "range is from " + str(bytesPerWord * ii) + " to " + str(bytesPerWord * (ii + 1))
      print scaledKey

   return ' '.join(words)
   
def kindaRandomOracle(pw0, pw1):
   val = scrypt.hash(pw0, pw1)
   return val

def str2int(s):
   '''
   Note that the way this works is kinda weird...
      >>> hex(int('1234'.encode('hex'), 16))
      '0x31323334'
      >>> hex(int('12345678'.encode('hex'), 16))
      '0x3132333435363738'

   Use encode to turn each character into a string showing the hex value,
   then convert each hex string into an integer.
   '''

   val = int(s.encode('hex'), 16)
   print hex(val)
   return val

