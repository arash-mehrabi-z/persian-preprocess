from invertedIndex.invertedIndex import InvertedIndex
from invertedIndex.document import Document
from invertedIndex.documentStore import DocumentStore
import xml.etree.ElementTree as ET
import preprocess
import stopword
import time

doc_store = DocumentStore() 
index = InvertedIndex()

def read_file(file_address):
    with open(file_address, 'r', encoding = 'utf-8') as f:
        file_content = f.read()

    return file_content

def is_xml():
    return True

def normalize(text):
    preprocessed = preprocess.PreProcess(text)
    preprocessed.normalize_letter()
    preprocessed.remove_punctuation()
    return preprocessed

def not_null(obj):
    return obj != None

def tokenize(normalized):
    if not_null(normalized):
        tokens = normalized.split()
        return remove_stopwords(tokens)
    else: return normalized

def remove_stopwords(tokens):
    sword = stopword.StopWord()
    return sword.remove_stopwords(tokens)

def tokens_is_not_empty(tokens):
    return tokens

def add_to_doc_store(document):
    global doc_store
    doc_store.add(document)

def get_normalized_text_of(doc, element_text):
    element = doc.find(element_text)
    if not_null(element):
        normalized_element = normalize(element.text)
        return normalized_element.get_text()
    else: return element

def create_doc(doc):
    normalized_title_text = get_normalized_text_of(doc, 'title')
    normalized_abstract_text = get_normalized_text_of(doc, 'abstract')
    document = Document(normalized_title_text, normalized_abstract_text)
    add_to_doc_store(document)
    return document

def add_to_inverted_index(document, tokens):
    global index
    if not_null(tokens):
        index.add(document, tokens)

def write_index_to_file(index):
    f = open("persianPreProcess/data/index.txt", "w")
    f.write(str(index))
    f.close()

def get_time():
    return time.time()

def print_status(document, start_time):
    if document.getDocId() % 1500 == 0:
        print(document.getDocId(), time.time() - start_time)

def parse_xml(file_content):
    start_time = get_time()
    root = ET.fromstring(file_content)
    for doc in root:
        document = create_doc(doc)
        tokens = tokenize(document.getBody())
        add_to_inverted_index(document, tokens)
        print_status(document, start_time)
    write_index_to_file(index)
        
if __name__ == '__main__':
    file_address = "/home/arash/learning/information_retrieval/assignment/ir/persianPreProcess/data/simple.xml"

    file_content = read_file(file_address)
    if(is_xml()):
        parse_xml(file_content)






