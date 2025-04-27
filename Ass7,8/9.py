import re

def hindi_tokenizer(text):
    # Define regular expressions for different token types
    punctuation_pattern = r'[।,!?;:\'\"(){}[\]<>।-]'  # Punctuation
    date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'  # Dates (e.g., 31/12/2021)
    url_pattern = r'https?://(?:www\.)?\w+\.\w+(?:\.\w+)*(?:/\S*)?'  # URLs
    email_pattern = r'\b\w+@\w+\.\w+(?:\.\w+)?\b'  # Emails
    number_pattern = r'\b\d+[\.,/]\d*\b|\b\d{1,3}(?:,\d{2,3})*\b'  # Numbers (e.g., 33.15, 3,22,243, 313/77)
    user_handle_pattern = r'@\w+'  # Social media usernames/user handles
    hindi_word_pattern = r'\b\p{Script=Devanagari}+\b'  # Hindi words (Unicode block for Devanagari script)

    # Compile all patterns into one
    patterns = f'({punctuation_pattern})|({date_pattern})|({url_pattern})|({email_pattern})|' \
               f'({number_pattern})|({user_handle_pattern})|({hindi_word_pattern})'

    # Find all matches
    tokens = re.findall(patterns, text)

    # Flatten the list of tuples and remove empty strings
    tokens = [token for sublist in tokens for token in sublist if token]

    return tokens

#