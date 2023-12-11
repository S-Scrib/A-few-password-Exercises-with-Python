# Ok, Lets do some password hashing!Going to start with a hash algorithm. I am going to use SHA-256.
# First, import the needed data.

import hashlib
import os

# Let's start with a salt
password = '12345!'
salt = os.urandom(32)
# And a little hash to go with it!
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

