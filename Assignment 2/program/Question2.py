#https://stackoverflow.com/questions/26570944/resource-utokenizers-punkt-english-pickle-not-found
import nltk as nl
import re as re
from collections import Counter
import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict 

# The setup for Question 2 i.e., part(a) starts here 
# the files are opened and concatenated into one string
    #https://stackoverflow.com/questions/12703842/how-to-tokenize-natural-english-text-in-an-input-file-in-python
    #https://www.nltk.org/book/ch03.html
    #https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character   
data=open("text_acad.txt",encoding="utf-8").read()
data = data + " " + open("text_blog.txt",encoding="utf-8").read()
data = data + " " +open("text_fic.txt",encoding="utf-8").read()
data = data + " " +open("text_mag.txt",encoding="utf-8").read()
data = data + " " +open("text_news.txt",encoding="utf-8").read()
data = data + " " +open("text_spok.txt",encoding="utf-8").read()
data = data + " " +open("text_tvm.txt",encoding="utf-8").read()
data = data + " " +open("text_web.txt",encoding="utf-8").read()

# the signs <p>, </p> and @ are removed from the string.
    #https://stackoverflow.com/questions/6167366/python-correct-way-to-strip-p-and-p-from-string
data = data.replace('<p>', ' ').replace('</p>', ' ')
data = data.replace('@', ' ')
# \n is removed here 
    #https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
data = data.strip()
# the string is lowercased
    #https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
data = data.lower()

#tokens are created based on whitespaces (lower cases again ) in the string 
token = re.split(r'\s+' , data)
token = [w.lower() for w in token]

#if there are any tokens that are just whitespaces, they are removed
while '' in token:
    token.pop(token.index(''))


#two gram tokens are created here
twoGram = []
for x in range(0,len(token)-1):
    twoGram.append(token[x]+" "+token[x+1])

#three gram tokens are created here,
threeGram = []
for x in range(0,len(token)-2):
    threeGram.append(token[x]+" "+token[x+1]+" "+token[x+2])



# part(b) starts here 
#the function below handles everything for part(b)
def partB(name):
    #input string is split into parts i.e., it is tokenised based whitespaces 
    test1 = re.split(r'\s+' , name)

    # 2 gram is created from the input string, last 2gram is removed as it does not have value, as nothing comes after the last 2 tokens
    twoTest=[]
    for x in range(0,len(test1)-1):
        twoTest.append(test1[x]+" "+test1[x+1])
    twoTest.pop(len(twoTest)-1)

    # 3 gram is created from the input string
    threeTest = []
    for x in range(0,len(test1)-2):
        threeTest.append(test1[x]+" "+test1[x+1]+" "+test1[x+2])

    #loop is run and inside the loop for each iteration 
    #instances of 3gram from input string is counted in 3gram of the data, this is then divided by instances of 2gram from input string is counted in 2gram of the data
    #the above gives the value of p when p1*p2*p3*p4
    p=1
    w = 0
    q = 0
    r = 0
    for x in range(len(twoTest)):
        p = p * ( (threeGram.count(threeTest[x])) / (twoGram.count(twoTest[x])) )
        w = w + math.log10( (threeGram.count(threeTest[x])) / (twoGram.count(twoTest[x])) )
        q = q + math.log1p( (threeGram.count(threeTest[x])) / (twoGram.count(twoTest[x])) )
        r = r + math.log2( (threeGram.count(threeTest[x])) / (twoGram.count(twoTest[x])) )
    w = math.exp(w)
    q = math.exp(q)
    r = math.exp(r)
    print("normal: P("+name+"): ",p)
    print("exp log10: P("+name+"): ",w)
    print("exp log1p: P("+name+"): ",q)
    print("exp log2: P("+name+"): ",r)
    print("\n")

#testcases for part(b) are given to the function here
partB("he is from the east .")
partB("she is from the east .")
partB("he is from the west .")
partB("she is from the west .")



# part(c) starts here 
#the function below handles everything for part(c)
def partC(name):
    #empty list is created along with an emplty string and a string with input string 
    damn =[]
    str = name
    chk = ""
    #loop is run till we encounter a '.'
    while(chk != "."):
        #input string is split based on whitespaces and while loop run for 3gram tokens 
            #https://www.geeksforgeeks.org/python-extract-words-from-given-string/
        lol = str.split()
        for x in threeGram:
            #3gram tokens are searched for the last 2 words in the string, 
            # and anything that follows those 2 words will also be accepted (apart from whitespaces) (i.e., \S+)
                #https://docs.python.org/3/library/re.html
                #https://stackoverflow.com/questions/44150709/how-to-input-a-string-in-regex-python
            test = re.search(r'(?<='+lol[len(lol)-2] +' '+lol[len(lol)-1]+' )\S+', x)
            #only and only if such a trigram is found it is added to the a list (test can oly store one value)
                #https://stackoverflow.com/questions/23086383/how-to-test-nonetype-in-python
            if test is not None:
                damn.append(test[0])
        #once all trigrams have been iterated over, list is sorted from most to least recurrring
        damn = [item for items, c in Counter(damn).most_common() for item in [items] * c] 
        #the steps below till the else statement are not nessesary for given testcase in part(c)
        #duplicates from the list are removed 
        damn = list(dict.fromkeys(damn))
        #it is checked if the last word from string + the most likely word already exists in the string 
            #if it does not exist, the most likely word is added 
            #if it does exist, the second most likely word is added
        chk = lol[len(lol)-1] + " " + damn[0]
            #https://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
        if chk not in str: 
            chk = damn[0]
        else:
            chk = damn[1]
        #the above helps in keeping the system from falling into a loop of repeating the same phrase 
        #the selected word is added to the string, the list is cleared so that it can be started from fresh
        str = str + " " + chk
        damn.clear()
    #once, '.' has been found and added to the string, the loop is exited from 
    #the finalised string is printed 
    print(str)

#testcases for part(c) are given to the function here
partC("a student is")
partC("the adventure of")
