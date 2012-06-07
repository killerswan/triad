Kevin Cantu, June 2012

Example usage, in Python:

```python
import book
import password

book.bookToJSON('pg2009.txt', 'demo.json')
words = book.loadWordsJSON('demo.json')
password.generate(words, 'otter', 'pop')     # u'summon feet leafstalks tested'
```

