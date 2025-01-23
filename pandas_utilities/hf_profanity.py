from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
import pandas as pd
from tqdm import tqdm

def detect_profanity(text):
  if pd.isna(text) or text.strip() == "":
    return 0.0, [0,0, 0.0]
  inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
  with torch.no_grad():
    outputs = model(**inputs)
  probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
  predicted_class = torch.argmax(probabilities, dim=1).item()
  return predicted_class, probabilities.tolist()
