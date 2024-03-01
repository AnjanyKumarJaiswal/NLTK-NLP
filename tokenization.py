# tokenization with simple sentence 

import string

customtext = "Hello! this is my first NLP code, In this example of code we would be doing Tokenizations!!!"

def mypunctuation(text):
    punc = string.punctuation
    
    opt_text = "".join(char for char in text if char not in punc)
    
    return opt_text

custompunc = mypunctuation(customtext)


def mylower(case):
    return case.lower()

caselower = mylower(custompunc)

def mytoken(tk):
    words = []
    i = 0
    word = ""
    while(i<len(tk)):
        if(tk[i]!=" "):
            word = word+tk[i]
        else:
            words.append(word)
        
        i =i +1
        words.append(word)
    
    return words

tokenization = mytoken(caselower)

print(tokenization)