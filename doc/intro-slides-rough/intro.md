% "If we don't try, we will not know how our luck falls." [0]

# Triad: a password generator
* Prompt for two memorized keys.
* Generate an *scrypt* hash.
* Use the hash to choose vocabulary words from a book.

# Goals
Trust nobody.  Make a user-focused tool which makes it painless to avoid password re-use.

# Not goals
* Secure entire web-services.
* Replace passwords altogether.

# Not goals
"Children warned name of first pet should contain 8 characters and a digit" [1]


# Existing tools
* http://updates.oplop.mobi/
* https://www.pwdhash.com/
* http://supergenpass.com/
* http://ypassword.espozito.com/

#
How many people know your password?

How much do you trust them?


# 1. passwords are everywhere

Alternatives exist, but passwords remain:
* fingerprints, retina scans, DNA sequencing, other biometrics
* smart cards, public key crypto, etc.

All those are a lot more work.

# 2. passwords have weaknesses
a. people choose bad ones (more later)
b. there's a lot of trust invested in defining a password

# 3. Who do you trust?
Who has keys to your front door?  Your garage?  Your car?  Are those keys the same?

# 4. How many people have you given passwords to?
How many companies?  How many _people_?

# 5. Are those passwords the same?

# 6. How are they protected?

HTTPS

SRP

HMAC

PBKDF2

bcrypt

scrypt

# 6b. How are they protected?

[Salted] SHA1

[Salted] MD5

Plaintext

Unencrypted HTTP

# 7. Are those passwords the same?

# 8. Attacks
a. brute force guessing
b. dictionary guessing / rainbow tables
c. knowing the password already from another location  <-- mortal combat: finish him!

# 9. What makes a good password (redux)?
a. large
b. genuinely random
c. unique

# 10. Proposal: Use a random number generator, per password?

one-at-a-time
   random number -> pwd

lifehacker piece of paper thingy keyed on site id
   random number + servicename -> pwd

# 11. What if I forget?

# 12. Proposal: let a computer remember?
disk failure?

# 13. Proposal: let a distributed corporate software remember?
You trust them?  You give a copy of all your keys to one person?

# 14. Other proposals:
* legal escrow
* bank safe deposit box
* US Marine Corp. defended physical building



# 15. Proposal: Use a pseudo random password generator
seed -> !random number -> pwd



# 16. XKCD:
a. it is OK if they're not just unintelligible garbage
http://xkcd.com/936/



# 17. REDUX:
d. easy to remember
e. easy to type fast


# 18. TODO

Make a GUI app.



# Some outstanding questions

Before I carve version 1.0 in stone (or, rather, Java), I want to get some feedback about how this can or should work in languages like Mandarin which are less likely to use word separators.  Will Mandarin, for example, break gracefully on each glyph?  Would speakers benefit from larger numbers of generated words (e.g., n=14 instead of n=6)?  How are numbers typically written?  Will the optional hex bytes work and be easy enough to write and memorize?  Will super-common characters and punctuation be easy to filter from the word lists?


# Biggest flaw?

People don't like to type on phones.  (Srsly.)



# References

[0] Saga of King Hrolf Kraki / Byock / random message board

[1] http://newsbiscuit.com/2012/06/08/chi

