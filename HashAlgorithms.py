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


wordToBreak = HashAlgorithm("iloveyou")
print('\n' + "Password trying to break  -- iloveyou:" + '\n' + wordToBreak)

BruteForce(PasswordList[:10])   #limits hashing to n
                                 # NumberOfPassWords should print the whole 14m list

print("\nFirst 10 hashed passwords:\n")
for item in HashedPasswordList[:10]:
    print(item)
    if item == wordToBreak:
        print("GOT IT!!! --> " + item)
        break


#search the first 10 passwords of the list for what your looking for

