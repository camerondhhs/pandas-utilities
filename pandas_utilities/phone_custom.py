import re
from commonregex import CommonRegex

class CustomRegex(CommonRegex):
    def __init__(self, text=''):
        super().__init__(text)
        
        # Custom regex for Australian phone numbers with different formats
        self.ausphone_pattern = re.compile(
            r'\b(?:\+61[-\s]?\d{4}[-\s]?\d{3}[-\s]?\d{3}|'  # +61 international with separators
            r'0\d{3}[-\s]?\d{3}[-\s]?\d{3})\b'              # Australian standard with separators
        )
        self.ausphones = self.ausphone_pattern.findall(text)

    def get_all_phones(self):
        # Combine and remove duplicates from default phone extraction and custom ausphones
        all_phones = set(self.phones + self.ausphones)
        return sorted(all_phones)
    
# Function to extract dates, emails, addresses, and phones using CommonRegex
def extract_common_regex_info(text):
    if not text or not isinstance(text, str) or text.strip() == "":
        return "", "", "", ""  # Return empty strings for all fields if the input is empty
    
    parser = CustomRegex(text)
    
    # Ensure empty strings instead of empty lists
    dates = ", ".join(parser.dates) if parser.dates else ""
    emails = ", ".join(parser.emails) if parser.emails else ""
    addresses = ", ".join(parser.street_addresses) if parser.street_addresses else ""
    all_phones = ", ".join(parser.get_all_phones()) if parser.get_all_phones() else ""

    return dates, emails, addresses, all_phones
