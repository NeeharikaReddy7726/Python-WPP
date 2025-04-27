import re

def hindi_tokenizer(text):
    # Regular expressions for different patterns
    patterns = {
        'punctuations': r'[।,;!?."\'“”‘’(){}[\]:-]',  # Match Hindi punctuations and general ones
        'dates': r'\b\d{1,2}/\d{1,2}/\d{2,4}\b',  # Match dates like DD/MM/YYYY
        'urls': r'\b(?:http|https)://[a-zA-Z0-9./?=_-]+\b',  # Match URLs
        'emails': r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b',  # Match emails
        'numbers': r'\b\d{1,3}(?:,\d{2,3})*(?:\.\d+)?\b',  # Match numbers like "33.15", "3,22,243"
        'user_handles': r'@[a-zA-Z0-9_]+',  # Match social media usernames/user handles
        'hindi_words': r'[\u0900-\u097F]+',  # Match Hindi words using Unicode block for Devanagari script
    }
    
    tokens = []
    for label, pattern in patterns.items():
        matches = re.findall(pattern, text)
        tokens.extend(matches)
        text = re.sub(pattern, '', text)  # Remove matched patterns to avoid overlapping matches
    
    # Remaining non-Hindi or leftover text tokens
    remaining_words = text.split()
    tokens.extend(remaining_words)
    
    return tokens

# Take input from the user
user_input = input("Enter your text for tokenization: ")

# Tokenize the user input
tokens = hindi_tokenizer(user_input)

# Display the tokens
print("Tokens:")
for token in tokens:
    print(token)
