Kevin Cantu, June 2012

This password generator uses scrypt's hash function to choose several
words from a given source of vocabulary.

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
import triad.demo as demo

gen = demo.makeGenerator('books/pg2009.txt')

gen('lincoln', 'vampire-slayer')
# u'cows mounting molecules theoretically oftener'

gen('lincoln', 'vampire-slayer', n=3)
# u'cows changes province'

gen('lincoln', 'vampire-slayer0', n=3)
#u'tried 96 stationary 0E stump'
```

TODO: an Android app...

