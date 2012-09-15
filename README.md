This password generator uses scrypt's hash function to choose several words
using a given source of vocabulary, given only two keyphrases.  It is named
for its inspiration in an episode of Sherlock Holmes, where the fictional triads
used numerical codes to look up vocabulary from a common book.

In the special case where one of the characters of the second password
is a number, bytes of capitalized hex (e.g. 'C7') will be inserted
between words.

To install the Python version in Linux, and then start the demo
(with Darwin's Origin of Species for vocabulary):
```bash
cd py
sudo python setup.py install
cd ..
python
```

Then, in Python:
```python
from triad.demo import Generator

gg = Generator('books/pg2009.json')

gg.gen('lincoln', 'vampire-slayer')
# u'cows mounting molecules theoretically oftener'

gg.gen('lincoln', 'vampire-slayer', n=3)
# u'cows changes province'

gg.gen('lincoln', 'vampire-slayer', n=3, hexSep=True)
#u'cows 3F changes 9F province'
```

Key features to note:
* These passwords tend to be easier to memorize, and longer.
* They're not really random, so you can recreate them.
* They're not stored anywhere.
* Because scrypt is being used (with the two keyphrases),
  if a generated password is compromised your other passwords are
  still relatively safe.

That is, even if they can guess one of the keyphrases,
it will still be moderately expensive to brute force and
find the generated password.

Say, for example, you used the following to generate a LinkedIn password.
```python
gen('cows mounting molecules theoretically oftener', 'linkedin')
# u'coat solicit provisions orchidaceous asiatic'
```

Then somebody may discover that password,
"coat solicit provisions orchidaceous asiatic", and maybe even
can guess that you used "linkedin".  Therefore they might try to
use this algorithm to brute force your first keyphrase, or directly
try to guess your Twitter password using the second keyphrase "twitter".

If a hash designed for speed like SHA or MD5 was used, this wouldn't be
very hard.  But because we're using *scrypt*, the following may get
expensive.
```python
def guessFirstKey(table):
   for x in table:
      if gen(x, 'linkedin') == u'coat solicit provisions orchidaceous asiatic':
         return x

key0 = guessFirstKey(...)
gen(key0, 'twitter')
```

Alternatively, they might know which vocabulary you used (e.g., Darwin's
book from this demo), and guess the words in it (assuming the same number
as were in the discovered password).
With the vocabulary list I've included from Darwin's Origin of Species,
the following will require somebody to test over 9000^5 passwords.
```python
for a in vocab:
   for b in vocab:
      for c in vocab:
         for d in vocab:
            for e in vocab:
               " ".join([a,b,c,d,e])
```

Using five words provides more than 2^65 choices, seven more than 2^91, ten more than 2^131, and twenty more than 2^256...

I welcome criticism, though: email me!

-- Kevin Cantu <me@kevincantu.org>

