from ListReader import *
import hashlib

print("yippy " + '\n')

HashedPasswordList = []

#hashes a word/password
def HashAlgorithm(password):
    h = hashlib.new('sha1')
    h.update(password.encode('utf-8'))
    return h.hexdigest()

#run a dictionary/rainbow list against the word that is hashed above
#-take the "rockyou.txt" list and hash every password
#-check those hashed passwords from rockyou.txt and compare it to the hashed password
#   in this file

def BruteForce(PasswordList):
    for password in PasswordList:
        hashedPassword = HashAlgorithm(password)
        HashedPasswordList.append(hashedPassword)



TxtReader()  #populates the list in ListReader

HashAlgorithm("\nbrazil\n")

BruteForce(PasswordList[:100])   #limits hashing to n

print("\nFirst 100 hashed passwords:\n")
for item in HashedPasswordList[:100]:
    print(item)


