import nltk
import string
from nltk.stem.porter import PorterStemmer
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import itertools

from nltk.tokenize import sent_tokenize
from nltk.corpus import wordnet
import keybert
from keybert import KeyBERT
# Text Pre-processing

from nltk.corpus import wordnet

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase




def Text_preprocess(text):
    
    #Decontraction
    pre_sample_text=decontracted(text)
   
    
    #remove words with numbers python
    #pre_sample_text = re.sub("\S*\d\S*", "",pre_sample_text).strip()
    
    #remove special character
    pre_sample_text= re.sub('[^A-Za-z0-9]+', ' ',pre_sample_text)
    
    
    #Removing stopwords
    stopwords= set(['the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"])
    pre_sample_text = ' '.join(e for e in pre_sample_text.split() if e.lower() not in stopwords)

    #Chunking
    chunked = ne_chunk(pos_tag(word_tokenize(pre_sample_text)))
    Tokens=[ w[0] if isinstance(w, tuple) else "_".join(t[0] for t in w) for w in chunked ]
    pre_sample_text=' '.join(Tokens)

    #Lowercase
    pre_sample_text=pre_sample_text.lower()

    return pre_sample_text


# Keyword Finder returns the top keywords and top keyphrases

# phrases_maxlen=set the maximum length of the phrases

# n_keywords=set the number of keywords required


def Keyword_Finder(doc,phrases_maxlen,n_keywords):
    
    keywords_list=[]
    keyphrases_list=[]
    
    pre_processed_doc=Text_preprocess(doc)
    
    kw_model = KeyBERT()
    print('Highlighted Keywords\n')
    keywords = kw_model.extract_keywords(pre_processed_doc,top_n=n_keywords,diversity=0.7,use_maxsum=True,highlight=True)
    keywords_list.append(keywords)
    print('Highlighted Keyphrases\n')
    phrases=keywords = kw_model.extract_keywords(pre_processed_doc,keyphrase_ngram_range=(1,phrases_maxlen),highlight=True,top_n=n_keywords,use_maxsum=True,diversity=0.7)
    keyphrases_list.append(phrases)
    return keywords_list,keyphrases_list

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

doc = blog
len(doc.split(" "))
doc = blog
#len(doc.split(" "))
phrases_maxlen=2
n_keywords=10

keywords,keyphrases=Keyword_Finder(doc,phrases_maxlen,n_keywords)

words=[]
for k,v in keywords[0]:
    words.append(k)
key_image=' '.join(words)
print(key_image)
print(words)

#words = ["artificial inteligence","artificial inteligence robot", "google research facility ", "elon Musk","google"]

#Converting text to audio 

# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = blog


# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False,tld='co.in')

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("AudioClip.mp3")

# Loading audioclip and getting its duration
audioclip =AudioFileClip("AudioClip.mp3")
audioclip_duration=audioclip.duration
print(audioclip_duration)

