#import nltk as nl

#https://stackabuse.com/python-for-nlp-working-with-text-and-pdf-files/

data_raven = open("E:\\WorkSpaces\\NLP\\Assignment 1\\.vscode\\raven.txt")
data_gTravels = open("E:\\WorkSpaces\\NLP\\Assignment 1\\.vscode\\gullivers-travels.txt")

data_raven.seek(0)
print(data_raven.read())

data_gTravels.seek(0)
print(data_gTravels.read())

data_gTravels.seek(0)
#token_gTravels = ntlkdata_gTravels

#token_raven = 