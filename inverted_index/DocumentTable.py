from alive_progress import alive_bar


def build_document_table(collection):
    document_table = {}
    for docid, text in collection.items():
        document_table[docid] = {"docno": "doc_" + str(docid), "doc_length": len(text.split())}
    return document_table


def merge_document_tables(final_document_table, temp_document_table):
    for doc_id, doc_info in temp_document_table.items():
        final_document_table[doc_id] = doc_info

    return final_document_table


def write_document_table(document_table, filepath):
    document_table = dict(sorted(document_table.items()))
    with open(filepath, "w") as f:
        for docid, doc_info in document_table.items():
            res = "{}:{}:{} ".format(docid, doc_info["docno"], doc_info["doc_length"])
            f.write(res)
    f.close()


def load_document_table(filepath):
    document_table = {}
    with open(filepath, "r") as f:
        content = f.read()
        docs = content.split()
        with alive_bar(len(docs), title="Loading Document Table") as bar:
            for doc in docs:
                docid, docno, doc_length = doc.split(':')
                document_table[docid] = {"docno": docno, "doc_length": int(doc_length)}
                bar()
    f.close()

    return document_table
