import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os
import ssl


def set_stopwords():
    try:
        os.path.exists('/Users/thomaslaurent/nltk_data/stopwords')
    except:
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        else:
            ssl._create_default_https_context = _create_unverified_https_context
        nltk.download('stopwords')
    return set(stopwords.words('english'))


def set_collection_path(collection_path):
    if collection_path is not None and os.path.exists(collection_path):
        return collection_path
    else:
        return "data/collection.tsv"


class Config:
    def __init__(self, collection_path=None, stopwords=None, stemming=None, compression=False, test=False, binary=False):
        self.test = test
        self.binary = binary
        self.base_dir = "data/" if self.test is False else "data/tests_binary/" if self.binary else "data/tests/"
        self.collection_path = set_collection_path(collection_path) if self.test is False else self.base_dir + "test.tsv"
        self.lexicon_path = "data/lexicon.txt" if self.test is False else self.base_dir + "lexicon.txt"
        self.document_table_path = "data/document_table.txt" if self.test is False else self.base_dir + "document_table.txt"
        self.stopwords = set_stopwords() if stopwords is not None else None
        self.stemmer = PorterStemmer() if stemming is not None else None
        self.compression = compression

