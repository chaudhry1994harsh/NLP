import pickle
#https://radimrehurek.com/gensim/models/keyedvectors.html
#https://web.stanford.edu/class/cs224n/materials/Gensim%20word%20vector%20visualization.html
def loadKVs(KVFile):
    with open(KVFile, "rb") as f:
        kv1 = pickle.load(f)
        kv2 = pickle.load(f)
        return kv1,kv2



def evaluate(KVFile):
    # c1 closest
    kvW2V, kvPCA = loadKVs(KVFile)
    close=['playstation','walk','love']
    for i in close:
        print(' '.join([i[0] for i in kvW2V.most_similar(i)[:3]]))
    for i in close:
        print(' '.join([i[0] for i in kvPCA.most_similar(i)[:3]]))

    # c2 doesnt_match outlier
    print('----------------Outlier---------------')
    outlier1=['mario', 'zelda', 'kirby', 'microsoft']
    outlier2 = ['january', 'july', 'december', 'year']
    print(kvW2V.doesnt_match(outlier1))
    print(kvPCA.doesnt_match(outlier1))

    print(kvW2V.doesnt_match(outlier2))
    print(kvPCA.doesnt_match(outlier2))
    print('---------------------------------------')
    # c3 analogies

    def analogy(x1, x2, y1):
        result1 = kvW2V.most_similar(positive=[y1, x2], negative=[x1])
        result2 = kvPCA.most_similar(positive=[y1, x2], negative=[x1])
        return  result2[0][0],result1[0][0]

    #resW2V, resPCA =analogy('son','daughter','boy')
    an_list=[['son','daughter','boy'],['n64','nintendo','playstation'],['acceptable','unacceptable','reasonable'],['good','better','tough'],['go','going','play']]
    for item in an_list:
        print(item, analogy(*item))





