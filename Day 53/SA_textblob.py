from textblob import TextBlob

texts=[
    "I love NLP. ",
    "This is my first experience on doing sentiment analysis and i feel stressed",
    "This NLP is quiet interesting"
]

#create function to do the sentiment analysis
def analyze_sentiment(text):
    analysis=TextBlob(text)
    #-1.0 - 1.0 polarity score
    polarity=analysis.sentiment.polarity
    if polarity>0:
        sentiment='Positive'
    elif polarity<0:
        sentiment="Negative"
    else:
        sentiment="Neutral"
    return sentiment
for text in texts:
    sentiment=analyze_sentiment(text)
    print(f"text:{text}")
    print(f"sentiment:{sentiment}")