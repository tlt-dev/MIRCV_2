import time

from queries.Config import Config
from queries.QueryParser import preprocess_query
from queries.Scoring import tfidf, bm25
from queries.Type import conjunctive, disjunctive
from inverted_index.Indexer import Indexer
from inverted_index.DocumentTable import load_document_table

import argparse
import os


def process_query(query, index_fp, lexicon, document_table, config):
    """    Process the query, compute ranking scores and return relevant documents ordered by relevance.    """

    query_terms = preprocess_query(query)

    if config.query_type == 'AND':
        relevant_docs = conjunctive(query_terms, index_fp, lexicon)
    else:
        relevant_docs = disjunctive(query_terms, index_fp, lexicon)

    scores = {}
    nb_docs = len(document_table)
    sum_doc_lengths = 0
    sum_doc_lengths += sum(document['doc_length'] for document in document_table.values())
    if config.ranking == 'bm25':
        avgdl = sum_doc_lengths / nb_docs

    for doc_id in relevant_docs:
        scores[doc_id] = 0
        for term in query_terms:
            if term in lexicon:
                index_fp.seek(lexicon[term]['offset'])
                if config.ranking == 'tfidf':
                    score = tfidf(index_fp, doc_id, lexicon[term]['posting_length'], nb_docs)
                else:
                    score = bm25(index_fp, document_table, doc_id, lexicon[term]['posting_length'], nb_docs, avgdl=avgdl)
                scores[doc_id] += score

    sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_docs[:10] if len(sorted_docs) > 10 else sorted_docs


def run():
    parser = argparse.ArgumentParser(description="MIRCV project query tool")
    parser.add_argument("--scoring_function", choices=['bm25', 'tfidf'])
    parser.add_argument("--query_type", choices=['AND', 'OR'])
    parser.add_argument('--test', action='store_true')

    args = parser.parse_args()
    config = Config()

    config.test = args.test
    base_dir = "data/" if config.test is False else "data/tests_binary/"

    if os.path.exists(base_dir + 'compressed_inverted_index.bin'):
        config.use_compression = True
        index_path = base_dir + 'compressed_inverted_index.bin'
        read_mode = 'rb'
    elif os.path.exists(base_dir + 'inverted_index.txt'):
        config.use_compression = False
        index_path = base_dir + 'inverted_index.txt'
        read_mode = 'r'
    else:
        raise Exception("Inverted index not found. Please run the indexing tool before running this script.")

    config.ranking = args.scoring_function if args.scoring_function else "bm25"
    config.query_type = args.query_type if args.query_type else "OR"

    indexer = Indexer()
    indexer.load_lexicon(base_dir + 'lexicon.txt')
    lexicon = indexer.lexicon
    document_table = load_document_table(base_dir + "document_table.txt")

    # avoid to load the full index by just getting the file pointer on the index
    index_fp = open(index_path, read_mode)
    total_time = 0
    query_count = 0
    while True:
        query = input("Query : ")
        query_count += 1
        start = time.time()
        docs = process_query(query, index_fp, lexicon, document_table, config)
        end = time.time()
        print("=== RESULTS ({}) in {}s ===".format(len(docs), end-start))
        if len(docs) > 0:
            for doc in docs:
                print("Document n°{}".format(doc[0]))
        else:
            print("No documents found from the above query")

        total_time += end-start
        print("Time elapsed {} queries: ".format(query_count), total_time)
        print("Average time by query: ", total_time / query_count)


if __name__ == "__main__":
    run()