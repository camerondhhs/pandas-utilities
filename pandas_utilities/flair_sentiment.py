from flair.data import Sentence
from flair.nn import Classifier
tagger = Classifier.load('sentiment')
def get_flair_sentiment_label(comment: str) -> str:
  if not comment or pd.isna(comment) or comment.strip() == "":
    return "Neutral"  # Default label for empty/missing comments
  sentence = Sentence(comment)
  tagger.predict(sentence)
  sentiment_label = sentence.get_labels()[0].value  # Get sentiment label
  # Convert flair labels to standardize format
  if sentiment_label == 'POSITIVE':
      return 'Positive'
  elif sentiment_label == 'NEGATIVE':
      return 'Negative'
  else:
      return 'Neutral'