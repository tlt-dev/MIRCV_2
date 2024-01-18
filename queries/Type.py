from compression.compression import variable_byte_decode
from inverted_index.Indexer import get_posting
def conjunctive(query, index_fp, lexicon):
    postings_list = []
    for term in query:
        if term in lexicon.keys():
            offset = lexicon[term]["offset"]
            posting_length = lexicon[term]["posting_length"]
            print("offset : " + str(offset))
            index_fp.seek(offset)
            postings_list.append(get_posting(index_fp, posting_length))

    print(len(postings_list))

    if not postings_list:
        return []

    common_documents = set.intersection(*map(set, postings_list))

    return list(common_documents)


def disjunctive(preprocessed_query, index_fp, lexicon):
    all_documents = set()

    for term in preprocessed_query:
        if term in lexicon:
            index_fp.seek(lexicon[term]["offset"])
            all_documents.update(get_posting(index_fp, lexicon[term]['posting_length']))

    return list(all_documents)