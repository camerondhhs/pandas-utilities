import pandas as pd
from flashtext2 import KeywordProcessor
kp = KeywordProcessor(case_sensitive=False)

def format_list(lst: list) -> str:
    """Format a list into a comma-separated string."""
    return ', '.join(map(str, lst)) if lst else ''

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

      for name in names_list:
        kp.add_keyword(name)
      # Add all keywords at once for better performance
      # kp.add_keywords_from_list(names_list)

      extracted_names = kp.extract_keywords(text)
      # extracted_list_fn = format_list(extracted_keywords_fn)
      return format_list(extracted_names)

    except FileNotFoundError:
        return "Error: The specified file was not found."
    except pd.errors.EmptyDataError:
        return "Error: The CSV file is empty."
    except Exception as e:
        return f"Error: {str(e)}"