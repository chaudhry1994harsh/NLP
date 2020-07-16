from gensim.models.keyedvectors import WordEmbeddingsKeyedVectors
import pickle
def createWordandVectorList():
    with open('assignment-semantics\w2v-50d.txt',encoding="utf8") as file:
        w2v=file.read()
        w2vlist=w2v.split('\n')
        wordlist=[]
        vectorList=[]
        word, vector= w2vlist[1].split(' ', 1)
        for i in range(1, len(w2vlist)-1):
            word, vector=w2vlist[i].split(' ', 1)
            wordlist.append(word)
            vectorList.append(list(map(float, vector.split(' '))))

        with open('ASS4c1.obj', "wb") as f:
            pickle.dump(wordlist, f)
            pickle.dump(vectorList,f)

def loadWordANdVectorsW2V():
    with open('ASS4c1.obj', "rb") as f:
        wordList = pickle.load(f)
        vectorList = pickle.load(f)
        print(len(wordList))
        print(len(vectorList))
        print('nbcsvbdsn')
    return wordList, vectorList

def loadWordANdVectorsPCA(DFFile, COFIle):
    with open(DFFile, "rb") as f:
        PCAdf= pickle.load(f)
        PCA= pickle.load(f)
    with open(COFIle, "rb") as f:
        doc= pickle.load(f)
        uniq_wrds = pickle.load(f)
        co_mat = pickle.load(f)
    return uniq_wrds, PCA.tolist()

def createKVs(DFFile, COFIle,type):
    #createWordandVectorList() # to create  word and vector list for wiki 50

    # wordList - list of words
    # vectorList - list of the vector corresponding to the words

    wordListW2V, vectorListW2V = loadWordANdVectorsW2V()
    wordListPCA, vectorListPCA = loadWordANdVectorsPCA(DFFile, COFIle)

    w2v_len = 50
    PCA_len = 10
    kv1 = WordEmbeddingsKeyedVectors(w2v_len)
    kv2 = WordEmbeddingsKeyedVectors(PCA_len)


    kv1.add(wordListW2V, list(vectorListW2V))
    kv2.add(wordListPCA, vectorListPCA)
    filename ='KV'+type+'.obj'
    with open(filename, "wb") as f:
        pickle.dump(kv1, f)
        pickle.dump(kv2, f)
    print(kv1.most_similar('love')) # gives the list of words similar to word1
    return filename