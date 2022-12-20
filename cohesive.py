from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from textblob import TextBlob

with open("question.txt","r",encoding="utf-8") as file:
    question = file.read()
with open("essay.txt","r",encoding="utf-8") as file:
    essay = file.read()

stopwords = set(stopwords.words("english"))
sentences = sent_tokenize(essay)
lm= WordNetLemmatizer()

#Generating similar words
def synonym_antonym_extractor(qword):
     from nltk.corpus import wordnet
     synonyms = []
     antonyms = []

     for syn in wordnet.synsets(qword):
          for l in syn.lemmas():
               synonyms.append(l.name())
               if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())

     return synonyms

def Lemmatizatize(sentence):
    sent = TextBlob(sentence)
    tag_dict = {"J": 'a', "N": 'n', "V": 'v', "R": 'r'}
    words_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]   
    lemma_list = []
    for wd,tag in words_tags:
        if wd not in stopwords:
            lemma_list.append(wd.lemmatize(tag))
    final_list=[]
    for word in lemma_list:
        final_list.extend(synonym_antonym_extractor(word))
    
    final_list = [*set(final_list)]
    return final_list
 
# match=0
# print(sentences[5])
# pwords=Lemmatizatize(sentences[5])
# print(pwords)
# print(sentences[6])
# nwords=Lemmatizatize(sentences[6])
# print(nwords)
# for word in sentences[6]:
        
#          if word in pwords:
#              print(word)
#              match+=1
# print("keep" in pwords)
sentValue = dict()
for sentence in sentences:
    sentValue[sentence]=0

for i in range(len(sentences)-1):
    
    next=sentences[i+1]
    pwords=Lemmatizatize(sentences[i])
    nwords=Lemmatizatize(sentences[i+1])
    words = word_tokenize(sentences[i+1])
    for word in words:
        if word in pwords:
            sentValue[sentences[i+1]]+=1
    

#Average sentence value
sumVal = 0
for sentence in sentValue:
    sumVal+=sentValue[sentence]
avg = sumVal/len(sentValue)
print("\n Sentence Scoring")
print(sentValue)
print("\n\n---------------------------------------------------\n\n")
print("Average Coherence of sentences: " + str(avg))

#Scoring Cohesiveness of sentences


if avg  > 2:
    cohesive_score=9
 
elif avg > 1.75:
     cohesive_score=8
 
 
elif avg > 1.5:
     cohesive_score=7
 

elif avg > 1.25:
     cohesive_score=6
 

elif avg > 1:
    cohesive_score=5
 

elif avg > 0.8:
    cohesive_score=4
 

elif avg > 0.6 :
    cohesive_score=3
 

elif avg > 0.4:
     cohesive_score=2
 
else:
     cohesive_score=1


print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
print("IELTS Score for Cohesive And Coherence :" ,cohesive_score)
print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")


