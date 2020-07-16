#https://stackoverflow.com/questions/26570944/resource-utokenizers-punkt-english-pickle-not-found
import nltk as nl
import math
import statistics
import numpy as np
from nltk.corpus import wordnet as wn
from prettytable import PrettyTable


# 4 functions have been made to solve Q1(a) to improve readability only. We realise the same could have been done in one function :)
# 5th is a checker function that prints data at every intermediate step i.e., at the  end of every function  

# 1st funcion to be run 
# This function takes a string input and returns a list of tokens to be processed further
def tokenCreate(sentence):
    token = nl.word_tokenize(sentence)
    return token

# 2nd function to be run 
# This function takes the tokens made by the 1st function and allocates POS tags to each word, returns a list of lists 
#https://medium.com/@muddaprince456/categorizing-and-pos-tagging-with-nltk-python-28f2bc9312c3#:~:text=The%20POS%20tagger%20in%20the,CD%20cardinal%20digit
#https://medium.com/greyatom/learning-pos-tagging-chunking-in-nlp-85f7f811a8cb
def insertPOS(token):
    pos = nl.pos_tag(token)
    pos = [list(ele) for ele in pos]
    # pos in the above line is a list of tuples, to make it editable it is converted into a list of list (method found on geeksforgeeks)
    # each POS tag inserted by nltk is processed into simpler tags, 
        # also replaces any tag that does not refer to NOUNS, ADJECTIVES, ADVERBS or VERBS with '-'. As only those 4 are supported by WordNet
    for x in pos:
        if(x[1]=='RB' or x[1]=='RBR' or x[1]=='RBS'):
            x[1]  = 'ADV'
        elif(x[1]=='VBG' or x[1]=='VBP' or x[1]=='VB' or x[1]=='VBD' or x[1]=='VBN' or x[1]=='VGZ'):
            x[1]  = 'VERB'
        elif(x[1]=='JJ' or x[1]=='JJR' or x[1]=='JJS' ):
            x[1]  = 'ADJ'
        elif(x[1]=='NN' or x[1]=='NNP' or x[1]=='NNPS' or x[1]=='NNS'):
            x[1]  = 'NOUN'
        else:
            x[1] = '-'
            '''print("find me i("+x[1]+") am lost!!")'''
    return pos


# 3rd function that takes input from the second function and returns a list of lists 
# This function checks the basic tags assigned to every word in the previous steps and,
    # uses that information to replace the basic tag in the list with the senseKey found with the help of WordNet 
#https://www.nltk.org/howto/wordnet.html
def wordNetSysNet(posSpeech):
    for x in posSpeech:
        if(x[1]  == 'NOUN'):
            x[1] = wn.synsets(x[0], pos = wn.NOUN)[0].lemmas()[0].key()
        elif(x[1]  == 'VERB'):
            x[1] = wn.synsets(x[0], pos = wn.VERB)[0].lemmas()[0].key()
        elif(x[1]  == 'ADJ'):
            x[1] = wn.synsets(x[0], pos = wn.ADJ)[0].lemmas()[0].key()
        elif(x[1]  == 'ADV'):
            x[1] = wn.synsets(x[0], pos = wn.ADV)[0].lemmas()[0].key()
    return posSpeech


# 4th fuction that takes input from the 3rd function and an integer (to print which input case we are printing the table for)
# returns nothing and is only used for draing a table 
#https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
def drawTable(keys,number):
    table = PrettyTable(['('+str(number)+')', 'SenseKey'])
    for x in keys:
        table.add_row([x[0],x[1]])
    print (table)


# simple function that prints the intermediate results from function 1 to 4
# serves no real purpose but is here for the reader's convenience to check and understand intermediate results if required 
def checker(ip):
    token = tokenCreate(ip1)
    print(token)
    posSpeech = insertPOS(token)
    print (posSpeech)
    senseKEY = wordNetSysNet(posSpeech)
    print (senseKEY)
    drawTable(senseKEY,'testCase')


# the 3 inputs given in the question 
ip1 = 'do you train for passing tests or do you train for creative inquiry'
ip2 = 'how it is we have so much information, but know so little'
ip3 = 'it is the responsibility of intellectuals to speak the truth and expose lies'

# all the functions called in one line for the above 3 inputs, draws 3 tables with found senseKeys
drawTable(wordNetSysNet(insertPOS(tokenCreate(ip1))),1)
drawTable(wordNetSysNet(insertPOS(tokenCreate(ip2))),2)
drawTable(wordNetSysNet(insertPOS(tokenCreate(ip3))),3)

