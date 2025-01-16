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

