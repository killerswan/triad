'''
Kevin Cantu
June 2012
'''

import json
import codecs

def loadWords(path):
   '''
   Read a JSON file of words.
   '''

   j = codecs.open(path, "r", "utf-8")
   words = json.loads(j.read())
   j.close()
   return words

