import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
# from torch.nn.functional import softmax
from scipy.special import softmax
import pandas as pd
import numpy as np
from tqdm import tqdm

def load_model_tokenizer_and_config(model_name):
    """
    Load the pre-trained model and tokenizer based on the provided model name.
    """
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.model_max_length = 512
    config = AutoConfig.from_pretrained(model_name)
    # print('tokenizer')
    # print(tokenizer)
    # print('config')
    # print(config)
    return model, tokenizer, config

def preprocess(text):
  new_text = []
  for t in text.split(" "):
    t = '@user' if t.startswith('@') and len(t) > 1 else t
    t = 'http' if t.startswith('http') else t
    new_text.append(t)
  return " ".join(new_text)

def st_analyze_sentiment(model_name, sentence):
    """
    Perform sentiment analysis on the given sentence using the specified model.
    """
    model, tokenizer, config = load_model_tokenizer_and_config(model_name)
    encoded_input = tokenizer(sentence, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    predictions = softmax(scores)
    return predictions

def st_label_sentiment(config, predictions):
    """
    Convert sentiment predictions to human-readable labels and return with confidence score.
    """
    # max_index = predictions.index(max(predictions))
    ranking = np.argsort(predictions)
    ranking = ranking[::1]
    for i in range(predictions.shape[0]):
      l = config.id2label[ranking[i]]
      s = predictions[ranking[i]]
      sf = np.round(float(s), 4)
    return l, sf

def st_process_comments(df, model_name):
    """
    Apply sentiment analysis and labeling to a DataFrame containing a 'comments' column.
    """
    # Load model and tokenizer once for efficiency
    model, tokenizer, config = load_model_tokenizer_and_config(model_name)

    def st_analyze_and_label(comment):
      if pd.isna(comment) or not isinstance(comment, str):
          return "", 0.0  # Handle missing or non-string values
      comment = preprocess(comment)
      predictions = st_analyze_sentiment(model_name, comment)
      sentiment_label, confidence_score = st_label_sentiment(config, predictions)
      return sentiment_label, confidence_score

    tqdm.pandas(desc="Processing Comments")
    df[['sentiment', 'confidence']] = df.progress_apply(
      lambda row: pd.Series(st_analyze_and_label(row['Comments'])), axis=1
    )
    return df
