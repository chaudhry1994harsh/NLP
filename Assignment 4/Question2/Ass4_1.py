import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
from sklearn.decomposition import PCA
from Assignment_4C import createKVs
from Assignment_4c1 import evaluate
import pickle
def rev_corpus(reviews):
    with open('assignment-semantics/'+reviews, 'r') as reviews:
        input= reviews.read()
        revListDoc=input.split('\n')
        unique_list=list(set(input.split()))
        return revListDoc,unique_list


def update_co_mat(x, window_len):
    # Get all the words in the sentence and store it in an array wrd_lst
    wrd_list = x.split(' ')
    #print('corpus word size',len(wrd_list))

    # Consider each word as a focus word
    for focus_wrd_indx, focus_wrd in enumerate(wrd_list):
        focus_wrd = focus_wrd.lower()
        # Get the indices of all the context words for the given focus word
        for contxt_wrd_indx in range((max(0, focus_wrd_indx - window_len)),
                                     (min(len(wrd_list), focus_wrd_indx + window_len + 1))):
            # If context words are in the unique words list
            if  focus_wrd=='':
                continue
            if wrd_list[contxt_wrd_indx] in uniq_wrds:
                # To identify the row number, get the index of the focus_wrd in the uniq_wrds list
                try:
                    co_mat_row_indx = uniq_wrds.index(focus_wrd)
                except:
                    print(wrd_list)
                    print(wrd_list[contxt_wrd_indx], wrd_list[contxt_wrd_indx-1],wrd_list[contxt_wrd_indx+1])

                # To identify the column number, get the index of the context words in the uniq_wrds list
                co_mat_col_indx = uniq_wrds.index(wrd_list[contxt_wrd_indx])

                # Update the respective columns of the corresponding focus word row
                co_mat[co_mat_row_indx][co_mat_col_indx] += 1

def createSave_co_mat(window_size,type):
    print('total docs ', len(doc))
    count = 0
    for sentence in doc:
        print('doc nmbr :',count)
        update_co_mat(sentence,window_size)
        count+=1
    filename='file_co_'+type+'.obj'
    with open(filename, "wb") as f:
        pickle.dump(doc, f,protocol = 4)
        pickle.dump(uniq_wrds, f,protocol = 4)
        pickle.dump(co_mat,f,protocol = 4)
    return filename
def runPCA(filename):
    with open(filename, "rb") as f:
        doc = pickle.load(f)
        print(len(doc))
        uniq_wrds = pickle.load(f)
        print(len(uniq_wrds))
        co_mat = pickle.load(f)
        print(len(co_mat), len(co_mat[0]))

    pca = PCA(n_components=10)
    principalComponents = pca.fit_transform(co_mat)
    principalDf = pd.DataFrame(data=principalComponents
                               , index=[i for i in uniq_wrds]
                               , columns=['PC' + str(i) for i in range(1, 11)])
    filenamePCA='DF'+filename
    with open(filenamePCA, "wb") as f:
        pickle.dump(principalDf, f)
        pickle.dump(principalComponents, f)
    return filenamePCA

def A41(filename):
    lst=['does', 'racing', 'zelda', 'fighting', 'nintendo', 'is', 'red']
    with open(filename, "rb") as f:
        doc= pickle.load(f)
        print(len(doc))
        uniq_wrds = pickle.load(f)
        print(len(uniq_wrds))
        co_mat = pickle.load(f)
        print(len(co_mat), len(co_mat[0]))

    for i in lst:
        print(i, end=' ')
        for j in lst:
            i_ind=uniq_wrds.index(i)
            j_ind = uniq_wrds.index(j)
            print( co_mat[i_ind][j_ind], end=' ')
        print()
def a42(filename):
    with open(filename, "rb") as f:
        PCAdf= pickle.load(f)
        PCAdf.to_excel('Assignment_4B.xlsx')
def createKV(PCA_file, CO_file,type):
    kVFIle=createKVs(PCA_file, CO_file, type)
    print(kVFIle)
    evaluate(kVFIle)

reviews= '2000-reviews.txt'

doc, uniq_wrds= rev_corpus(reviews)
print('Corpus pickeled total unique words ',len(uniq_wrds))
n = len(uniq_wrds)
co_mat = np.zeros((n,n))
window=10
type=str(window)+reviews
#CO_file=createSave_co_mat(window, type)
CO_file='file_co_102000-reviews.txt.obj'
print('Co matrix written')
PCA_file=runPCA(CO_file)#CO_file
print(CO_file, PCA_file)
createKV(PCA_file, CO_file,type)



