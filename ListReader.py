print("hellow" + '\n')

PasswordList = []
PasswordLengthList = []

#word.replace('\n','') for word in f
with open('testList.txt', 'r') as f:
    count = 0
    for word in f:
        processed_word = word.rstrip('\n')
        count = count + 1
        #print(processed_word)
        PasswordList.append(processed_word)
    print('\n' + "number of words:")
    print(count)
    #print(PasswordList)


def WordLength(Password_List, PasswordLengthList):
    for word in Password_List:
        PasswordLengthList.append(len(word) - 1)
    return PasswordLengthList


WordLength(PasswordList, PasswordLengthList)
#print(PasswordLengthList)
NumberOfPasswords = PasswordList.__len__()
print("-----------------")
print(NumberOfPasswords)




