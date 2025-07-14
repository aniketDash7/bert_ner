import streamlit as st
from utils import load_ner_pipeline, load_watchlist, extract_entities, match_watchlist,analyze_sentiment

# Load models and data
st.title("📰 News & Media Monitoring (NER)")
ner_pipeline = load_ner_pipeline()
watchlist = load_watchlist()

# Load news articles
with open("news_articles.txt", "r") as f:
    articles = f.readlines()

results = []
for text in articles:
    text = text.strip()
    entities = extract_entities(text, ner_pipeline)
    matched = match_watchlist(entities, watchlist)
    if matched:
        sentiment,polarity = analyze_sentiment(text)
        results.append({
            "Article": text,
            "Matched Companies": ", ".join(matched),
            "Extracted Entities": ", ".join(entities),
            "Sentiment" : sentiment,
            "Polarity": polarity
        })

# Display
st.subheader("🧠 Matched News Alerts")
st.dataframe(results)