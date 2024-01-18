from enum import Enum, StrEnum


class DocumentParserTestData(Enum):
    ONE_MALFORMED_CHARACTER = "There's one malformedâ character here."
    MULTIPLE_MALFORMED_CHARACTERS = "This phraseâcontains moreâ than one malformed character."
    NO_MALFORMED_CHARACTERS = "This phrase is perfect !"

    DOCUMENT_WITHOUT_TAB = "0 This document contains no tab"
    DOCUMENT_WITHOUT_PID = "\tThis document contains no pid"
    DOCUMENT_WITH_NON_NUMERIC_PID = "Zero\tThis document contains no numeric pid"
    DOCUMENT_WIHOUT_TEXT = "0\t"
    DOCUMENT_WITH_LINE_FEED = "0\t\n"
    DOCUMENT_WITH_SPACES_AND_LINE_FEED = "0\t    \n    "
    WELL_FORMED_DOCUMENT = "0\tThis document is well formed"

    TEXT_COLLECTION = "0\tThis is the first document\n1\tThis is the second document\n2\tThis is the third document"

    PUNCTUATED_TOKEN = "This,"
    PUNCTUATION = "!"

    NON_NORMALIZED_TOKENS = {"0": ['This,', 'TOKENS', 'are', '(Not)', 'normali_zed!', '...']}

    SENTENCE_TO_TOKENIZE = {
        "0": "This, sentence is_ _ not tokenized !",
        "1": "This one# @ is also:. a sentence not ) tokenized"
    }

    DICT_COLLECTION = {
        "1": "This is the first document",
        "2": "This is the second document",
        "3": "This is the third document"
    }

    TEXT_TO_PREPROCESS = "0	The presence of communication amid scientific minds was equally important to the success of the Manhattan Project as scientific intellect was. The only cloud hanging over the impressive achievement of the atomic researchers and engineers is what their success truly meant; hundreds of thousands of innocent lives obliterated.\n1	The Manhattan Project and its atomic bomb helped bring an end to World War II. Its legacy of peaceful uses of atomic energy continues to have an impact on history and science.\n2	Essay on The Manhattan Project - The Manhattan Project The Manhattan Project was to see if making an atomic bomb possible. The success of this project would forever change the world forever making it known that something this powerful can be manmade.\n3	The Manhattan Project was the name for a project conducted during World War II, to develop the first atomic bomb. It refers specifically to the period of the project from 194 â¦ 2-1946 under the control of the U.S. Army Corps of Engineers, under the administration of General Leslie R. Groves.\n"


class DocumentParserExpectedData(Enum):
    ONE_MALFORMED_CHARACTER = "There's one malformed character here."
    MULTIPLE_MALFORMED_CHARACTERS = "This phrase contains more than one malformed character."
    NO_MALFORMED_CHARACTERS = "This phrase is perfect !"

    DOCUMENT_WITHOUT_TAB = False
    DOCUMENT_WITHOUT_PID = False
    DOCUMENT_WITH_NON_NUMERIC_PID = False
    DOCUMENT_WIHOUT_TEXT = False
    DOCUMENT_WITH_LINE_FEED = False
    DOCUMENT_WITH_SPACES_AND_LINE_FEED = False
    WELL_FORMED_DOCUMENT = True

    DICT_COLLECTION = {
        "1": "This is the first document to put in the document table",
        "2": "This is the second document",
        "3": "This is an other document to process"
    }

    PUNCTUATED_TOKEN = "This"
    PUNCTUATION = ""

    NORMALIZED_TOKENS = {"0": ['this', 'tokens', 'are', 'not', 'normalized']}

    SENTENCE_TOKENIZED = {
        "0": ['This,', 'sentence', 'is_', 'not', 'tokenized'],
        "1": ['This', 'one#', 'is', 'also:.', 'sentence', 'not', 'tokenized']
    }

    TEXT_PREPROCESSED = {
        "0": ['the', 'presence', 'of', 'communication', 'amid', 'scientific', 'minds', 'was', 'equally', 'important',
              'to', 'the', 'success', 'of', 'the', 'manhattan', 'project', 'as', 'scientific', 'intellect', 'was',
              'the', 'only', 'cloud', 'hanging', 'over', 'the', 'impressive', 'achievement', 'of', 'the', 'atomic',
              'researchers', 'and', 'engineers', 'is', 'what', 'their', 'success', 'truly', 'meant', 'hundreds', 'of',
              'thousands', 'of', 'innocent', 'lives', 'obliterated'],
        "1": ['the', 'manhattan', 'project', 'and', 'its', 'atomic', 'bomb', 'helped', 'bring', 'an', 'end', 'to',
              'world', 'war', 'ii', 'its', 'legacy', 'of', 'peaceful', 'uses', 'of', 'atomic', 'energy', 'continues',
              'to', 'have', 'an', 'impact', 'on', 'history', 'and', 'science'],
        "2": ['essay', 'on', 'the', 'manhattan', 'project', 'the', 'manhattan', 'project', 'the', 'manhattan',
              'project', 'was', 'to', 'see', 'if', 'making', 'an', 'atomic', 'bomb', 'possible', 'the', 'success', 'of',
              'this', 'project', 'would', 'forever', 'change', 'the', 'world', 'forever', 'making', 'it', 'known',
              'that', 'something', 'this', 'powerful', 'can', 'be', 'manmade'],
        "3": ['the', 'manhattan', 'project', 'was', 'the', 'name', 'for', 'project', 'conducted', 'during', 'world',
              'war', 'ii', 'to', 'develop', 'the', 'first', 'atomic', 'bomb', 'it', 'refers', 'specifically', 'to',
              'the', 'period', 'of', 'the', 'project', 'from', 'one', 'nine', 'four', 'two', 'one', 'nine', 'four',
              'six', 'under', 'the', 'control', 'of', 'the', 'us', 'army', 'corps', 'of', 'engineers', 'under', 'the',
              'administration', 'of', 'general', 'leslie', 'groves']
    }


class DocumentTableTestData(Enum):
    DICT_COLLECTION = {
        "1": "This is the first document to put in the document table",
        "2": "This is the second document",
        "3": "This is an other document to process"
    }

    DOCUMENT_TABLE_1 = {
        "1": {"docno": "doc_1", "doc_length": 11},
        "2": {"docno": "doc_2", "doc_length": 5},
        "3": {"docno": "doc_3", "doc_length": 7}
    }

    DOCUMENT_TABLE_2 = {
        "4": {"docno": "doc_4", "doc_length": 11},
        "5": {"docno": "doc_5", "doc_length": 5},
        "6": {"docno": "doc_6", "doc_length": 7}
    }

    MERGED_DOCUMENT_TABLE = {
        "4": {"docno": "doc_4", "doc_length": 11},
        "5": {"docno": "doc_5", "doc_length": 5},
        "6": {"docno": "doc_6", "doc_length": 7},
        "1": {"docno": "doc_1", "doc_length": 11},
        "2": {"docno": "doc_2", "doc_length": 5},
        "3": {"docno": "doc_3", "doc_length": 7}
    }


class DocumentTableExpectedData(Enum):
    DOCUMENT_TABLE_1 = {
        "1": {"docno": "doc_1", "doc_length": 11},
        "2": {"docno": "doc_2", "doc_length": 5},
        "3": {"docno": "doc_3", "doc_length": 7}
    }

    MERGED_DOCUMENT_TABLE = {
        "4": {"docno": "doc_4", "doc_length": 11},
        "5": {"docno": "doc_5", "doc_length": 5},
        "6": {"docno": "doc_6", "doc_length": 7},
        "1": {"docno": "doc_1", "doc_length": 11},
        "2": {"docno": "doc_2", "doc_length": 5},
        "3": {"docno": "doc_3", "doc_length": 7}
    }

    LOADED_DOCUMENT_TABLE = {
        "1": {"docno": "doc_1", "doc_length": 11},
        "2": {"docno": "doc_2", "doc_length": 5},
        "3": {"docno": "doc_3", "doc_length": 7},
        "4": {"docno": "doc_4", "doc_length": 11},
        "5": {"docno": "doc_5", "doc_length": 5},
        "6": {"docno": "doc_6", "doc_length": 7}
    }

    DOCUMENT_TABLE_FILE_CONTENT = "1:doc_1:11 2:doc_2:5 3:doc_3:7 4:doc_4:11 5:doc_5:5 6:doc_6:7"


class IndexerTestData(Enum):
    POSTING = (1, 10)

    TEXT_PREPROCESSED = {
        "0": ["presenc", "commun", "amid", "scientif", "mind", "equal", "import", "success", "manhattan", "project",
              "scientif", "intellect", "cloud", "hang", "impress", "achiev", "atom", "research", "engin", "success",
              "truli", "meant", "hundr", "thousand", "innoc", "live", "obliter"],
        "1": ["manhattan", "project", "atom", "bomb", "help", "bring", "end", "world", "war", "ii", "legaci", "peac",
              "use", "atom", "energi", "continu", "impact", "histori", "scienc"],
        "2": ["essay", "manhattan", "project", "manhattan", "project", "manhattan", "project", "see", "make", "atom",
              "bomb", "possibl", "success", "project", "would", "forev", "chang", "world", "forev", "make", "known",
              "someth", "power", "manmad"],
        "3": ["manhattan", "project", "name", "project", "conduct", "world", "war", "ii", "develop", "first", "atom",
              "bomb", "refer", "specif", "period", "project", "one", "nine", "four", "two", "one", "nine", "four",
              "six", "control", "us", "armi", "corp", "engin", "administr", "gener", "lesli", "grove"]
    }

    INVERTED_INDEX = {'presenc': {'0': 1}, 'commun': {'0': 1}, 'amid': {'0': 1}, 'scientif': {'0': 2}, 'mind': {'0': 1},
                      'equal': {'0': 1}, 'import': {'0': 1}, 'success': {'0': 2, '2': 1},
                      'manhattan': {'0': 1, '1': 1, '2': 3, '3': 1}, 'project': {'0': 1, '1': 1, '2': 4, '3': 3},
                      'intellect': {'0': 1}, 'cloud': {'0': 1}, 'hang': {'0': 1}, 'impress': {'0': 1},
                      'achiev': {'0': 1}, 'atom': {'0': 1, '1': 2, '2': 1, '3': 1}, 'research': {'0': 1},
                      'engin': {'0': 1, '3': 1}, 'truli': {'0': 1}, 'meant': {'0': 1}, 'hundr': {'0': 1},
                      'thousand': {'0': 1}, 'innoc': {'0': 1}, 'live': {'0': 1}, 'obliter': {'0': 1},
                      'bomb': {'1': 1, '2': 1, '3': 1}, 'help': {'1': 1}, 'bring': {'1': 1}, 'end': {'1': 1},
                      'world': {'1': 1, '2': 1, '3': 1}, 'war': {'1': 1, '3': 1}, 'ii': {'1': 1, '3': 1},
                      'legaci': {'1': 1}, 'peac': {'1': 1}, 'use': {'1': 1}, 'energi': {'1': 1}, 'continu': {'1': 1},
                      'impact': {'1': 1}, 'histori': {'1': 1}, 'scienc': {'1': 1}, 'essay': {'2': 1}, 'see': {'2': 1},
                      'make': {'2': 2}, 'possibl': {'2': 1}, 'would': {'2': 1}, 'forev': {'2': 2}, 'chang': {'2': 1},
                      'known': {'2': 1}, 'someth': {'2': 1}, 'power': {'2': 1}, 'manmad': {'2': 1}, 'name': {'3': 1},
                      'conduct': {'3': 1}, 'develop': {'3': 1}, 'first': {'3': 1}, 'refer': {'3': 1},
                      'specif': {'3': 1}, 'period': {'3': 1}, 'one': {'3': 2}, 'nine': {'3': 2}, 'four': {'3': 2},
                      'two': {'3': 1}, 'six': {'3': 1}, 'control': {'3': 1}, 'us': {'3': 1}, 'armi': {'3': 1},
                      'corp': {'3': 1}, 'administr': {'3': 1}, 'gener': {'3': 1}, 'lesli': {'3': 1}, 'grove': {'3': 1}}

    LEXICON_DICT = {'presenc': {'document_frequency': 1, 'offset': 0, 'posting_length': 4},
                    'commun': {'document_frequency': 1, 'offset': 4, 'posting_length': 4},
                    'amid': {'document_frequency': 1, 'offset': 8, 'posting_length': 4},
                    'scientif': {'document_frequency': 2, 'offset': 12, 'posting_length': 4},
                    'mind': {'document_frequency': 1, 'offset': 16, 'posting_length': 4},
                    'equal': {'document_frequency': 1, 'offset': 20, 'posting_length': 4},
                    'import': {'document_frequency': 1, 'offset': 24, 'posting_length': 4},
                    'success': {'document_frequency': 3, 'offset': 28, 'posting_length': 8},
                    'manhattan': {'document_frequency': 6, 'offset': 36, 'posting_length': 16},
                    'project': {'document_frequency': 9, 'offset': 52, 'posting_length': 16},
                    'intellect': {'document_frequency': 1, 'offset': 68, 'posting_length': 4},
                    'cloud': {'document_frequency': 1, 'offset': 72, 'posting_length': 4},
                    'hang': {'document_frequency': 1, 'offset': 76, 'posting_length': 4},
                    'impress': {'document_frequency': 1, 'offset': 80, 'posting_length': 4},
                    'achiev': {'document_frequency': 1, 'offset': 84, 'posting_length': 4},
                    'atom': {'document_frequency': 5, 'offset': 88, 'posting_length': 16},
                    'research': {'document_frequency': 1, 'offset': 104, 'posting_length': 4},
                    'engin': {'document_frequency': 2, 'offset': 108, 'posting_length': 8},
                    'truli': {'document_frequency': 1, 'offset': 116, 'posting_length': 4},
                    'meant': {'document_frequency': 1, 'offset': 120, 'posting_length': 4},
                    'hundr': {'document_frequency': 1, 'offset': 124, 'posting_length': 4},
                    'thousand': {'document_frequency': 1, 'offset': 128, 'posting_length': 4},
                    'innoc': {'document_frequency': 1, 'offset': 132, 'posting_length': 4},
                    'live': {'document_frequency': 1, 'offset': 136, 'posting_length': 4},
                    'obliter': {'document_frequency': 1, 'offset': 140, 'posting_length': 4},
                    'bomb': {'document_frequency': 3, 'offset': 144, 'posting_length': 12},
                    'help': {'document_frequency': 1, 'offset': 156, 'posting_length': 4},
                    'bring': {'document_frequency': 1, 'offset': 160, 'posting_length': 4},
                    'end': {'document_frequency': 1, 'offset': 164, 'posting_length': 4},
                    'world': {'document_frequency': 3, 'offset': 168, 'posting_length': 12},
                    'war': {'document_frequency': 2, 'offset': 180, 'posting_length': 8},
                    'ii': {'document_frequency': 2, 'offset': 188, 'posting_length': 8},
                    'legaci': {'document_frequency': 1, 'offset': 196, 'posting_length': 4},
                    'peac': {'document_frequency': 1, 'offset': 200, 'posting_length': 4},
                    'use': {'document_frequency': 1, 'offset': 204, 'posting_length': 4},
                    'energi': {'document_frequency': 1, 'offset': 208, 'posting_length': 4},
                    'continu': {'document_frequency': 1, 'offset': 212, 'posting_length': 4},
                    'impact': {'document_frequency': 1, 'offset': 216, 'posting_length': 4},
                    'histori': {'document_frequency': 1, 'offset': 220, 'posting_length': 4},
                    'scienc': {'document_frequency': 1, 'offset': 224, 'posting_length': 4},
                    'essay': {'document_frequency': 1, 'offset': 228, 'posting_length': 4},
                    'see': {'document_frequency': 1, 'offset': 232, 'posting_length': 4},
                    'make': {'document_frequency': 2, 'offset': 236, 'posting_length': 4},
                    'possibl': {'document_frequency': 1, 'offset': 240, 'posting_length': 4},
                    'would': {'document_frequency': 1, 'offset': 244, 'posting_length': 4},
                    'forev': {'document_frequency': 2, 'offset': 248, 'posting_length': 4},
                    'chang': {'document_frequency': 1, 'offset': 252, 'posting_length': 4},
                    'known': {'document_frequency': 1, 'offset': 256, 'posting_length': 4},
                    'someth': {'document_frequency': 1, 'offset': 260, 'posting_length': 4},
                    'power': {'document_frequency': 1, 'offset': 264, 'posting_length': 4},
                    'manmad': {'document_frequency': 1, 'offset': 268, 'posting_length': 4},
                    'name': {'document_frequency': 1, 'offset': 272, 'posting_length': 4},
                    'conduct': {'document_frequency': 1, 'offset': 276, 'posting_length': 4},
                    'develop': {'document_frequency': 1, 'offset': 280, 'posting_length': 4},
                    'first': {'document_frequency': 1, 'offset': 284, 'posting_length': 4},
                    'refer': {'document_frequency': 1, 'offset': 288, 'posting_length': 4},
                    'specif': {'document_frequency': 1, 'offset': 292, 'posting_length': 4},
                    'period': {'document_frequency': 1, 'offset': 296, 'posting_length': 4},
                    'one': {'document_frequency': 2, 'offset': 300, 'posting_length': 4},
                    'nine': {'document_frequency': 2, 'offset': 304, 'posting_length': 4},
                    'four': {'document_frequency': 2, 'offset': 308, 'posting_length': 4},
                    'two': {'document_frequency': 1, 'offset': 312, 'posting_length': 4},
                    'six': {'document_frequency': 1, 'offset': 316, 'posting_length': 4},
                    'control': {'document_frequency': 1, 'offset': 320, 'posting_length': 4},
                    'us': {'document_frequency': 1, 'offset': 324, 'posting_length': 4},
                    'armi': {'document_frequency': 1, 'offset': 328, 'posting_length': 4},
                    'corp': {'document_frequency': 1, 'offset': 332, 'posting_length': 4},
                    'administr': {'document_frequency': 1, 'offset': 336, 'posting_length': 4},
                    'gener': {'document_frequency': 1, 'offset': 340, 'posting_length': 4},
                    'lesli': {'document_frequency': 1, 'offset': 344, 'posting_length': 4},
                    'grove': {'document_frequency': 1, 'offset': 348, 'posting_length': 4}}

    INVERTED_INDEX_TO_MERGE_1 = {
        'presenc': {'0': 1}, 'commun': {'0': 1}, 'amid': {'0': 1}, 'scientif': {'0': 2},
        'mind': {'0': 1}, 'equal': {'0': 1}, 'import': {'0': 1}, 'success': {'0': 2, '2': 1},
        'manhattan': {'0': 1, '1': 1, '2': 3, '3': 1},
        'project': {'0': 1, '1': 1, '2': 4, '3': 3},
        'intellect': {'0': 1}, 'cloud': {'0': 1}, 'hang': {'0': 1}, 'impress': {'0': 1},
        'achiev': {'0': 1}, 'atom': {'0': 1, '1': 2, '2': 1, '3': 1}, 'research': {'0': 1},
        'engin': {'0': 1, '3': 1}, 'truli': {'0': 1}, 'meant': {'0': 1}, 'hundr': {'0': 1},
        'thousand': {'0': 1}, 'innoc': {'0': 1}, 'live': {'0': 1}, 'obliter': {'0': 1},
        'bomb': {'1': 1, '2': 1, '3': 1}, 'help': {'1': 1}, 'bring': {'1': 1}, 'end': {'1': 1},
        'world': {'1': 1, '2': 1, '3': 1}, 'war': {'1': 1, '3': 1}, 'ii': {'1': 1, '3': 1},
        'legaci': {'1': 1}, 'peac': {'1': 1}, 'use': {'1': 1}, 'energi': {'1': 1},
        'continu': {'1': 1}, 'impact': {'1': 1}, 'histori': {'1': 1}, 'scienc': {'1': 1}, 'essay': {'2': 1},
        'see': {'2': 1}
    }

    INVERTED_INDEX_TO_MERGE_2 = {
        'scientif': {'5': 4}, 'manhattan': {'5': 0}, 'project': {'5': 2, '4': 3}, 'intellect': {'5': 1},
        'research': {'5': 5}, 'engin': {'4': 2, '5': 1}, 'meant': {'4': 2}, 'innoc': {'4': 0}, 'help': {'4': 3},
        'bring': {'5': 3}, 'end': {'5': 1}, 'world': {'4': 3}, 'ii': {'5': 4, '4': 0}, 'legaci': {'5': 3},
        'peac': {'4': 3}, 'use': {'5': 1}, 'histori': {'4': 4}, 'scienc': {'4': 5}, 'possibl': {'5': 5},
        'chang': {'5': 1}, 'known': {'4': 1}, 'power': {'5': 4}, 'conduct': {'5': 4}, 'specif': {'4': 3},
        'one': {'4': 5}, 'four': {'4': 0}, 'two': {'5': 3}, 'control': {'4': 4}, 'armi': {'5': 4}, 'grove': {'5': 5}
    }

class IndexerExpectedData(Enum):
    POSTING = "1:10 "

    INVERTED_INDEX = {'presenc': {'0': 1}, 'commun': {'0': 1}, 'amid': {'0': 1}, 'scientif': {'0': 2}, 'mind': {'0': 1},
                      'equal': {'0': 1}, 'import': {'0': 1}, 'success': {'0': 2, '2': 1},
                      'manhattan': {'0': 1, '1': 1, '2': 3, '3': 1}, 'project': {'0': 1, '1': 1, '2': 4, '3': 3},
                      'intellect': {'0': 1}, 'cloud': {'0': 1}, 'hang': {'0': 1}, 'impress': {'0': 1},
                      'achiev': {'0': 1}, 'atom': {'0': 1, '1': 2, '2': 1, '3': 1}, 'research': {'0': 1},
                      'engin': {'0': 1, '3': 1}, 'truli': {'0': 1}, 'meant': {'0': 1}, 'hundr': {'0': 1},
                      'thousand': {'0': 1}, 'innoc': {'0': 1}, 'live': {'0': 1}, 'obliter': {'0': 1},
                      'bomb': {'1': 1, '2': 1, '3': 1}, 'help': {'1': 1}, 'bring': {'1': 1}, 'end': {'1': 1},
                      'world': {'1': 1, '2': 1, '3': 1}, 'war': {'1': 1, '3': 1}, 'ii': {'1': 1, '3': 1},
                      'legaci': {'1': 1}, 'peac': {'1': 1}, 'use': {'1': 1}, 'energi': {'1': 1}, 'continu': {'1': 1},
                      'impact': {'1': 1}, 'histori': {'1': 1}, 'scienc': {'1': 1}, 'essay': {'2': 1}, 'see': {'2': 1},
                      'make': {'2': 2}, 'possibl': {'2': 1}, 'would': {'2': 1}, 'forev': {'2': 2}, 'chang': {'2': 1},
                      'known': {'2': 1}, 'someth': {'2': 1}, 'power': {'2': 1}, 'manmad': {'2': 1}, 'name': {'3': 1},
                      'conduct': {'3': 1}, 'develop': {'3': 1}, 'first': {'3': 1}, 'refer': {'3': 1},
                      'specif': {'3': 1}, 'period': {'3': 1}, 'one': {'3': 2}, 'nine': {'3': 2}, 'four': {'3': 2},
                      'two': {'3': 1}, 'six': {'3': 1}, 'control': {'3': 1}, 'us': {'3': 1}, 'armi': {'3': 1},
                      'corp': {'3': 1}, 'administr': {'3': 1}, 'gener': {'3': 1}, 'lesli': {'3': 1}, 'grove': {'3': 1}}

    MERGED_INVERTED_INDEX = {'achiev': {'0': 1}, 'amid': {'0': 1}, 'armi': {'5': 4},
                             'atom': {'0': 1, '1': 2, '2': 1, '3': 1}, 'bomb': {'1': 1, '2': 1, '3': 1},
                             'bring': {'1': 1, '5': 3}, 'chang': {'5': 1}, 'cloud': {'0': 1}, 'commun': {'0': 1},
                             'conduct': {'5': 4}, 'continu': {'1': 1}, 'control': {'4': 4}, 'end': {'1': 1, '5': 1},
                             'energi': {'1': 1}, 'engin': {'0': 1, '3': 1, '4': 2, '5': 1}, 'equal': {'0': 1},
                             'essay': {'2': 1}, 'four': {'4': 0}, 'grove': {'5': 5}, 'hang': {'0': 1},
                             'help': {'1': 1, '4': 3}, 'histori': {'1': 1, '4': 4}, 'hundr': {'0': 1},
                             'ii': {'1': 1, '3': 1, '5': 4, '4': 0}, 'impact': {'1': 1}, 'import': {'0': 1},
                             'impress': {'0': 1}, 'innoc': {'0': 1, '4': 0}, 'intellect': {'0': 1, '5': 1},
                             'known': {'4': 1}, 'legaci': {'1': 1, '5': 3}, 'live': {'0': 1},
                             'manhattan': {'0': 1, '1': 1, '2': 3, '3': 1, '5': 0}, 'meant': {'0': 1, '4': 2},
                             'mind': {'0': 1}, 'obliter': {'0': 1}, 'one': {'4': 5}, 'peac': {'1': 1, '4': 3},
                             'possibl': {'5': 5}, 'power': {'5': 4}, 'presenc': {'0': 1},
                             'project': {'0': 1, '1': 1, '2': 4, '3': 3, '5': 2, '4': 3}, 'research': {'0': 1, '5': 5},
                             'scienc': {'1': 1, '4': 5}, 'scientif': {'0': 2, '5': 4}, 'see': {'2': 1},
                             'specif': {'4': 3}, 'success': {'0': 2, '2': 1}, 'thousand': {'0': 1}, 'truli': {'0': 1},
                             'two': {'5': 3}, 'use': {'1': 1, '5': 1}, 'war': {'1': 1, '3': 1},
                             'world': {'1': 1, '2': 1, '3': 1, '4': 3}}

    LEXICON_DICT = {'presenc': {'document_frequency': 1, 'offset': 0, 'posting_length': 4},
                    'commun': {'document_frequency': 1, 'offset': 4, 'posting_length': 4},
                    'amid': {'document_frequency': 1, 'offset': 8, 'posting_length': 4},
                    'scientif': {'document_frequency': 2, 'offset': 12, 'posting_length': 4},
                    'mind': {'document_frequency': 1, 'offset': 16, 'posting_length': 4},
                    'equal': {'document_frequency': 1, 'offset': 20, 'posting_length': 4},
                    'import': {'document_frequency': 1, 'offset': 24, 'posting_length': 4},
                    'success': {'document_frequency': 3, 'offset': 28, 'posting_length': 8},
                    'manhattan': {'document_frequency': 6, 'offset': 36, 'posting_length': 16},
                    'project': {'document_frequency': 9, 'offset': 52, 'posting_length': 16},
                    'intellect': {'document_frequency': 1, 'offset': 68, 'posting_length': 4},
                    'cloud': {'document_frequency': 1, 'offset': 72, 'posting_length': 4},
                    'hang': {'document_frequency': 1, 'offset': 76, 'posting_length': 4},
                    'impress': {'document_frequency': 1, 'offset': 80, 'posting_length': 4},
                    'achiev': {'document_frequency': 1, 'offset': 84, 'posting_length': 4},
                    'atom': {'document_frequency': 5, 'offset': 88, 'posting_length': 16},
                    'research': {'document_frequency': 1, 'offset': 104, 'posting_length': 4},
                    'engin': {'document_frequency': 2, 'offset': 108, 'posting_length': 8},
                    'truli': {'document_frequency': 1, 'offset': 116, 'posting_length': 4},
                    'meant': {'document_frequency': 1, 'offset': 120, 'posting_length': 4},
                    'hundr': {'document_frequency': 1, 'offset': 124, 'posting_length': 4},
                    'thousand': {'document_frequency': 1, 'offset': 128, 'posting_length': 4},
                    'innoc': {'document_frequency': 1, 'offset': 132, 'posting_length': 4},
                    'live': {'document_frequency': 1, 'offset': 136, 'posting_length': 4},
                    'obliter': {'document_frequency': 1, 'offset': 140, 'posting_length': 4},
                    'bomb': {'document_frequency': 3, 'offset': 144, 'posting_length': 12},
                    'help': {'document_frequency': 1, 'offset': 156, 'posting_length': 4},
                    'bring': {'document_frequency': 1, 'offset': 160, 'posting_length': 4},
                    'end': {'document_frequency': 1, 'offset': 164, 'posting_length': 4},
                    'world': {'document_frequency': 3, 'offset': 168, 'posting_length': 12},
                    'war': {'document_frequency': 2, 'offset': 180, 'posting_length': 8},
                    'ii': {'document_frequency': 2, 'offset': 188, 'posting_length': 8},
                    'legaci': {'document_frequency': 1, 'offset': 196, 'posting_length': 4},
                    'peac': {'document_frequency': 1, 'offset': 200, 'posting_length': 4},
                    'use': {'document_frequency': 1, 'offset': 204, 'posting_length': 4},
                    'energi': {'document_frequency': 1, 'offset': 208, 'posting_length': 4},
                    'continu': {'document_frequency': 1, 'offset': 212, 'posting_length': 4},
                    'impact': {'document_frequency': 1, 'offset': 216, 'posting_length': 4},
                    'histori': {'document_frequency': 1, 'offset': 220, 'posting_length': 4},
                    'scienc': {'document_frequency': 1, 'offset': 224, 'posting_length': 4},
                    'essay': {'document_frequency': 1, 'offset': 228, 'posting_length': 4},
                    'see': {'document_frequency': 1, 'offset': 232, 'posting_length': 4},
                    'make': {'document_frequency': 2, 'offset': 236, 'posting_length': 4},
                    'possibl': {'document_frequency': 1, 'offset': 240, 'posting_length': 4},
                    'would': {'document_frequency': 1, 'offset': 244, 'posting_length': 4},
                    'forev': {'document_frequency': 2, 'offset': 248, 'posting_length': 4},
                    'chang': {'document_frequency': 1, 'offset': 252, 'posting_length': 4},
                    'known': {'document_frequency': 1, 'offset': 256, 'posting_length': 4},
                    'someth': {'document_frequency': 1, 'offset': 260, 'posting_length': 4},
                    'power': {'document_frequency': 1, 'offset': 264, 'posting_length': 4},
                    'manmad': {'document_frequency': 1, 'offset': 268, 'posting_length': 4},
                    'name': {'document_frequency': 1, 'offset': 272, 'posting_length': 4},
                    'conduct': {'document_frequency': 1, 'offset': 276, 'posting_length': 4},
                    'develop': {'document_frequency': 1, 'offset': 280, 'posting_length': 4},
                    'first': {'document_frequency': 1, 'offset': 284, 'posting_length': 4},
                    'refer': {'document_frequency': 1, 'offset': 288, 'posting_length': 4},
                    'specif': {'document_frequency': 1, 'offset': 292, 'posting_length': 4},
                    'period': {'document_frequency': 1, 'offset': 296, 'posting_length': 4},
                    'one': {'document_frequency': 2, 'offset': 300, 'posting_length': 4},
                    'nine': {'document_frequency': 2, 'offset': 304, 'posting_length': 4},
                    'four': {'document_frequency': 2, 'offset': 308, 'posting_length': 4},
                    'two': {'document_frequency': 1, 'offset': 312, 'posting_length': 4},
                    'six': {'document_frequency': 1, 'offset': 316, 'posting_length': 4},
                    'control': {'document_frequency': 1, 'offset': 320, 'posting_length': 4},
                    'us': {'document_frequency': 1, 'offset': 324, 'posting_length': 4},
                    'armi': {'document_frequency': 1, 'offset': 328, 'posting_length': 4},
                    'corp': {'document_frequency': 1, 'offset': 332, 'posting_length': 4},
                    'administr': {'document_frequency': 1, 'offset': 336, 'posting_length': 4},
                    'gener': {'document_frequency': 1, 'offset': 340, 'posting_length': 4},
                    'lesli': {'document_frequency': 1, 'offset': 344, 'posting_length': 4},
                    'grove': {'document_frequency': 1, 'offset': 348, 'posting_length': 4}}

    LEXICON_FILE_CONTENT = "achiev:1:84:4 administr:1:336:4 amid:1:8:4 armi:1:328:4 atom:5:88:16 bomb:3:144:12 bring:1:160:4 chang:1:252:4 cloud:1:72:4 commun:1:4:4 conduct:1:276:4 continu:1:212:4 control:1:320:4 corp:1:332:4 develop:1:280:4 end:1:164:4 energi:1:208:4 engin:2:108:8 equal:1:20:4 essay:1:228:4 first:1:284:4 forev:2:248:4 four:2:308:4 gener:1:340:4 grove:1:348:4 hang:1:76:4 help:1:156:4 histori:1:220:4 hundr:1:124:4 ii:2:188:8 impact:1:216:4 import:1:24:4 impress:1:80:4 innoc:1:132:4 intellect:1:68:4 known:1:256:4 legaci:1:196:4 lesli:1:344:4 live:1:136:4 make:2:236:4 manhattan:6:36:16 manmad:1:268:4 meant:1:120:4 mind:1:16:4 name:1:272:4 nine:2:304:4 obliter:1:140:4 one:2:300:4 peac:1:200:4 period:1:296:4 possibl:1:240:4 power:1:264:4 presenc:1:0:4 project:9:52:16 refer:1:288:4 research:1:104:4 scienc:1:224:4 scientif:2:12:4 see:1:232:4 six:1:316:4 someth:1:260:4 specif:1:292:4 success:3:28:8 thousand:1:128:4 truli:1:116:4 two:1:312:4 us:1:324:4 use:1:204:4 war:2:180:8 world:3:168:12 would:1:244:4 "

    INVERTED_INDEX_FILE_CONTENT = "0:1 0:1 0:1 0:2 0:1 0:1 0:1 0:2 2:1 0:1 1:1 2:3 3:1 0:1 1:1 2:4 3:3 0:1 0:1 0:1 0:1 0:1 0:1 1:2 2:1 3:1 0:1 0:1 3:1 0:1 0:1 0:1 0:1 0:1 0:1 0:1 1:1 2:1 3:1 1:1 1:1 1:1 1:1 2:1 3:1 1:1 3:1 1:1 3:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 1:1 2:1 2:1 2:2 2:1 2:1 2:2 2:1 2:1 2:1 2:1 2:1 3:1 3:1 3:1 3:1 3:1 3:1 3:1 3:2 3:2 3:2 3:1 3:1 3:1 3:1 3:1 3:1 3:1 3:1 3:1 3:1 "
