print("hellow" + '\n')


#word.replace('\n','') for word in f
with open('testList.txt', 'r') as f:
    count = 0
    for word in f:
        processed_word = word.rstrip('\n')
        count = count + 1
        print(processed_word)
    print('\n' + "number of words:")
    print(count)    



def makingWords():
    print('\n' + "what am I doing?")

makingWords()






