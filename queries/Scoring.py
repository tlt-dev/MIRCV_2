import math
from inverted_index.Indexer import get_posting

def tfidf(index_fp, doc_id, posting_length, total_docs):
    posting_dict = get_posting(index_fp, posting_length)
    #TF
    tf = posting_dict[doc_id] if doc_id in posting_dict else 0

    # IDF
    doc_freq = len(posting_dict)
    idf = math.log(total_docs / doc_freq)
    return tf * idf


def bm25(index_fp, document_table, doc_id, posting_length, total_docs, avgdl, k1=1.5, b=0.75):
    #  IDF
    posting_dict = get_posting(index_fp, posting_length)
    doc_freq = len(posting_dict)
    idf = math.log((total_docs - doc_freq + 0.5) / (doc_freq + 0.5) + 1)

    # Term frequency
    tf = posting_dict[doc_id] if doc_id in posting_dict else 0

    doc_length = document_table[doc_id]['doc_length']

    # BM25
    score = idf * ((tf * (k1 + 1)) / (tf + k1 * (1 - b + b * (doc_length / avgdl))))

    return score
