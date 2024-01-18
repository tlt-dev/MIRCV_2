import string
import re

from nltk import PorterStemmer
from num2words import num2words

from document_processing.Config import Config
from inverted_index.DocumentTable import build_document_table


def remove_malformed_characters(line):
    """ Remove all non utf-8 characters """
    cleaned_line = ' '.join(re.sub(r'[^\x20-\x7E]', ' ', line).split())
    return cleaned_line.encode("utf-8", 'ignore').decode('utf-8')


def remove_punctuation(token):
    translator = str.maketrans('', '', string.punctuation)
    return token.translate(translator)


def token_to_numbers(token):
    return [num2words(number) for number in token]


def normalize_tokens(tokens, stopwords):
    final_tokens = []
    if stopwords:
        stemmer = PorterStemmer()
        normalized_tokens = [remove_punctuation(token).strip().lower() for token in tokens]
        normalized_tokens = [stemmer.stem(token) for token in normalized_tokens if token not in stopwords]
    else:
        normalized_tokens = [remove_punctuation(token).strip().lower() for token in tokens]
    for token in normalized_tokens:
        if token.isdigit():
            token = token_to_numbers(token)
        if tokens != '' and len(token) >= 2:
            final_tokens.append(token)

    return final_tokens


def tokenize(query):
    cleaned_query = remove_malformed_characters(query)
    tokens = [token for token in cleaned_query.split() if len(token) >= 2]
    return tokens


def preprocess_query(query):
    config = Config(stopwords=True)
    tokens = tokenize(query)
    normalized_tokens = normalize_tokens(tokens, stopwords=config.stopwords)
    print(normalized_tokens)
    return normalized_tokens




