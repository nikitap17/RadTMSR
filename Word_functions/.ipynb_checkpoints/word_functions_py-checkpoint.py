# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:03:55 2024

@author: nikit
"""

import re
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_sm')
from collections import Counter


### Functions for data cleaning

def strip_characters(string):
    '''
    Intended use with pd.DataFrame.apply() function.
    '''
    string = re.sub(r"[^a-zA-Z -]|\b[nN]\b| - ", "", string)
    string = re.sub(" {2,}", " ", string)
    return string

def POS_tagging(string, extract_pos = ["NOUN","ADJ"]):
    '''
    Intended use with pd.DataFrame.apply() function.
    '''
    doc = nlp(string)
    doc2 = " ".join([token.text for token in doc if token.pos_ in extract_pos])
    doc2 = re.sub(" - ", " ", doc2)
    return doc2

def lemmatisation(string):
    '''
    Intended use with pd.DataFrame.apply() function.
    '''
    doc = nlp(string)
    
    lem_spacy = []
    for token in doc: 
        lem_spacy.append(token.lemma_)
    doc2 = " ".join(lem_spacy)
    #doc2 = re.sub(" - ", "-", doc2)
    return doc2



### Functions for N-gram extraction

def ngram_extractor(doc_list):
    '''
    Building one list(1) of lists(2) of strings. Each list(2) includes all possible combinations of three words, that is,
    one 3-gram, two 2-grams, and 3 1-grams.
    '''

    doc = []
    for idx in range(len(doc_list)-2):
        combo_list = [" ".join(doc_list[idx:idx+3])] + [" ".join(doc_list[idx:idx+2])] + [" ".join(doc_list[idx+1:idx+3])] + [doc_list[idx]] + [doc_list[idx+1]] + [doc_list[idx+2]]
        doc.append(combo_list)
    
    return doc


def trigram_to_nounbydoc(df):
    data = df.copy(deep=True)
    data["trigrams"] = data.ngram.apply(lambda x: Counter([element[0] for element in x]))
    
    ids = list(data.record_id)
    tri_count = [len(trigram) for trigram in data.trigrams]
    trigrams_list = sum(data.trigrams.apply(lambda x: list(x.keys())),[])
    freq_list = sum(data.trigrams.apply(lambda x: list(x.values())),[])

    new_ids = []
    for idx,count in enumerate(tri_count):
        new_ids += [ids[idx]] * count

    nounbydoc = pd.DataFrame({"doc_id" : new_ids,
                              "term" : trigrams_list,
                              "freq" : freq_list})

    return nounbydoc


def bigram_to_nounbydoc(df):
    
    data = df.copy(deep=True)
    data["bigrams"] = data.residual_ngrams.apply(lambda x: Counter(sum([[element[0], element[1]] for element in x],[])))
    
    ids = list(data.record_id)
    bi_count = [len(bigram) for bigram in data.bigrams]
    bigrams_list = sum(data.bigrams.apply(lambda x: list(x.keys())),[])
    freq_list = sum(data.bigrams.apply(lambda x: list(x.values())),[])

    new_ids = []
    for idx,count in enumerate(bi_count):
        new_ids += [ids[idx]] * count

    nounbydoc = pd.DataFrame({"doc_id" : new_ids,
                              "term" : bigrams_list,
                              "freq" : freq_list})
    
    return nounbydoc


def relevant_bigrams(data_residual_ngrams, meaningful_bigrams):
    bigrams = []
    single_words = []
    for alist in data_residual_ngrams:
        if alist[0] in meaningful_bigrams and alist[1] in meaningful_bigrams:
            bigrams.append(alist[0])
            bigrams.append(alist[1])
        elif alist[0] in meaningful_bigrams:
            bigrams.append(alist[0])
        elif alist[1] in meaningful_bigrams:
            bigrams.append(alist[1])
        else:
            single_words.extend(alist[2:])
    return bigrams, single_words



### Functions for CLassification and Replacements

def classification(list_of_words, word_dict):
    '''
    Counts frequency of words falling into categories as pre-defined by a
    regex dictionary.

    Parameters
    ----------
    list_of_words : list
        The list should consist of strings, representing (key)words.
    word_dict : dict
        The dictionary classifies different regex patterns. The dict().values() should
        be a list of strings (regex patterns)

    Returns
    -------
    count_dict : dict
        A dictionary including the category names as values and their frequency counts
        as values.
    uniques_list : list
        A list of strings.
    terms_in_cat_dict : dict
        A dictionary including the category names as keys and a list of categorised
        tokens from the corpus as values.
    '''
    count_dict = {key: 0 for key in word_dict}
    terms_in_cat_dict = {key: set() for key in word_dict}
    uniques_list = []

    for token in list_of_words:
        not_detected = True
        for term in word_dict.keys():
            synonym_list = []
            for pattern in word_dict[term]:
                synonym_list += re.findall(pattern, token)
            if synonym_list:
                count_dict[term] += 1
                terms_in_cat_dict[term].update([token])
                not_detected = False
                
        if not_detected:
            uniques_list.append(token)
            
    return count_dict, uniques_list, terms_in_cat_dict



def extend_keywords(data_kw, word_dict):
    '''
    Categorises keywords as according to a regex dictionary and replaces original
    (key)words with overarching categories. One keyword can be classified into multiple categories.
    Intended use with the pd.DataFrame.apply() function.

    Parameters
    ----------
    data_kw : list
        List of strings.
    word_dict : dict
        The dictionary classifies different regex patterns. The values should
        be a list of strings (regex patterns).

    Returns
    -------
    list
        List of strings. Strings that have been matched with a dictionary class are replaced
        by the key term, respectively.
    '''
    new_kw_list = []
    for token in data_kw:
        not_detected = True
        
        for term in word_dict.keys():
            synonym_list = []
            for pattern in word_dict[term]:
                synonym_list += re.findall(pattern, token)
            if synonym_list:
                new_kw_list.append(term)
                not_detected = False
                
        if not_detected:
            new_kw_list.append(token)
            
    return list(set(new_kw_list))


def to_nounbydoc(data):
    '''
    Transforms a document-strring pd.DataFrame() from a "wide" to a "long" format.
    The columns "record_id" and "cat_keywords" should be defined in the data frame.

    Parameters
    ----------
    data : pd.DataFrame()

    Returns
    -------
    nounbydoc : pd.DataFrame()
    '''
    ids = list(data.record_id)
    kw_count = [len(kw_list) for kw_list in data.cat_keywords]
    kw = sum(data.cat_keywords, [])

    new_ids = []
    for idx,count in enumerate(kw_count):
        new_ids += [ids[idx]] * count

    nounbydoc = pd.DataFrame({"doc_id" : new_ids,
                              "term" : kw,
                              "freq" : 1})
    
    return nounbydoc

