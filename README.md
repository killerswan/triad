Kevin Cantu, June 2012

Example Python usage, with Darwin's Origin of Species for vocabulary:

```python
import book
import password

book.bookToJSON('pg2009.txt', 'demo.json')
words = book.loadWordsJSON('demo.json')

password.generate(words, 'lincoln', 'vampire-slayer')
# u'cows mounting molecules theoretically oftener'

password.generate(words, 'lincoln', 'vampire-slayer', nn=3, sep=True)
# u'cows 3F changes 9F province'
```

Update: I think we can now easily satisfy Apple:
(1) have at least one letter,
(2) have at least one capital letter,
(3) have at least one number,
(4) not contain more than 3 consecutive identical characters,
(5) be at least 8 characters.

Also: an Android app...

