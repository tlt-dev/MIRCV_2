# MIRCV_project

# Purpose
The goal of the project is to build an efficient search engine based on an inverted index.

Two tools are implemented :
- indexing.py : this tool preprocesses the document collection and build the inverted index
- query.py : this tool processes the queries to give the most relevant documents in the collection

##The index must be built before launching the query tool##

# Installation
Before launching the programs, please install the required dependencies:
```
pip install -r requirements.txt
```

# Indexing.py
To run:
```
python indexing.py --stopwords --stemming --use_compression
```

Options:
```
indexing.py [-h] [--collection_path COLLECTION_PATH] [--stopwords] [--stemming] [--use_compression] [--test] [--binary]

options:
  -h, --help            show this help message and exit
  --collection_path COLLECTION_PATH
                        Documents collection path
  --stopwords           Process stop_word removal
  --stemming            Process stemming with Porter Algorithm
  --use_compression     If true, use binary format for performance
  --test                If true, test dataset is used (results in data/tests/)
  --binary              If true, test will be proceed with compression (results in data/tests/)
```

# Query.py
To run:
```
python query.py
```

Options:
```
options:
  -h, --help            show this help message and exit
  --scoring_function {bm25,tfidf}
  --query_type {AND,OR}
  --test
```








