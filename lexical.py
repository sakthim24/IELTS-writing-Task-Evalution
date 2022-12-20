from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from textblob import Word




with open("essay.txt","r",encoding="utf-8") as file:
    essay = file.read()

#essay tokenize.
text = essay
stopwords = set(stopwords.words("english"))

#words_tokenize

words = word_tokenize(essay)
uwords = []
for word in words:
    if word.isalpha() :
        uwords.append(word)

#spelling checker
def check_word_spelling(word):
    
    word = Word(word)
    
    result = word.spellcheck()
    
    if word == result[0][0]:
        return False
    else:
        return True

#calculaing mistake score

mistakes=0
for word in uwords:
    if(check_word_spelling(word)):
        mistakes+=1

mistakes_percent=(mistakes/len(uwords))*100



print("\n\n---------------------------------------------------\n\n")
print("mistake percentage : " + str(mistakes_percent))


if mistakes_percent < 3:
    spelling_score=9
 
elif mistakes_percent < 6:
     spelling_score=8
 
 
elif mistakes_percent < 9:
     spelling_score=7
 

elif mistakes_percent < 12:
     spelling_score=6
 

elif mistakes_percent < 15:
    spelling_score=5
 

elif mistakes_percent < 18:
    spelling_score=4
 

elif mistakes_percent < 21 :
    spelling_score=3
 

elif mistakes_percent < 25:
     spelling_score=2
 
else:
     spelling_score=1

print("Spelling Mistakes  score :",spelling_score)

#Scoring of Range of vocabulary

words = word_tokenize(essay)
used_words = []
unique_words = []
common_words_count=0
for word in words:
    word =word.lower()
    if word in stopwords:
        common_words_count+=1
        continue 
    else:
        if word.isalpha():
            used_words.append(word)
 
unique_words = [*set(used_words)]


vocabulary_value=(len(unique_words)/len(used_words))*100
print("\n\n---------------------------------------------------\n\n")
print("Vocabulary Range percentage :",vocabulary_value)

#vocabulary score

if vocabulary_value > 90:
    vocabulary_score=9
 
elif vocabulary_value > 80:
     vocabulary_score=8
 
 
elif vocabulary_value > 70:
     vocabulary_score=7
 

elif vocabulary_value > 60 :
     vocabulary_score=6
 

elif vocabulary_value > 50 :
    vocabulary_score=5
 

elif vocabulary_value > 40:
    vocabulary_score=4
 

elif vocabulary_value > 30 :
    vocabulary_score=3
 

elif vocabulary_value > 20:
     vocabulary_score=2
 
else:
     vocabulary_score=1 
     
print("Range of Vocabulary score :",vocabulary_score)

print("\n\n---------------------------------------------------\n\n")

#common words usage score

cw_value=(common_words_count/len(uwords))*100
print("Common words usage percentage :",cw_value)

if cw_value < 30:
    cw_score=9
 
elif cw_value < 35:
     cw_score=8
 
 
elif cw_value < 40:
     cw_score=7
 

elif cw_value < 45 :
     cw_score=6
 

elif cw_value < 50 :
    cw_score=5
 

elif cw_value < 55:
    cw_score=4
 

elif cw_value < 60 :
    cw_score=3
 

elif cw_value < 65:
     cw_score=2
 
else:
     cw_score=1 

print("Common words usage score :",cw_score)

print("\n\n---------------------------------------------------\n\n")

lexical_ielts=((1.5*spelling_score)+(2.5*vocabulary_score)+cw_score)/5
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
print("IELTS Score for Lexical Resource :" ,int(lexical_ielts))
print("\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")

