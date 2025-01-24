import pandas as pd
import nltk
import sklearn
nltk.download('vader_lexicon')

# Import SentimentIntensityAnalyzer and create an sid object
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

def nltksentiment(comment: str ) -> dict:
    print(comment)
    if (isinstance(comment, str)):
        x = sid.polarity_scores(comment)
    else:
        x = None
    return x

# Use type-annotated function signature or function type hinting
from typing import Dict, Any
def get_nltk_sentiment(comment: str) -> Dict[str, Any]:
    sentiment_scores = sid.polarity_scores(comment)
    compound = sentiment_scores['compound']
    neg = sentiment_scores['neg']
    neu = sentiment_scores['neu']
    pos = sentiment_scores['pos']

    # Determine sentiment status
    if compound >= 0.05:
        sentiment = 'Positive'
    elif compound <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return {
        'sentiment': sentiment,
        'compound_score': compound,
        'negative_score': neg,
        'neutral_score': neu,
        'positive_score': pos
    }

def get_nltk_sentiment_label(comment: str) -> str:
    sentiment_scores = sid.polarity_scores(comment)
    compound = sentiment_scores['compound']
    neg = sentiment_scores['neg']
    neu = sentiment_scores['neu']
    pos = sentiment_scores['pos']

    # Determine sentiment status
    if compound >= 0.05:
        sentiment = 'Positive'
    elif compound <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment
