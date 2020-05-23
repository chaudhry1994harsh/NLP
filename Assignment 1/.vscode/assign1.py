import nltk as nl
import re
from collections import Counter

class tokenizor():
    token = list
    def __init__(self,name):
        super().__init__()
        data=open(name).read()
        token=re.split(r'\s+' , data)
        self.token = [w.lower() for w in token]
        self.token = [re.sub(r'\W+', r'',w) for w in self.token]
        while '' in self.token:
            self.token.pop(self.token.index(''))

    def ONEgram(self):
        g = self.token
        ct = Counter(g)
        print(ct.most_common(3))

    def TWOgram(self):
        g=[]
        for x in range(0,len(self.token)-1):
            g.append(self.token[x]+" "+self.token[x+1])
        ct = Counter(g)
        print (ct.most_common(3))

    def THREEgram(self):
        g=[]
        for x in range(0,len(self.token)-2):
            g.append(self.token[x]+" "+self.token[x+1]+" "+self.token[x+2])
        ct = Counter(g)
        print (ct.most_common(3))

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


raven = tokenizor("raven.txt");
raven.ONEgram()
raven.TWOgram()
raven.THREEgram()
print(raven.tLength())
print(raven.vocab())
print(raven.TTR())
print(raven.meanLen())


gulliversT = tokenizor("gullivers-travels.txt");