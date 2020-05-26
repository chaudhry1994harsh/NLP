#https://stackoverflow.com/questions/26570944/resource-utokenizers-punkt-english-pickle-not-found
import nltk as nl
import re
from collections import Counter

#https://stackoverflow.com/questions/12703842/how-to-tokenize-natural-english-text-in-an-input-file-in-python
#https://www.nltk.org/book/ch03.html
#open file 
data_raven = open("raven.txt").read()
data_gulliversT = open("gullivers-travels.txt").read()

#data_gTravels = open("E:\\WorkSpaces\\NLP\\Assignment 1\\.vscode\\gullivers-travels.txt")
#tokenize and set and lowercase using ntlk
'''token_raven = nl.word_tokenize(data_raven)
token_raven = sorted(set(token_raven))
token_raven = [w.lower() for w in token_raven]
print(token_raven)
len(token_raven)'''

#tokenize and lowercase using re
tok_raven = re.split(r'\s+' , data_raven)
tok_raven = [w.lower() for w in tok_raven]

tok_gulliversT = re.split(r'\s+' , data_gulliversT)
tok_gulliversT = [w.lower() for w in tok_gulliversT]


#https://docs.python.org/3.4/library/re.html
#remove punctuation
tok_raven = [re.sub(r'\W+', r'',w) for w in tok_raven]

tok_gulliversT = [re.sub(r'\W+', r'',w) for w in tok_gulliversT]


#remove blank space tokens 
while '' in tok_raven:
    tok_raven.pop(tok_raven.index(''))

while '' in tok_gulliversT:
    tok_gulliversT.pop(tok_gulliversT.index(''))


#https://stackoverflow.com/questions/48342492/python-maximum-number-of-times-element-appear-in-list
#1gram
raven_1g = tok_raven;
r1g = Counter(raven_1g)
print(r1g.most_common(3))

gulliversT_1g = tok_gulliversT;
g1g = Counter(gulliversT_1g)
print(g1g.most_common(3))


#2gram
raven_2g = [];
for x in range(0,len(tok_raven)-1):
    raven_2g.append(tok_raven[x]+" "+tok_raven[x+1])
r2g = Counter(raven_2g)
print (r2g.most_common(3))

gulliversT_2g = [];
for x in range(0,len(tok_gulliversT)-1):
    gulliversT_2g.append(tok_gulliversT[x]+" "+tok_gulliversT[x+1])
g2g = Counter(gulliversT_2g)
print (g2g.most_common(3))


#3gram
raven_3g = []
for x in range(0,len(tok_raven)-2):
    raven_3g.append(tok_raven[x]+" "+tok_raven[x+1]+" "+tok_raven[x+2])
r3g = Counter(raven_3g)
print(r3g.most_common(3))

gulliversT_3g = []
for x in range(0,len(tok_gulliversT)-2):
    gulliversT_3g.append(tok_gulliversT[x]+" "+tok_gulliversT[x+1]+" "+tok_gulliversT[x+2])
g3g = Counter(gulliversT_3g)
print(g3g.most_common(3))


#set token for vocab and calculate total tokens 
len_raven = len(tok_raven)
vtok_raven = sorted(set(tok_raven))
vocab_raven = len(vtok_raven)
print("vocab raven: ",vocab_raven)
print("len raven: ", len_raven)

len_gulliversT = len(tok_gulliversT)
vtok_gulliversT = sorted(set(tok_gulliversT))
vocab_gulliversT = len(vtok_gulliversT)
print("vocab gulliver's: ",vocab_gulliversT)
print("len gulliversT: ", len_gulliversT)

#https://carla.umn.edu/learnerlanguage/spn/comp/activity4.html
#calculate TTR
TTR_raven = vocab_raven/len_raven
print(TTR_raven)
TTR_gulliversT = vocab_gulliversT/len_gulliversT
print(TTR_gulliversT)

#calculate mean token length
mlen_raven = 0
for x in tok_raven:
    mlen_raven = mlen_raven + len(x)
print(mlen_raven)
mlen_raven = mlen_raven/len_raven
print(mlen_raven)

mlen_gullivers = 0
for x in tok_gulliversT:
    mlen_gullivers = mlen_gullivers + len(x)
print(mlen_gullivers)
mlen_gullivers = mlen_gullivers/len_gulliversT
print(mlen_gullivers)


#https://www.w3schools.com/python/python_howto_remove_duplicates.asp
#https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/
#find average c in zipf
z=0
rank_raven = [item for items, c in Counter(tok_raven).most_common() for item in [items] * c] 
rank_raven = list(dict.fromkeys(rank_raven))
for x in vtok_raven:
    z = z + (((tok_raven.count(x))/(len(tok_raven)))*((rank_raven.index(x))+1))
c_raven = z/vocab_raven
print(c_raven)

z = 0
rank_gulliversT = [item for items, c in Counter(tok_gulliversT).most_common() for item in [items] * c] 
rank_gulliversT = list(dict.fromkeys(rank_gulliversT))
for x in vtok_gulliversT:
    z = z + (((tok_gulliversT.count(x))/(len(tok_gulliversT)))*((rank_gulliversT.index(x))+1))
c_gulliversT = z/vocab_gulliversT
print(c_gulliversT)


