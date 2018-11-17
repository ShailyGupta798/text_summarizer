import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
f=open('text_data.txt')
text=f.read()
stopWords=set(stopwords.words("english"))
words=word_tokenize(text)

freqTable=dict()
for word in words:
    word=word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word]+=1
    else:
        freqTable[word]=1

sentences=sent_tokenize(text)
sentenceValue=dict()

for sentence in sentences:
    for wordValue in freqTable.keys():
        if wordValue in sentence.lower():
            if sentence[:12] in sentenceValue:
                sentenceValue[sentence[:12]]+=freqTable[wordValue]
            else:
                sentenceValue[sentence[:12]] =freqTable[wordValue]

sumValues =0
for sentence in sentenceValue:
    sumValues +=sentenceValue[sentence]
    
average=int(sumValues/len(sentenceValue))

summary= ''
for sentence in sentences:
    if sentence[:12] in sentenceValue and sentenceValue[sentence[:12]] > (average):
        summary += " " + sentence
        
print( summary)
