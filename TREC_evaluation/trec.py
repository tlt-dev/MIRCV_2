import math
import time
from statistics import mean

from inverted_index.DocumentTable import load_document_table
from inverted_index.Indexer import Indexer
from queries.Config import Config
from query import process_query

with open('msmarco-test2020-queries.tsv', 'r') as f:
    queries = {}
    for line in f:
        id, query = line.strip().split('\t')
        queries[id] = query
f.close()

with open('2020qrels-docs.txt', 'r') as f:
    expected_results = {}
    for line in f:
        query_id, _, doc_id, relevance = line.strip().split()
        if query_id not in expected_results:
            expected_results[query_id] = {}
        expected_results[query_id][doc_id] = int(relevance)
f.close()

print(len(queries), sorted(queries.keys()))
print(len(expected_results), sorted(expected_results.keys()))

index_fp = open('../data/compressed_inverted_index.bin', 'rb')
indexer = Indexer()
indexer.load_lexicon('../data/lexicon.txt')
lexicon = indexer.lexicon
document_table = load_document_table('../data/document_table.txt')
nb_docs = len(document_table)

ndcg_list = []
for scoring_function in ['bm25', 'tfidf']:
    config = Config(ranking=scoring_function)
    nb_queries = 0
    elapsed_time = 0
    ndcg = []
    for id, query in queries.items():
        if id not in expected_results:
            continue
        k = len(expected_results[id])
        querying_start = time.time()
        results = process_query(query, index_fp, lexicon, document_table, config)
        elapsed_time += time.time() - querying_start
        nb_queries += 1
        results = {docid for docid, _ in results}

        weighted_assessed_run = []
        for docid in results:
            if docid in expected_results[id]:
                weighted_assessed_run.append(expected_results[id][docid])
            else:
                weighted_assessed_run.append(0)

        if len(weighted_assessed_run) == 0:
            ndcg.append(0)
            continue

        # Compute DCG
        dcg = weighted_assessed_run[0]
        count = 1
        for weight in weighted_assessed_run[1:]:
            dcg += weight / math.log2(count + 1)
            count += 1

        # Compute IDCG
        expected_results = list(expected_results[id].values())
        weighted_assessed_ideal_run = sorted(expected_results)[20:]
        idcg = weighted_assessed_ideal_run[0]
        count = 1
        for weight in weighted_assessed_ideal_run[1:]:
            idcg += weight / math.log2(count + 1)
            count += 1

        ndcg.append(dcg / idcg)

    ndcg_list.append(mean(ndcg))
    print("nDCG " + scoring_function + " : ", mean(ndcg))
    print("Time elapsed : ", elapsed_time)
    print("Nb of queries : ", nb_queries)
    print("Average time for each query : ", elapsed_time / nb_queries)


