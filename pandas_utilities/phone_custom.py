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
        return None, None, None, None  # Return None for all fields if empty
    
    parser = CustomRegex(text)
    dates = parser.dates
    emails = parser.emails
    addresses = parser.street_addresses
    all_phones = parser.get_all_phones()
    return dates, emails, addresses, all_phones