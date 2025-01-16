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
        sentiment = 'positive'
    elif compound <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    return {
        'sentiment': sentiment,
        'compound_score': compound,
        'negative_score': neg,
        'neutral_score': neu,
        'positive_score': pos
    }
