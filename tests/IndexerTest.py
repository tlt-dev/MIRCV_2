from inverted_index.Indexer import Indexer
from document_processing.DocumentParser import preprocess
from test_data import IndexerTestData as test_data, IndexerExpectedData as expected_data

import unittest


class IndexerTest(unittest.TestCase):
    def setUp(self):
        self.indexer = Indexer()
        self.maxDiff = None

    def test_posting_to_string(self):
        return self.assertEqual(expected_data.POSTING.value,
                                self.indexer.posting_to_string(test_data.POSTING.value[0], test_data.POSTING.value[1]))

    def test_build_index(self):
        self.indexer.build_index(test_data.TEXT_PREPROCESSED.value)
        return self.assertEqual(expected_data.INVERTED_INDEX.value, self.indexer.inverted_index)

    def test_write_index(self):
        self.indexer.build_index(test_data.TEXT_PREPROCESSED.value)
        self.indexer.write_index("test_dir/inverted_index.txt")
        with open("test_dir/inverted_index.txt", "r") as f:
            inverted_index_content = f.read()
        f.close()

        return self.assertEqual(expected_data.INVERTED_INDEX_FILE_CONTENT.value, inverted_index_content)

    def test_build_lexicon(self):
        self.indexer.build_index(test_data.TEXT_PREPROCESSED.value)
        self.indexer.write_index("test_dir/inverted_index.txt", True)
        return self.assertEqual(expected_data.LEXICON_DICT.value, self.indexer.lexicon)

    def test_write_lexicon(self):
        self.indexer.build_index(test_data.TEXT_PREPROCESSED.value)
        self.indexer.write_index("test_dir/inverted_index.txt", True)
        self.indexer.write_lexicon("test_dir/lexicon.txt")

        with open("test_dir/lexicon.txt", "r") as f:
            lexicon_content = f.read()
        return self.assertEqual(expected_data.LEXICON_FILE_CONTENT.value, lexicon_content)

    def test_merge_index(self):
        index_to_merge = Indexer()
        self.indexer.inverted_index = test_data.INVERTED_INDEX_TO_MERGE_1.value
        index_to_merge.inverted_index = test_data.INVERTED_INDEX_TO_MERGE_2.value

        self.indexer.merge_index(index_to_merge)
        return self.assertEqual(expected_data.MERGED_INVERTED_INDEX.value, self.indexer.inverted_index)


    def test_load_index(self):
        pass

    def test_load_lexicon(self):
        pass
