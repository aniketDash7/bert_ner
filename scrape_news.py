import feedparser 

def scrape_google_news(query='technology',max_articles=10):
    feed_url = f"https://news.google.com/rss/search?q={query}"
    feed = feedparser.parse(feed_url)
    articles = []


    for entry in feed.entries[:max_articles]:
        title = entry.title 
        summary = entry.get("summary","")
        articles.append(f"{title}.{summary}")
    return articles

def save_articles(articles,path='news_articles.txt'):
    with open(path,"w",encoding='utf-8') as f:
        for article in articles:
            f.write(article.strip() + "\n")


if __name__ == "__main__":
    keywords = ["Apple", "Microsoft", "OpenAI", "Nvidia"]
    all_articles = []

    for keyword in keywords:
        print(f"Scraping news for: {keyword}")
        articles = scrape_google_news(query=keyword, max_articles=5)
        all_articles.extend(articles)

    save_articles(all_articles)
    print(f"✅ Saved {len(all_articles)} articles to news_articles.txt")