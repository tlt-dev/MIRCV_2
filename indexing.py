import shutil
import tarfile

from document_processing.Config import Config
from document_processing.DocumentParser import preprocess
from inverted_index.Indexer import Indexer
from inverted_index.DocumentTable import *
from timeit import default_timer as timer
from multiprocessing import Pool

import argparse
import json
import os

PROCESS_NB = 8

def uncompressed_collection(collection="data/collection.tar"):
    pass

def prepare_inputs_file(config):
    paths = ["input", "preprocessed_files", "temp_document_tables"]
    for path in paths:
        if os.path.exists(config.base_dir + path):
            shutil.rmtree(config.base_dir + path)

        os.mkdir(config.base_dir + path)

    with open(config.collection_path, 'r') as f:
        for total_lines, line in enumerate(f):
            pass
    total_lines = total_lines + 1

    line_per_file = int(total_lines / PROCESS_NB)
    print(line_per_file)
    file_number = 1
    current_datafile = None
    with open(config.collection_path) as f:
        for i, line in enumerate(f):
            if i % line_per_file == 0:
                if current_datafile:
                    current_datafile.close()
                current_datafile = open(config.base_dir + "input/data_{}.tsv".format(file_number), "w")
                file_number += 1
            current_datafile.write(line)
        if current_datafile:
            current_datafile.close()

    return total_lines


def task(task_data):
    try:
        print("Task started for {}".format(task_data[0]))

        base_dir = task_data[1].base_dir
        input_file_path = base_dir + "input/{}.tsv".format(task_data[0])
        document_table_file_path = base_dir + "temp_document_tables/temp_document_table_{}.json".format(task_data[0])

        with open(input_file_path, "r") as input_file:
            content = input_file.read()
        input_file.close()

        preprocessed_collection, document_table = preprocess(text_collection=content, stopwords=task_data[1].stopwords)

        with open(document_table_file_path, "w") as document_table_file:
            document_table_file.write(json.dumps(document_table))
        document_table_file.close()

        indexer = Indexer()
        indexer.build_index(preprocessed_collection)
        indexer.write_lexicon(base_dir + "lexicon.txt")

        print("Task completed for {}".format(task_data[0]))

        return indexer
    except Exception as e:
        print(f"Error processing {task_data[0]}: {str(e)}")


def run():
    start = timer()
    parser = argparse.ArgumentParser(description="MIRCV project")
    parser.add_argument("--collection_path", action="store", help="Documents collection path")
    parser.add_argument("--stopwords", action="store_true", help="Process stop_word removal")
    parser.add_argument("--stemming", action="store_true", help="Process stemming with Porter Algorithm")
    parser.add_argument('--use_compression', action='store_true', help='If true, use binary format for performance')
    parser.add_argument('--test', action='store_true', help='If true, test dataset is used (results in data/tests/')
    parser.add_argument('--binary', action='store_true', help='If true, test dataset is used (results in data/tests/')

    args = parser.parse_args()

    if args.collection_path:
        if not os.path.exists(args.collection_path):
            raise FileNotFoundError(
                "The document collection file  < " + args.collection_path + " >  is not found. Please check the file path and try again.")
    else:
        args.collection_path = None

    config = Config(collection_path=args.collection_path, stopwords=args.stopwords, stemming=args.stemming, compression=args.use_compression, test=args.test, binary=args.binary)

    prepare_inputs_file(config)

    params = []
    for i in range(1, PROCESS_NB + 1):
        params.append(["data_{}".format(str(i)), config])

    pool = Pool(processes=PROCESS_NB)
    temp_indexes = pool.map(task, params)
    final_inverted_index = Indexer()
    for inverted_index in temp_indexes:
        final_inverted_index.merge_index(inverted_index)

    base_dir = config.base_dir
    final_document_table = {}
    for i in range(1, PROCESS_NB + 1):
        with open(base_dir + "temp_document_tables/temp_document_table_data_{}.json".format(i), "r") as f:
            document_table = json.loads(f.read())
        f.close()
        final_document_table = merge_document_tables(final_document_table, document_table)

    if config.compression:
        final_inverted_index.write_compressed_index(base_dir + "compressed_inverted_index.bin")
    else:
        final_inverted_index.write_index(base_dir + "inverted_index.txt", final_index=True)
    final_inverted_index.write_lexicon(base_dir + "lexicon.txt")

    write_document_table(final_document_table, base_dir + "document_table.txt")


    end = timer()
    print(end - start)


if __name__ == '__main__':
    run()