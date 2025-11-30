
print("hellow" + '\n')

PasswordList = []
PasswordLengthList = []

def TxtReader():
    with open("rockyou.txt", "r", encoding="utf-8", errors="ignore") as f:
        count = 0
        for word in f:
            processed_word = word.rstrip('\n')
            count += 1
            #print(processed_word)
            PasswordList.append(processed_word)
        print('\n' + "number of words:")
        #print(count)
        #print(PasswordList)



    #gets the length of every password in the .txt list
def WordLength(Password_List, PasswordLengthList):
    for word in Password_List:
        PasswordLengthList.append(len(word) - 1)
    print("longest password length:")
    return PasswordLengthList



    # For somet reason this is the varaible that the visualization class uses
    # in the graphs
#
# WordLength(PasswordList, PasswordLengthList)    #gets the character count for each password and makes a list of of them 
#print(PasswordLengthList)
print("-----------------")
TxtReader()
NumberOfPasswords = PasswordList.__len__()
print(NumberOfPasswords)
print("-----------------")
WordLength(PasswordList, PasswordLengthList)
MaxPasswordLength = max(PasswordLengthList)     #finds the max lenght password in the .txt file
print(MaxPasswordLength)

print("   index/location of password:")
IndexOfMaxPasswordLength = PasswordLengthList.index(MaxPasswordLength)
print(IndexOfMaxPasswordLength)
print("   longest password:")
print(PasswordList[IndexOfMaxPasswordLength])





