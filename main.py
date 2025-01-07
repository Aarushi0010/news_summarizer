import tkinter as tk 
import nltk 
from textblob import TextBlob 
from newspaper import Article 

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

url = 'https://thesentry.org/2024/12/12/80685/deepening-descent-into-corruption-in-libya-parallels-with-syria/'

article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title : {article.title}')
print(f'Author : {article.authors}')
print(f'Published Date : {article.publish_date}')
print(f'Summary : {article.summary}')

analysis = TextBlob(article.text)
print(analysis.polarity)

print(f'Sentiment  : {"Positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

