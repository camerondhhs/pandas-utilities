import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from torch.nn.functional import softmax

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
    Convert sentiment predictions to human-readable labels.
    """
    labels = ["Negative", "Positive"]
    return labels[predictions.index(max(predictions))]