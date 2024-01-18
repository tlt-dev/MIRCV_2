import string
import re
import time
from alive_progress import alive_bar

from nltk import PorterStemmer
from num2words import num2words
from inverted_index.DocumentTable import build_document_table

def remove_malformed_characters(line):
    """ Remove all non utf-8 characters """
    cleaned_line = ' '.join(re.sub(r'[^\x20-\x7E]', ' ', line).split())
    return cleaned_line.encode("utf-8", 'ignore').decode('utf-8')


def check_document_format(document):
    """ check if line is well-formed (<pid>\t<text>) and not empty"""
    try:
        document = document.split('\t')
    except ValueError:
        return False
    else:
        if document[0].isnumeric() and document[1].strip() not in ['\n', '\r\n', ""]:
            return True
        return False


def split_collection(text_collection):
    return text_collection.split('\n')


def collection_to_dict(text_collection):
    """
    Split collection into dictionnary based on pid of each document if the document is well-formed (<pid>\t<text>-
    """
    collection = {}
    for document in split_collection(text_collection):
        if check_document_format(document):
            pid, text = document.split('\t')
            collection[pid] = text
    return collection


def remove_punctuation(token):
    translator = str.maketrans(' ', ' ', string.punctuation)
    return token.translate(translator)


def token_to_numbers(token):
    return [num2words(number) for number in token]


def normalize_tokens(tokenized_collection, stopwords):
    normalized_collection = {}
    for pid, tokens in tokenized_collection.items():
        if stopwords:
            stemmer = PorterStemmer()
            normalized_tokens = [remove_punctuation(token).strip().lower() for token in tokens]
            normalized_tokens = [stemmer.stem(token) for token in normalized_tokens if token not in stopwords]
        else:
            normalized_tokens = [remove_punctuation(token).strip().lower() for token in tokens]
        for index, token in enumerate(normalized_tokens):
            if token.isdigit():
                new_end_list = token_to_numbers(token) + normalized_tokens[index+1:]
                normalized_tokens[index:] = new_end_list
            normalized_collection[pid] = [token for token in normalized_tokens if token != '' and len(token) >= 2]

    return normalized_collection


def tokenize(collection):
    for pid, text in collection.items():
        cleaned_text = remove_malformed_characters(text)
        collection[pid] = [token for token in cleaned_text.split() if len(token) >= 2]
    return collection


def preprocess(stopwords=None, text_collection=None):
    if text_collection:
        collection = collection_to_dict(text_collection)
        document_table = build_document_table(collection)

        tokens = tokenize(collection)
        normalized_tokens = normalize_tokens(tokens, stopwords)

    return normalized_tokens, document_table





