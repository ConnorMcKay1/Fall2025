import hashlib

print("yippy " + '\n')


#hashes a word/password
h = hashlib.new('sha1')
h.update(b"Nobody")
print(h.hexdigest())


#run a dictionary/rainbow list against the word that is hashed above
#-take the "rockyou.txt" list and hash every password
#-check those hashed passwords from rockyou.txt and compare it to the hashed password
#   in this file
