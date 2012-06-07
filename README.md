Kevin Cantu, June 2012

Example Python usage, with Darwin's Origin of Species for vocabulary:

```python
import book
import password

book.bookToJSON('pg2009.txt', 'demo.json')
words = book.loadWordsJSON('demo.json')

password.generate(words, 'otter', 'pop')
# u'summon feet leafstalks tested'
```

Now I need to implement a mechanism to optionally
generate passwords like those required for AppleIDs:
(1) have at least one letter,
(2) have at least one capital letter,
(3) have at least one number,
(4) not contain more than 3 consecutive identical characters,
(5) be at least 8 characters.

Also: an Android app...

