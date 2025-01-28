import spacy

nlp = spacy.load('en_core_web_sm')

def get_entity(text: str) -> str:
  """
  Args:
    text (str): The input text to find entities
  Returns:
    str: A comma-separated string of entities.
  """
  ent_list = []
  if (isinstance(text, str)):
    doc = nlp(text)
    for entity in doc.ents:
      ent_list.append(entity.text + ' (' + entity.label_ + ')')
    listtostring = ', '.join(ent_list)
  else:
    listtostring = ''
  return listtostring
