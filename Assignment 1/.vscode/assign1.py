import nltk as nl
import re
from collections import Counter

class tokenizor():
    token = list
    def __init__(self,name):
        super().__init__()
        data=open(name,encoding="utf-8").read()
        token=re.split(r'\s+' , data)
        self.token = [w.lower() for w in token]
        self.token = [re.sub(r'\W+', r'',w) for w in self.token]
        while '' in self.token:
            self.token.pop(self.token.index(''))

    def ONEgram(self,x):
        g = self.token
        ct = Counter(g)
        print(ct.most_common(x))

    def TWOgram(self,y):
        g=[]
        for x in range(0,len(self.token)-1):
            g.append(self.token[x]+" "+self.token[x+1])
        ct = Counter(g)
        print (ct.most_common(y))

    def THREEgram(self,z):
        g=[]
        for x in range(0,len(self.token)-2):
            g.append(self.token[x]+" "+self.token[x+1]+" "+self.token[x+2])
        ct = Counter(g)
        print (ct.most_common(z))

    def tLength(self):
        return len(self.token)

    def vocab(self):
        return len(sorted(set(self.token)))

    def TTR(self):
        return (len(sorted(set(self.token))))/(len(self.token))
    
    def meanLen(self):
        mlen_raven = 0
        for x in self.token:
            mlen_raven = mlen_raven + len(x)
        return mlen_raven/len(self.token)

    def zipfEstimateC(self):
        z=0 
        r = [item for items, c in Counter(self.token).most_common() for item in [items] * c] 
        r= list(dict.fromkeys(r))
        rt = sorted(set(self.token))
        for x in rt:
            z = z + ( ( (self.token.count(x)) / (len(self.token)) ) * ( (r.index(x)) +1) )
        c = z/len(sorted(set(self.token)))
        return c 


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
    print("zipf's C:",raven.zipfEstimateC(),"\n")

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
    print("zipf's C:",gulliversT.zipfEstimateC(),"\n")

def allABTausten(x):
    print("AUSTEN")
    austen = tokenizor("austen.txt");
    austen.ONEgram(x)
    austen.TWOgram(x)
    austen.THREEgram(x)
    print("Tokens: ",austen.tLength())
    print("Vocabulary: ",austen.vocab())
    print("TTR: ",austen.TTR())
    print("Mean length: ",austen.meanLen(),"\n")
    #austen.zipfEstimateC()

def allABTbronte(x):
    print("BRONTE")
    bronte = tokenizor("bronte.txt");
    bronte.ONEgram(x)
    bronte.TWOgram(x)
    bronte.THREEgram(x)
    print("Tokens: ",bronte.tLength())
    print("Vocabulary: ",bronte.vocab())
    print("TTR: ",bronte.TTR())
    print("Mean length: ",bronte.meanLen(),"\n")
    #bronte.zipfEstimateC()

def allABTdisputed(x):
    print("DISPUTED")
    disputed = tokenizor("disputed.txt");
    disputed.ONEgram(x)
    disputed.TWOgram(x)
    disputed.THREEgram(x)
    print("Tokens: ",disputed.tLength())
    print("Vocabulary: ",disputed.vocab())
    print("TTR: ",disputed.TTR())
    print("Mean length: ",disputed.meanLen(),"\n")
    #disputed.zipfEstimateC()


allABTraven(3)
allABTgullivers(3)

allABTausten(5)
allABTbronte(5)
allABTdisputed(5)