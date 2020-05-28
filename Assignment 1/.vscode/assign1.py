#https://stackoverflow.com/questions/26570944/resource-utokenizers-punkt-english-pickle-not-found
import nltk as nl
import re
from collections import Counter
import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict 

#class used for Question 2 and 3 primarily and supplements Question 4
#a class is created consisting of all required meathods 
#each object will represent a txt file from the assignment
class tokenizor():
    #the file is tokenized based on empty space. Punctuation is then removed from the tokens later. 
    #in effect: 'i'm' stays one token and is converted to 'im'
    token = list
    vocabulary = list
    def __init__(self,name):
        super().__init__()
        #open file
            #https://stackoverflow.com/questions/12703842/how-to-tokenize-natural-english-text-in-an-input-file-in-python
            #https://www.nltk.org/book/ch03.html
            #https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character   
        data=open(name,encoding="utf-8").read()
        #tokenize and lowercase using re
        token=re.split(r'\s+' , data)
        self.token = [w.lower() for w in token]
        #remove punctuation
            #https://docs.python.org/3.4/library/re.html
        self.token = [re.sub(r'\W+', r'',w) for w in self.token]
        #remove blank space tokens 
        while '' in self.token:
            self.token.pop(self.token.index(''))
        self.vocabulary = sorted(set(self.token))

    #one gram tokens are created here,
    #counted and printed based on which gram was used most to least 
        ##https://stackoverflow.com/questions/48342492/python-maximum-number-of-times-element-appear-in-list
    def ONEgram(self,x):
        g = self.token
        ct = Counter(g)
        print(ct.most_common(x))

    #two gram tokens are created here,
    #counted and printed based on which gram was used most to least 
    def TWOgram(self,y):
        g=[]
        for x in range(0,len(self.token)-1):
            g.append(self.token[x]+" "+self.token[x+1])
        ct = Counter(g)
        print (ct.most_common(y))

    #three gram tokens are created here,
    #counted and printed based on which gram was used most to least 
    def THREEgram(self,z):
        g=[]
        for x in range(0,len(self.token)-2):
            g.append(self.token[x]+" "+self.token[x+1]+" "+self.token[x+2])
        ct = Counter(g)
        print (ct.most_common(z))

    #number of total tokens are calculated here
    def tLength(self):
        return len(self.token)

    #set token list for vocabulary list and calculate number of vocabulary used 
    def vocab(self):
        return len(self.vocabulary)

    #calculate TTR(type token ratio)
    #ratio of range of vocabulary vs number of words used
        ##https://carla.umn.edu/learnerlanguage/spn/comp/activity4.html
    def TTR(self):
        return (len(sorted(set(self.token))))/(len(self.token))
    
    #calculate mean token length
    #average length of tokens 
    def meanLen(self):
        mlen_raven = 0
        for x in self.token:
            mlen_raven = mlen_raven + len(x)
        return mlen_raven/len(self.token)

    #calulate entropy 
        #https://www.geeksforgeeks.org/log-functions-python/
    def entropy(self):
        e=0
        for x in sorted(set(self.token)):
            e = e + ( ( self.token.count(x) / len(self.token) ) *  math.log2( self.token.count(x) / len(self.token) ) )
        return (-1*e)

    #Question 2
    #find average c in zipf
        #https://www.w3schools.com/python/python_howto_remove_duplicates.asp
        #https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/
    def zipfEstimateC(self):
        z=0
        #arranges tokens by most to least occurancs rank
        r = [item for items, c in Counter(self.token).most_common() for item in [items] * c] 
        #duplicates are removed from tokens as we do not need them as rank sequence has already been determined
        r= list(dict.fromkeys(r))
        #represents the range/number of vocaubulary used 
        rt = sorted(set(self.token))
        for x in rt:
            #z = z + (how many times word(x) was in tokens)/(total number of tokens) * (rank (by most to least occurances) +1(as 0 is not a rank))
            z = z + ( ( (self.token.count(x)) / (len(self.token)) ) * ( (r.index(x)) +1) )
        #average c
        c = z/len(sorted(set(self.token)))
        return c 


#Question 2 and 3
#calls required methods for raven.txt
def allABTraven(x):
    print("RAVEN")
    raven = tokenizor("raven.txt");
    raven.ONEgram(x)
    raven.TWOgram(x)
    raven.THREEgram(x)
    print("Tokens: ",raven.tLength())
    print("Vocabulary: ",raven.vocab())
    print("TTR: ",raven.TTR())
    print("Mean length: ",raven.meanLen())
    print("Entropy: ",raven.entropy())
    #Question 2
    print("zipf's C:",raven.zipfEstimateC(),"\n")

#Question 2 and 3
#calls required methods for gullivers-travels.txt
def allABTgullivers(x):
    print("GULLIVER'S")
    gulliversT = tokenizor("gullivers-travels.txt");
    gulliversT.ONEgram(x)
    gulliversT.TWOgram(x)
    gulliversT.THREEgram(x)
    print("Tokens: ",gulliversT.tLength())
    print("Vocabulary: ",gulliversT.vocab())
    print("TTR: ",gulliversT.TTR())
    print("Mean length: ",gulliversT.meanLen())
    print("Entropy: ",gulliversT.entropy())
    #Question 2
    print("zipf's C:",gulliversT.zipfEstimateC(),"\n")

#Question 4.a
#calls required methods for austen.txt
def allABTausten(x):
    print("AUSTEN")
    austen = tokenizor("austen.txt");
    austen.ONEgram(x)
    austen.TWOgram(x)
    austen.THREEgram(x)
    print("Tokens: ",austen.tLength())
    print("Vocabulary: ",austen.vocab())
    print("TTR: ",austen.TTR())
    print("Mean length: ",austen.meanLen())
    print("Entropy: ",austen.entropy(),"\n")
    #austen.zipfEstimateC()

#Question 4.a
#calls required methods for bronte.txt
def allABTbronte(x):
    print("BRONTE")
    bronte = tokenizor("bronte.txt");
    bronte.ONEgram(x)
    bronte.TWOgram(x)
    bronte.THREEgram(x)
    print("Tokens: ",bronte.tLength())
    print("Vocabulary: ",bronte.vocab())
    print("TTR: ",bronte.TTR())
    print("Mean length: ",bronte.meanLen())
    print("Entropy: ",bronte.entropy(),"\n")
    #bronte.zipfEstimateC()

#Question 4.a
#calls required methods for disputed.txt
def allABTdisputed(x):
    print("DISPUTED")
    disputed = tokenizor("disputed.txt");
    disputed.ONEgram(x)
    disputed.TWOgram(x)
    disputed.THREEgram(x)
    print("Tokens: ",disputed.tLength())
    print("Vocabulary: ",disputed.vocab())
    print("TTR: ",disputed.TTR())
    print("Mean length: ",disputed.meanLen())
    print("Entropy: ",disputed.entropy(),"\n")
    #disputed.zipfEstimateC()


#Question 4.b1 and 4.b2
#find common vocab from 3 txt docs 
def whoWroteIT():
    #Question 4.b1
    #make new objects to have token list and vocab list auto generated 
    bronte = tokenizor("bronte.txt")
    disputed = tokenizor("disputed.txt")
    austen = tokenizor("austen.txt")
    #common tokens from the three files are put into an empty list
    common_tokens = []
    for x in bronte.vocabulary:
        if(x in austen.vocabulary):
            if(x in disputed.vocabulary):
                common_tokens.append(x)

    #duplictes are removed from the list if any are present
    common_tokens = list(dict.fromkeys(common_tokens))

    #new lists are created for the 3 files: sorted based on most to least number of occurances, (similar process to one used in Question 2)
    #duplicates  removed and list trimmed to length of 50
        #https://stackoverflow.com/questions/1534939/how-to-trim-a-list-in-python
        #https://www.w3schools.com/python/python_howto_remove_duplicates.asp
        #https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/
    bronte_frequent50 = [item for items, c in Counter(bronte.token).most_common() for item in [items] * c] 
    bronte_frequent50 = list(dict.fromkeys(bronte_frequent50))
    bronte_frequent50 = bronte_frequent50[:50]
    austen_frequent50 = [item for items, c in Counter(austen.token).most_common() for item in [items] * c] 
    austen_frequent50 = list(dict.fromkeys(austen_frequent50))
    austen_frequent50 = austen_frequent50[:50]
    disputed_frequent50 = [item for items, c in Counter(disputed.token).most_common() for item in [items] * c] 
    disputed_frequent50 = list(dict.fromkeys(disputed_frequent50))
    disputed_frequent50 = disputed_frequent50[:50]

    #2 empty lists initialised to keep the z scores 
    dump = []
    temp = []

    #for loop started for top 50 in austen.txt
        #https://www.geeksforgeeks.org/python-statistics-stdev/
        #https://stackoverflow.com/questions/8744113/python-list-by-value-not-by-reference
    for x in austen_frequent50:
        #we check if the word also exists in common tokens as this confirms that we will have a z score for all .txt files 
        if x in common_tokens:
            #temp list is cleared, this preps it for intake of fresh values 
            temp.clear()
            #below the z score for the given word is calculated in the same order every time so we can know which position refers to which .txt file 
            #the order is always: 1.austen, 2.bronte, 3.disputed 
            #after each calculation, the z score is appended to temp list
            z = 0
            z = ( ( austen.token.count(x) / len(austen.token) ) - ( ( ( austen.token.count(x) / len(austen.token) ) + ( bronte.token.count(x) / len(bronte.token) ) + ( disputed.token.count(x) / len(disputed.token) ) ) / 3) )
            z = z / ( statistics.stdev([( austen.token.count(x) / len(austen.token) ), ( bronte.token.count(x) / len(bronte.token) ), ( disputed.token.count(x) / len(disputed.token) )]) )
            temp.append(z)

            z = 0
            z = ( ( bronte.token.count(x) / len(bronte.token) ) - ( ( ( austen.token.count(x) / len(austen.token) ) + ( bronte.token.count(x) / len(bronte.token) ) + ( disputed.token.count(x) / len(disputed.token) ) ) / 3) )
            z = z / ( statistics.stdev([( austen.token.count(x) / len(austen.token) ), ( bronte.token.count(x) / len(bronte.token) ), ( disputed.token.count(x) / len(disputed.token) )]) )
            temp.append(z)

            z = 0
            z = ( ( disputed.token.count(x) / len(disputed.token) ) - ( ( ( austen.token.count(x) / len(austen.token) ) + ( bronte.token.count(x) / len(bronte.token) ) + ( disputed.token.count(x) / len(disputed.token) ) ) / 3) )
            z = z / ( statistics.stdev([( austen.token.count(x) / len(austen.token) ), ( bronte.token.count(x) / len(bronte.token) ), ( disputed.token.count(x) / len(disputed.token) )]) )
            temp.append(z)

            #the temp list now has 3 values, these are now appended to dump list
            #so dump list has lists of 3 values inside it
            dump.append(temp[:])
            #the word is then removed from common_tokens list
            #this is done so that in subsequent calculations for other .txt files, we dont calculate z scores for words that have already been calculated for (if statement in loop does this).
            #as austen, bronte, disputed can have the same word, but it only exists once in common_token list 
            common_tokens.pop(common_tokens.index(x))

    #for loop started for top 50 in bronte.txt
        #https://www.geeksforgeeks.org/python-statistics-stdev/
        #https://stackoverflow.com/questions/8744113/python-list-by-value-not-by-reference
    for x in bronte_frequent50:
        #we check if the word also exists in common tokens as this confirms that we will have a z score for all .txt files 
        if x in common_tokens:
            #temp list is cleared, this preps it for intake of fresh values 
            temp.clear()
            #below the z score for the given word is calculated in the same order every time so we can know which position refers to which .txt file 
            #the order is always: 1.austen, 2.bronte, 3.disputed 
            #after each calculation, the z score is appended to temp list
            z = 0
            z = ( ( austen.token.count(x) / len(austen.token) ) - ( ( ( austen.token.count(x) / len(austen.token) ) + ( bronte.token.count(x) / len(bronte.token) ) + ( disputed.token.count(x) / len(disputed.token) ) ) / 3) )
            z = z / ( statistics.stdev([( austen.token.count(x) / len(austen.token) ), ( bronte.token.count(x) / len(bronte.token) ), ( disputed.token.count(x) / len(disputed.token) )]) )
            temp.append(z)

            z = 0
            z = ( ( bronte.token.count(x) / len(bronte.token) ) - ( ( ( austen.token.count(x) / len(austen.token) ) + ( bronte.token.count(x) / len(bronte.token) ) + ( disputed.token.count(x) / len(disputed.token) ) ) / 3) )
            z = z / ( statistics.stdev([( austen.token.count(x) / len(austen.token) ), ( bronte.token.count(x) / len(bronte.token) ), ( disputed.token.count(x) / len(disputed.token) )]) )
            temp.append(z)

            z = 0
            z = ( ( disputed.token.count(x) / len(disputed.token) ) - ( ( ( austen.token.count(x) / len(austen.token) ) + ( bronte.token.count(x) / len(bronte.token) ) + ( disputed.token.count(x) / len(disputed.token) ) ) / 3) )
            z = z / ( statistics.stdev([( austen.token.count(x) / len(austen.token) ), ( bronte.token.count(x) / len(bronte.token) ), ( disputed.token.count(x) / len(disputed.token) )]) )
            temp.append(z)

            #the temp list now has 3 values, these are now appended to dump list
            #so dump list has lists of 3 values inside it
            dump.append(temp[:])
            #the word is then removed from common_tokens list
            #this is done so that in subsequent calculations for other .txt files, we dont calculate z scores for words that have already been calculated for (if statement in loop does this).
            #as austen, bronte, disputed can have the same word, but it only exists once in common_token list 
            common_tokens.pop(common_tokens.index(x))

    #for loop started for top 50 in disputed.txt
        #https://www.geeksforgeeks.org/python-statistics-stdev/
        #https://stackoverflow.com/questions/8744113/python-list-by-value-not-by-reference
    for x in disputed_frequent50:
        #we check if the word also exists in common tokens as this confirms that we will have a z score for all .txt files 
        if x in common_tokens:
            #temp list is cleared, this preps it for intake of fresh values 
            temp.clear()
            #below the z score for the given word is calculated in the same order every time so we can know which position refers to which .txt file 
            #the order is always: 1.austen, 2.bronte, 3.disputed 
            #after each calculation, the z score is appended to temp list
            z = 0
            z = ( ( austen.token.count(x) / len(austen.token) ) - ( ( ( austen.token.count(x) / len(austen.token) ) + ( bronte.token.count(x) / len(bronte.token) ) + ( disputed.token.count(x) / len(disputed.token) ) ) / 3) )
            z = z / ( statistics.stdev([( austen.token.count(x) / len(austen.token) ), ( bronte.token.count(x) / len(bronte.token) ), ( disputed.token.count(x) / len(disputed.token) )]) )
            temp.append(z)

            z = 0
            z = ( ( bronte.token.count(x) / len(bronte.token) ) - ( ( ( austen.token.count(x) / len(austen.token) ) + ( bronte.token.count(x) / len(bronte.token) ) + ( disputed.token.count(x) / len(disputed.token) ) ) / 3) )
            z = z / ( statistics.stdev([( austen.token.count(x) / len(austen.token) ), ( bronte.token.count(x) / len(bronte.token) ), ( disputed.token.count(x) / len(disputed.token) )]) )
            temp.append(z)

            z = 0
            z = ( ( disputed.token.count(x) / len(disputed.token) ) - ( ( ( austen.token.count(x) / len(austen.token) ) + ( bronte.token.count(x) / len(bronte.token) ) + ( disputed.token.count(x) / len(disputed.token) ) ) / 3) )
            z = z / ( statistics.stdev([( austen.token.count(x) / len(austen.token) ), ( bronte.token.count(x) / len(bronte.token) ), ( disputed.token.count(x) / len(disputed.token) )]) )
            temp.append(z)
            
            #the temp list now has 3 values, these are now appended to dump list
            #so dump list has lists of 3 values inside it
            dump.append(temp[:])
            #the word is then removed from common_tokens list
            #this is done so that in subsequent calculations for other .txt files, we dont calculate z scores for words that have already been calculated for (if statement in loop does this).
            #as austen, bronte, disputed can have the same word, but it only exists once in common_token list 
            common_tokens.pop(common_tokens.index(x))


    #3 empty lists are created to save the .txt file specific z scores for the words
    z_austen = []
    z_bronte = []
    z_disputed = []
    
    #as we set the insertion sequence initially as 1.austen, 2.bronte, 3.disputed 
    #we sort the values based on it 
    #these values are then further also used in Q4.b2
    for x in dump:
        z_austen.append(x[0])
        z_bronte.append(x[1])
        z_disputed.append(x[2])
    
    #bar chart drawing process starts from here 
        #https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm
        #https://pythonspot.com/matplotlib-bar-chart/
    n_groups = len(z_austen)
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8

    #datasets are provided and characteristics such as color, etc are set
    rects1 = plt.bar(index, z_austen, bar_width,alpha=opacity,color='b',label='Austen')
    rects2 = plt.bar(index + bar_width, z_bronte, bar_width,alpha=opacity,color='g',label='Bronte')
    rects3 = plt.bar(index + (bar_width*2), z_disputed, bar_width,alpha=opacity,color='r',label='Disputed')

    #legend is put in place
    plt.xlabel('Common most used words from the given .txt files')
    plt.ylabel('Z scores')
    plt.title('Z Scores for .txt files')
    plt.legend()

    #chart/graph is created/shown
    plt.tight_layout()
    plt.show()


    #Question 4.b2 starts here 
    #the delta B values for lists of d_scores is calculated and printed in the following parts
        #https://www.w3schools.com/python/ref_func_abs.asp
    deltaBA = 0 
    for x in range(0,len(z_disputed)):
        deltaBA = deltaBA + abs( z_bronte[x] - z_austen[x] )

    deltaBD = 0
    for x in range(0,len(z_disputed)):
        deltaBD = deltaBD + abs( z_bronte[x] - z_disputed[x] )

    deltaAD = 0
    for x in range(0,len(z_disputed)):
        deltaAD = deltaAD + abs( z_austen[x] - z_disputed[x] )

    print("deltaV(bronte,austen): ",deltaBA)
    print("deltaV(bronte,disputed): ",deltaBD)
    print("deltaV(austen,disputed): ",deltaAD)




#here we just call the created functions

#Question 2 and 3
allABTraven(3)
allABTgullivers(3)

#Question 4.a
allABTausten(5)
allABTbronte(5)
allABTdisputed(5)

#Question 4.b
whoWroteIT()
