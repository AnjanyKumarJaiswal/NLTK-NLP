def mysentence(inputtext):
    sentence = []
    start = 0
    for i in range(len(inputtext)):
        if inputtext[i] == '.' or inputtext[i] == '!' or inputtext[i]=='?' :
            sentence.append(inputtext[start:i+1].strip())
        
    return sentence

print("Enter your user input text for sentence segementation:")
inputtext = str(input())

print(mysentence(inputtext))