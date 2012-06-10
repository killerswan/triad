Kevin Cantu, June 2012

This password generator uses scrypt's hash function to choose several
words from a given source of vocabulary.

In the special case where one of the characters of the second password
is a number, bytes of capitalized hex (e.g. 'C7') will be inserted
between words.

Example Python usage, with Darwin's Origin of Species for vocabulary:

```python
import book
import password

book.bookToJSON('pg2009.txt', 'demo.json')
words = book.loadWordsJSON('demo.json')

password.generate(words, 'lincoln', 'vampire-slayer')
# u'cows mounting molecules theoretically oftener'

password.generate(words, 'lincoln', 'vampire-slayer', nn=3)
# u'cows changes province'

password.generate(words, 'lincoln', 'vampire-slayer7', nn=3)
# u'destroy 48 rubs 36 prepotency'
```

TODO: an Android app...

