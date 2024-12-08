import string
import re

def remove_punctiation_from_tokens(tokens):
    return [token for token in tokens if token not in string.punctuation]

def remove_paranthesis_from_tokens(tokens):
    return [token for token in tokens if token not in ['(', ')', '{', '}', '[', ']']]

def remove_empty_tokens(tokens):
    return [token for token in tokens if token != '']

def lower_case_tokens(tokens):
    return [token.lower() for token in tokens]

def remove_numbers_from_tokens(tokens):
    return [token for token in tokens if not token.isdigit()]

def remove_non_alphanumeric(tokens):
    return [re.sub(r'\W+', '', token) for token in tokens if re.sub(r'\W+', '', token) != '']

def strip_whitespace(tokens):
    return [token.strip() for token in tokens]

def clean_tokens(tokens):
    tokens = remove_non_alphanumeric(tokens)
    tokens = lower_case_tokens(tokens)
    tokens = remove_punctiation_from_tokens(tokens)
    tokens = remove_paranthesis_from_tokens(tokens)
    tokens = remove_empty_tokens(tokens)
    tokens = remove_numbers_from_tokens(tokens)
    tokens = strip_whitespace(tokens)
    return tokens