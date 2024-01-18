import unittest
from document_processing.Config import Config
from document_processing.DocumentParser import *
from tests.test_data import DocumentParserTestData as test_data
from tests.test_data import DocumentParserExpectedData as expected_data


class DocumentParserTest(unittest.TestCase):
    def setUp(self) -> None:
        self.config = Config(None, True, True)
        self.maxDiff = None

    def test_remove_one_malformed_character(self):
        return self.assertEqual(expected_data.ONE_MALFORMED_CHARACTER.value,
                                remove_malformed_characters(test_data.ONE_MALFORMED_CHARACTER.value))

    def test_remove_multiple_malformed_characters(self):
        return self.assertEqual(expected_data.MULTIPLE_MALFORMED_CHARACTERS.value,
                                remove_malformed_characters(test_data.MULTIPLE_MALFORMED_CHARACTERS.value))

    def test_remove_no_malformed_characters(self):
        return self.assertEqual(expected_data.NO_MALFORMED_CHARACTERS.value,
                                remove_malformed_characters(test_data.NO_MALFORMED_CHARACTERS.value))

    def test_check_document_format_without_tab(self):
        return self.assertFalse(expected_data.DOCUMENT_WITHOUT_TAB.value,
                                check_document_format(test_data.DOCUMENT_WITHOUT_TAB.value))

    def test_check_document_format_without_pid(self):
        return self.assertFalse(expected_data.DOCUMENT_WITHOUT_PID.value,
                                check_document_format(test_data.DOCUMENT_WITHOUT_PID.value))

    def test_check_document_format_with_non_numeric_pid(self):
        return self.assertFalse(expected_data.DOCUMENT_WITH_NON_NUMERIC_PID.value,
                                check_document_format(test_data.DOCUMENT_WITH_NON_NUMERIC_PID.value))

    def test_check_document_format_without_text(self):
        return self.assertFalse(expected_data.DOCUMENT_WIHOUT_TEXT.value,
                                check_document_format(test_data.DOCUMENT_WIHOUT_TEXT.value))

    def test_check_document_format_empty_text_with_line_feed(self):
        return self.assertFalse(expected_data.DOCUMENT_WITH_SPACES_AND_LINE_FEED.value,
                                check_document_format(test_data.DOCUMENT_WITH_SPACES_AND_LINE_FEED.value))

    def test_check_document_format_well_formed(self):
        return self.assertTrue(expected_data.WELL_FORMED_DOCUMENT.value,
                               check_document_format(test_data.WELL_FORMED_DOCUMENT.value))

    def test_collection_to_dict(self):
        return self.assertTrue(expected_data.DICT_COLLECTION.value,
                               collection_to_dict(test_data.TEXT_COLLECTION.value))

    def test_remove_punctuation_with_token(self):
        return self.assertEqual(expected_data.PUNCTUATED_TOKEN.value,
                                remove_punctuation(test_data.PUNCTUATED_TOKEN.value))

    def test_remove_punctuation_without_token(self):
        return self.assertEqual(expected_data.PUNCTUATION.value,
                                remove_punctuation(test_data.PUNCTUATION.value))

    def test_normalize_tokens(self):
        return self.assertEqual(expected_data.NORMALIZED_TOKENS.value,
                                normalize_tokens(test_data.NON_NORMALIZED_TOKENS.value, stopwords=None))

    def test_tokenize(self):
        return self.assertEqual(expected_data.SENTENCE_TOKENIZED.value,
                                tokenize(test_data.SENTENCE_TO_TOKENIZE.value))

    def test_preprocess(self):
        return self.assertEqual(expected_data.TEXT_PREPROCESSED.value,
                                preprocess(text_collection=test_data.TEXT_TO_PREPROCESS.value)[0])


if __name__ == "__main__":
    unittest.main()
