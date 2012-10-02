'''
Kevin Cantu
June 2012
'''

import json
import codecs

def saveWords(path, words):
   'Write a JSON file of words.'

   jwords = json.dumps(words, indent=3) + "\n"
   out = codecs.open(path, "w", "utf-8")
   out.write(jwords)
   out.close()

def loadWords(path):
   'Read a JSON file of words.'

   j = codecs.open(path, "r", "utf-8")
   words = json.loads(j.read())
   j.close()
   return words

