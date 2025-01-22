import pandas as pd
from flashtext2 import KeywordProcessor

def format_list(lst: list) -> str:
    """Format a list into a comma-separated string with unique entries."""
    return ', '.join(map(str, sorted(set(lst)))) if lst else ''

def format_list_all(lst: list) -> str:
    """Format a list into a comma-separated string."""
    return ', '.join(map(str, lst)) if lst else ''

def load_names_from_csv( file_path: str) -> KeywordProcessor:
    """
    Load names from a CSV file and initialize a KeywordProcessor.

    Args:
        text (str): The input text to search for names        file_path (str): Path to the CSV file containing names.

    Returns:
        KeywordProcessor: Initialized processor with keywords loaded.
    """
    
    try:
      df = pd.read_csv(file_path, header=None, names=['name'], usecols=[0])  # Read without header and assign a column name
      names_list = df['name'].dropna().tolist()

      kp = KeywordProcessor(case_sensitive=False)
      for name in names_list:
        kp.add_keyword(name)

      return kp

    except FileNotFoundError:
        return "Error: The specified file was not found."
    except pd.errors.EmptyDataError:
        return "Error: The CSV file is empty."
    except Exception as e:
        return f"Error: {str(e)}"

def extract_names_from_text(text: str, keyword_processor: KeywordProcessor) -> str:
    """
    Extract names from a given text using the provided KeywordProcessor.
    
    Args:
        text (str): The input text to search for keywords.
        keyword_processor (KeywordProcessor): Preloaded KeywordProcessor instance.
        
    Returns:
        str: A comma-separated string of extracted names.
    """
    extracted_names = keyword_processor.extract_keywords(text)
    return format_list(extracted_names)

def extract_names_from_csv(text: str, file_path: str) -> str:
    """
    Extract names from a given text using names provided in a CSV file.

    Args:
        text (str): The input text to search for names.
        file_path (str): Path to the CSV file containing names.

    Returns:
        str: A comma-separated string of extracted names.
    """
    
    try:
      df = pd.read_csv(file_path, header=None, names=['name'], usecols=[0])  # Read without header and assign a column name
      names_list = df['name'].dropna().tolist()

      kp = KeywordProcessor(case_sensitive=False)
      for name in names_list:
        kp.add_keyword(name)
      extracted_names = kp.extract_keywords(text)

      return format_list(extracted_names)

    except FileNotFoundError:
        return "Error: The specified file was not found."
    except pd.errors.EmptyDataError:
        return "Error: The CSV file is empty."
    except Exception as e:
        return f"Error: {str(e)}"