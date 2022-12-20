from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk



with open("question.txt","r",encoding="utf-8") as file:
    question = file.read()
with open("essay.txt","r",encoding="utf-8") as file:
    essay = file.read()

#essay tokenize
text = essay
stopwords = set(stopwords.words("english"))
words = word_tokenize(question)
qwords = []
for word in words:
    word =word.lower()
    if word in stopwords:
        continue
   
    else:
        if word.isalpha():
            qwords.append(word)

# freqTable = finalwords
sentences = sent_tokenize(essay)
sentValue = dict()
for sentence in sentences:
    sentValue[sentence]=0
print("\nKeyowords taken from question")
print(qwords)
print("-----------------------------------------------------------------")

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

print("similar words\n")
swords=[]
for qword in qwords:
    swords.extend(synonym_antonym_extractor(qword))
swords = [*set(swords)]
print(len(swords))


for sentence in sentences:
    for word in swords:
        if word in sentence.lower():
            sentValue[sentence]+=1
            
#print(sentValue)  


#Average sentence value
sumVal = 0
for sentence in sentValue:
    sumVal+=sentValue[sentence]
avg = sumVal/len(sentValue)
print("\n Sentence Scoring")
print(sentValue)
print("\n\n---------------------------------------------------\n\n")
print("Average Relavancy of sentences: " + str(avg))


if avg > 4.5 :
    relavancy_ielts=9
 
elif avg > 4 :
    relavancy_ielts=8
 
elif avg > 3.5:
  relavancy_ielts=7

elif avg > 3 :
    relavancy_ielts=6

elif avg > 2.5 :
   relavancy_ielts=5

elif avg > 2 :
    relavancy_ielts=4

elif avg > 1.5 :
   relavancy_ielts=3

elif avg > 1 :
    relavancy_ielts=2

else:
   relavancy_ielts=1

print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
print("IELTS Score for Task Achievemnet :" ,int(relavancy_ielts))
print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")