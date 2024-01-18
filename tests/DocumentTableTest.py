import shutil

from inverted_index.DocumentTable import *
from tests.test_data import DocumentTableTestData as test_data, DocumentTableExpectedData as expected_data

import unittest
import os


class DocumentTableTest(unittest.TestCase):
    def test_build_document_table(self):
        return self.assertEqual(expected_data.DOCUMENT_TABLE_1.value,
                                build_document_table(test_data.DICT_COLLECTION.value))

    def test_merge_document_tables(self):
        return self.assertEqual(expected_data.MERGED_DOCUMENT_TABLE.value,
                                merge_document_tables(test_data.DOCUMENT_TABLE_2.value, test_data.DOCUMENT_TABLE_1.value))

    def test_write_document_table(self):
        write_document_table(test_data.MERGED_DOCUMENT_TABLE.value, "test_dir/document_table.txt")

        with open("test_dir/document_table.txt", "r") as f:
            document_table = f.read()
        f.close()

        return self.assertEqual(expected_data.DOCUMENT_TABLE_FILE_CONTENT.value, document_table.strip())

    def test_load_document_table(self):
        return self.assertEqual(expected_data.LOADED_DOCUMENT_TABLE.value, load_document_table("test_dir/document_table_to_load.txt"))