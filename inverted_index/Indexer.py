from compression.compression import variable_byte_encode, variable_byte_decode
from alive_progress import alive_bar



class Indexer:
    def __init__(self):
        self.inverted_index = {}
        self.lexicon = {}

    def posting_to_string(self, docid, frequency):
        return "{}:{} ".format(docid, frequency)

    def read_postings(self, postings):
        posting_list = {}
        splitted_postings = postings.split()
        for posting in splitted_postings:
            for docid, frequency in posting.split(':'):
                posting_list[docid] = frequency
        return posting_list

    def build_index(self, preprocessed_collection):
        for docid, doc in preprocessed_collection.items():
            for term in doc:
                if term not in self.inverted_index.keys():
                    self.inverted_index[term] = {}

                if docid not in self.inverted_index[term].keys():
                    frequency = doc.count(term)
                    self.inverted_index[term][docid] = frequency

    def build_lexicon(self, term, postings, offset):
        self.lexicon[term] = {}
        self.lexicon[term]["offset"] = offset
        self.lexicon[term]["posting_length"] = len(postings.encode('utf-8'))

        document_frequency = 0
        for posting in postings.split():
            print(len(postings.split()))
            document_frequency += 1
            # for frequency in posting.split(':')[1]:
            #     document_frequency += int(frequency)
        self.lexicon[term]["document_frequency"] = document_frequency

    def write_lexicon(self, filepath):
        self.lexicon = dict(sorted(self.lexicon.items()))
        with open(filepath, "w") as f:
            for term in self.lexicon.keys():
                res = "{}:{}:{}:{} ".format(term, str(self.lexicon[term]["document_frequency"]),
                                            str(self.lexicon[term]["offset"]), str(self.lexicon[term]["posting_length"]))
                f.write(res)
        f.close()

    def write_index(self, index_file_path, final_index=False):
        with open(index_file_path, 'w') as f:
            for term in self.inverted_index:
                res = ''.join(
                    self.posting_to_string(docid, frequency) for docid, frequency in self.inverted_index[term].items())
                if final_index:
                    self.build_lexicon(term, res, f.tell())
                f.write(res)
        f.close()

    def merge_index(self, index_to_merge):
        if len(self.inverted_index) == 0:
            self.inverted_index = index_to_merge.inverted_index
        else:
            for term, postings in index_to_merge.inverted_index.items():
                if term in self.inverted_index.keys():
                    self.inverted_index[term].update(postings)
                else:
                    self.inverted_index[term] = postings
        self.inverted_index = dict(sorted(self.inverted_index.items()))


    def load_inverted_index(self, filepath):
        """ Load the full inverted index"""
        base_dir = filepath.split('/')[0]
        with open(filepath, "r") as f:
            if len(self.lexicon) == 0:
                self.load_lexicon(base_dir + "/lexicon.txt")
            for term in self.lexicon.keys():
                f.seek(self.lexicon[term]["offset"])
                self.inverted_index[term] = self.read_postings(f.read(self.lexicon[term]["posting_length"]))

    def get_posting_list(self, term, filepath=None, offset=None, posting_length=None):
        if self.inverted_index is not None:
            return self.inverted_index[term]
        else:
            with open(filepath, "r") as f:
                f.seek(offset)
                return self.read_postings(f.read(posting_length))

    def load_lexicon(self, filepath):
        with open(filepath, "r") as f:
            lexicon = f.read()
            with alive_bar(len(lexicon.split()), title="Loading Lexicon") as bar:
                for lexic in lexicon.split():
                    term, document_frequency, offset, posting_length = lexic.split(':')
                    self.lexicon[term] = {}
                    self.lexicon[term]["document_frequency"] = document_frequency
                    self.lexicon[term]["offset"] = int(offset)
                    self.lexicon[term]["posting_length"] = int(posting_length)
                    bar()


    def write_compressed_index(self, index_file_path="data/compressed_index.bin"):
        with open(index_file_path, "wb") as f:
            for term, posting_list in self.inverted_index.items():
                offset = f.tell()
                posting_length = 0
                last_doc = 0
                document_frequency = 0
                for doc_id, frequency in posting_list.items():
                    document_frequency += 1
                    gap = int(doc_id) - last_doc
                    for doc_id_byte in variable_byte_encode(gap):
                        posting_length += len(bytes([doc_id_byte]))
                        f.write(bytes([doc_id_byte]))
                    for freq_id_byte in variable_byte_encode(frequency):
                        posting_length += len(bytes([freq_id_byte]))
                        f.write(bytes([freq_id_byte]))
                    last_doc = int(doc_id)

                if term not in self.lexicon.keys():
                    self.lexicon[term] = {}
                self.lexicon[term]['offset'] = offset
                self.lexicon[term]['posting_length'] = posting_length
                self.lexicon[term]['document_frequency'] = document_frequency
        f.close()

def get_posting(index_fp, posting_length):
    postings_bytes = index_fp.read(posting_length)

    decoded_postings = variable_byte_decode(postings_bytes)
    postings_dict = {}
    last_doc_id = 0
    for i in range(0, len(decoded_postings), 2):
        postings_dict[str(last_doc_id + decoded_postings[i])] = decoded_postings[i + 1]
        last_doc_id += decoded_postings[i]
    return postings_dict




