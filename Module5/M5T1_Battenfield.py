# coding: utf-8
get_ipython().run_line_magic('load', '1-8.py')
# %load 1-8.py
from textblob import TextBlob
text = "Today is a beautiful day. Tommorrow looks like bad weather."
blob = TextBlob(text)
blob
exercise_blob = TextBlob('This is a TextBlob')
exercise_blob
blob.sentences
blob.words
ex = TextBlob('My old computer is slow. My new one is fast.')
ex.sentences
ex.words
blob
blob.tags
TextBlob('My dog is cute').tags

#get_ipython().run_line_magic('save', '1-8 textblob_sample 1-8')
blob
blob.noun_phrases
TextBlob('The red brick factory is for sale').noun_phrases
blob
blob.sentiment
get_ipython().run_line_magic('precision', '3')
