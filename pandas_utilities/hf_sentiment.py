import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from torch.nn.functional import softmax
import pandas as pd

def load_model_and_tokenizer(model_name):
    """
    Load the pre-trained model and tokenizer based on the provided model name.
    """
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

def analyze_sentiment(model_name, sentence):
    """
    Perform sentiment analysis on the given sentence using the specified model.
    """
    model, tokenizer = load_model_and_tokenizer(model_name)
    tokens = tokenizer(sentence, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**tokens)
    predictions = softmax(outputs.logits, dim=-1)
    return predictions[0].tolist()

def label_sentiment(predictions):
    """
    Convert sentiment predictions to human-readable labels and return with confidence score.
    """
    labels = ["Negative", "Positive"]
    max_index = predictions.index(max(predictions))
    return labels[max_index], predictions[max_index]

def process_comments(df, model_name):
    """
    Apply sentiment analysis and labeling to a DataFrame containing a 'comments' column.
    """
    # Load model and tokenizer once for efficiency
    model, tokenizer = load_model_and_tokenizer(model_name)

    # Function to analyze a single comment
    def analyze_and_label(comment):
        if pd.isna(comment) or not isinstance(comment, str):
            return "Neutral", 0.0  # Handle missing or non-string values
        predictions = analyze_sentiment(model_name, comment)
        sentiment_label, confidence_score = label_sentiment(predictions)
        return sentiment_label, confidence_score

    # Apply sentiment analysis to each comment in the DataFrame
    df[['sentiment', 'confidence']] = df['comments'].apply(lambda x: pd.Series(analyze_and_label(x)))
    return df