from transformers import AutoTokenizer,AutoModelForTokenClassification
from transformers import pipeline 
from textblob import TextBlob
import nltk 

nltk.download('punkt',quiet=True)

import re 

def load_ner_pipeline(model_path = 'aniketDS/ner-bert-model'):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForTokenClassification.from_pretrained(model_path)
    return pipeline("ner",
                    model=model,
                    tokenizer=tokenizer,
                    aggregation_strategy='simple')

def load_watchlist(path='company_watchlist.txt'):
    with open(path,'r') as f:
        return [line.strip() for line in f.readlines()]

def extract_entities(tgitext,ner_pipeline):
    entities = ner_pipeline(text)
    return list(set([ent['word'] for ent in entities]))

def match_watchlist(entities,watchlist):
    return [company for company in watchlist if company in entities]


def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    sentiment = (
        "positive" if polarity > 0.1
        else "negative" if polarity < -0.1
        else "neutral"
    )
    return sentiment,round(polarity,3)


